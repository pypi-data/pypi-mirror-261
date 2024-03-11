from typing import List, Annotated
import time
import asyncio

from fastapi import FastAPI, HTTPException, Depends, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncssh
from agentdesk.server.models import V1Desktop, V1DesktopReqeust, V1Desktops
from agentdesk.vm import DesktopVM
from agentdesk import Desktop
from agentdesk.util import find_open_port
import requests
import os

from guisurfer.auth.transport import get_current_user
from .models import (
    DesktopRuntimeModel,
    SSHKeyModel,
    DesktopRuntimesModel,
    CreateDesktopRuntimeModel,
    SSHKeysModel,
    SSHKeyCreateModel,
    TaskModel,
    TaskCreateModel,
    TaskUpdateModel,
    PostMessageModel,
    V1UserProfile,
    CreateDesktopModel,
    ActionModel,
    ActionResponseModel,
    AgentRuntimeModel,
    AgentRuntimesModel,
    CreateAgentRuntimeModel,
    CreateAgentModel,
    AgentModel,
    AgentsModel,
    AgentTypeModel,
    AgentTypesModel,
    CreateAgentTypeModel,
    TasksModel,
)
from .runtime import DesktopRuntime
from .key import SSHKeyPair
from .boot import boot_seq
from guisurfer.agent.task import Task
from guisurfer.agent.base import TaskAgent, TaskAgentInstance
from guisurfer.agent.types import AgentType
from guisurfer.agent.env import HUB_API_KEY_ENV
from guisurfer.agent.runtime import AgentRuntime

boot_seq()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000, http://localhost:3001",
        "https://surf.agentlabs.xyz",
        "https://surf.dev.agentlabs.xyz",
        "https://surf.deploy.agentlabs.xyz",
        "https://surf.stg.agentlabs.xyz",
        "https://surf.testing.agentlabs.xyz",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Agent in the shell"}


@app.get("/health")
async def health():
    return {"status": "ok"}


async def ssh_proxy(
    websocket: WebSocket,
    host: str,
    username: str,
    private_ssh_key: str,
    port: int = 6080,
):
    # Connect to the SSH server using the private key for authentication
    async with asyncssh.connect(
        host,
        port=port,
        username=username,
        client_keys=[asyncssh.import_private_key(private_ssh_key)],
    ) as conn:
        # Open a direct TCP/IP channel to the destination (WebSocket service)
        async with conn.open_connection("localhost", 6080) as ssh_conn:
            try:
                await websocket.accept()
                while True:
                    # Wait for data from either the WebSocket or the SSH connection
                    tasks = [
                        asyncio.create_task(websocket.receive_text()),
                        asyncio.create_task(ssh_conn.reader.read(65536)),
                    ]
                    done, pending = await asyncio.wait(
                        tasks, return_when=asyncio.FIRST_COMPLETED
                    )

                    # Relay data received from the WebSocket to the SSH connection
                    for task in done:
                        if task == tasks[0]:  # Data received from WebSocket
                            data = task.result()
                            ssh_conn.writer.write(data.encode())
                            await ssh_conn.writer.drain()
                        else:  # Data received from SSH connection
                            data = task.result()
                            await websocket.send_text(data.decode())

                    for task in pending:
                        task.cancel()

            except WebSocketDisconnect:
                print("WebSocket disconnected")
            except Exception as e:
                print(f"Error: {e}")


@app.websocket("/ws/vnc/{desktop_name}")
async def websocket_proxy(
    websocket: WebSocket,
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    desktop_name: str,
):
    found = Desktop.find(owner_id=current_user.email, name=desktop_name)
    if len(found) == 0:
        raise HTTPException(status_code=404, detail=f"Desktop {desktop_name} not found")
    desktop = found[0]

    found = SSHKeyPair.find(owner_id=current_user.email, public_key=desktop.ssh_key)
    if len(found) == 0:
        raise HTTPException(
            status_code=404, detail=f"SSH key for desktop {desktop_name} not found"
        )

    key_pair = found[0]
    private_key = key_pair.decrypt_private_key(key_pair.private_key)

    # Proxy the WebSocket connection to the SSH connection
    await ssh_proxy(
        websocket, desktop.addr, username="agentsea", ssh_private_key=private_key
    )


@app.post("/v1/sshkeys", response_model=SSHKeyModel)
async def create_ssh_key(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: SSHKeyCreateModel,
):
    ssh_key = SSHKeyPair(
        name=data.name,
        public_key=data.public_key,
        private_key=data.private_key,
        owner_id=current_user.email,
    )
    return ssh_key.to_schema()


@app.get("/v1/sshkeys", response_model=SSHKeysModel)
async def get_ssh_keys(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)]
):
    keys = SSHKeyPair.find(owner_id=current_user.email)
    return SSHKeysModel(keys=[key.to_schema() for key in keys])


@app.delete("/v1/sshkeys/{name}")
async def delete_ssh_keys(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    SSHKeyPair.delete(name=name, owner_id=current_user.email)
    return {"message": "SSH key deleted successfully"}


# ---


@app.post("/v1/desktops", response_model=V1Desktop)
async def create_desktop(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: CreateDesktopModel,
):
    runtimes = DesktopRuntime.find(owner_id=current_user.email, name=data.runtime)
    if len(runtimes) == 0:
        raise HTTPException(status_code=404, detail=f"Runtime {data.runtime} not found")
    runtime = runtimes[0]

    vm: DesktopVM = runtime.create(
        name=data.name,
        owner_id=current_user.email,
        ssh_key_name=data.ssh_key_name,
        gce_opts=data.gce_opts,
        ec2_opts=data.ec2_opts,
        image=data.image,
        memory=data.memory,
        cpu=data.cpu,
        disk=data.disk,
        tags=data.tags,
        reserve_ip=data.reserve_ip,
    )

    return vm.to_v1_schema()


@app.get("/v1/desktops", response_model=V1Desktops)
async def get_desktops(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)]
):
    desktops = Desktop.find(owner_id=current_user.email)
    return V1Desktops(desktops=[desktop.to_v1_schema() for desktop in desktops])


@app.get("/v1/desktops/{name}", response_model=V1Desktop)
async def get_desktop(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    found = Desktop.find(name=name, owner_id=current_user.email)
    if not found:
        raise HTTPException(status_code=404, detail="Desktop not found")

    return found[0].to_v1_schema()


@app.delete("/v1/desktops/{name}")
async def delete_desktop(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    found = Desktop.find(name=name, owner_id=current_user.email)
    if not found:
        raise HTTPException(status_code=404, detail="Desktop not found")

    found[0].delete()


@app.post("/v1/desktops/{name}/exec", response_model=V1Desktop)
async def exec_desktop(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    name: str,
    action: ActionModel,
):
    found_desktops = Desktop.find(owner_id=current_user.email, name=name)
    if not found_desktops:
        raise HTTPException(status_code=404, detail="Desktop not found")
    desktop_vm = found_desktops[0]

    found_keys = SSHKeyPair.find(
        owner_id=current_user.email, public_key=desktop_vm.ssh_key
    )
    if not found_keys:
        raise HTTPException(status_code=404, detail="SSH key not found")
    key_pair = found_keys[0]
    private_key = key_pair.decrypt_private_key(key_pair.private_key)

    proxy_port = find_open_port()
    remote_port = 8000

    async with asyncssh.connect(
        desktop_vm.addr,
        username="agentsea",
        client_keys=[asyncssh.import_private_key(private_key)],
        known_hosts=None,
    ) as conn:
        # Setup port forwarding from localhost:proxy_port to desktop.addr:remote_port
        await conn.forward_local_port("localhost", proxy_port, "localhost", remote_port)

        desktop = Desktop(
            agentd_url=f"http://localhost:{proxy_port}", proxy_type="custom"
        )

        found_action = desktop.find_action(action.name)
        if not found_action:
            raise HTTPException(status_code=404, detail="Action not found")

        try:
            result = desktop.use(found_action, **action.parameters)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"failed to execute action {e}")

    return ActionResponseModel(
        action=action.name, result=str(result), parameters=action.parameters
    )


# ---


@app.post("/v1/runtimes/desktops", response_model=DesktopRuntimeModel)
async def create_desktop_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: CreateDesktopRuntimeModel,
):
    runtime = DesktopRuntime(
        provider=data.provider,
        credentials=data.credentials,
        name=data.name,
        owner_id=current_user.email,
    )
    return runtime.to_schema()


@app.get("/v1/runtimes/desktops", response_model=DesktopRuntimesModel)
async def get_desktop_runtimes(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)]
):
    runtimes = DesktopRuntime.find(owner_id=current_user.email)
    return DesktopRuntimesModel(runtimes=[runtime.to_schema() for runtime in runtimes])


@app.get("/v1/runtimes/desktops/{name}", response_model=DesktopRuntimeModel)
async def get_desktop_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    runtime = DesktopRuntime.find(name=name, owner_id=current_user.email)
    if not runtime:
        raise HTTPException(status_code=404, detail="DesktopRuntime not found")
    return runtime[0].to_schema()


@app.delete("/v1/runtimes/desktops/{name}")
async def delete_desktop_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    DesktopRuntime.delete(name=name, owner_id=current_user.email)
    return {"message": "DesktopRuntime deleted successfully"}


# ---


@app.post("/v1/runtimes/agents", response_model=AgentRuntimeModel)
async def create_agent_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: CreateAgentRuntimeModel,
):
    runtime = AgentRuntime(
        provider=data.provider,
        credentials=data.credentials,
        name=data.name,
        owner_id=current_user.email,
    )
    return runtime.to_schema()


@app.get("/v1/runtimes/agents", response_model=AgentRuntimesModel)
async def get_agent_runtimes(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)]
):
    runtimes = AgentRuntime.find(owner_id=current_user.email)
    return AgentRuntimesModel(runtimes=[runtime.to_schema() for runtime in runtimes])


@app.get("/v1/runtimes/agents/{name}", response_model=AgentRuntimeModel)
async def get_agent_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    runtime = AgentRuntime.find(name=name, owner_id=current_user.email)
    if not runtime:
        raise HTTPException(status_code=404, detail="DesktopRuntime not found")
    return runtime[0].to_schema()


@app.delete("/v1/runtimes/agents/{name}")
async def delete_agent_runtime(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    AgentRuntime.delete(name=name, owner_id=current_user.email)
    return {"message": "DesktopRuntime deleted successfully"}


# ---


@app.post("/v1/agents", response_model=AgentModel)
async def create_agent(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: CreateAgentModel,
):
    print("creating agent with model: ", data)
    if data.desktop:
        print("finding desktop...")
        desktop_vms = Desktop.find(name=data.desktop, owner_id=current_user.email)
        if not desktop_vms:
            raise HTTPException(status_code=404, detail="Desktop not found")
        desktop_vm = desktop_vms[0]

    elif data.desktop_request:
        print("creating desktop...")
        desktop_runtimes = DesktopRuntime.find(
            name=data.desktop_request.runtime, owner_id=current_user.email
        )
        if not desktop_runtimes:
            raise HTTPException(status_code=404, detail="DesktopRuntime not found")
        desktop_runtime = desktop_runtimes[0]

        desktop_vm = desktop_runtime.create(
            ssh_key_name=data.desktop_request.ssh_key_name,
            gce_opts=data.desktop_request.gce_opts,
            ec2_opts=data.desktop_request.ec2_opts,
            name=data.desktop_request.name,
            image=data.desktop_request.image,
            memory=data.desktop_request.memory,
            cpu=data.desktop_request.cpu,
            disk=data.desktop_request.disk,
            tags=data.desktop_request.tags,
            reserve_ip=data.desktop_request.reserve_ip,
        )
        print("created desktop")

    else:
        raise HTTPException(
            status_code=400, detail="desktop or desktop_runtime is required"
        )

    print("finding agent runtime...")
    agent_runtimes = AgentRuntime.find(name=data.runtime, owner_id=current_user.email)
    if not agent_runtimes:
        raise HTTPException(status_code=404, detail="AgentRuntime not found")
    agent_runtime = agent_runtimes[0]

    print("getting api key for agent...")
    hub_url = os.getenv("AGENTSEA_HUB_URL", "https://hub.agentsea.ai")
    hub_key_url = f"{hub_url}/v1/users/me/keys"
    headers = {"Authorization": f"Bearer {current_user.token}"}
    response = requests.get(hub_key_url, headers=headers)
    response.raise_for_status()  # Raises an exception for 4XX or 5XX errors
    key_data = response.json()
    key = key_data["key"]
    data.secrets[HUB_API_KEY_ENV] = key

    print("creating agent...")

    instance = agent_runtime.run(
        name=data.name,
        type=data.type,
        desktop=desktop_vm.name,
        envs=data.envs,
        secrets=data.secrets,
        metadata=data.metadata,
        wait_ready=data.wait_ready,
        icon=data.icon,
    )
    print("created agent")

    return instance.to_schema()


@app.get("/v1/agents", response_model=AgentsModel)
async def get_agents(current_user: Annotated[V1UserProfile, Depends(get_current_user)]):
    agents = TaskAgentInstance.find(owner_id=current_user.email)
    return AgentsModel(agents=[agent.to_schema() for agent in agents])


@app.get("/v1/agents/{name}", response_model=AgentModel)
async def get_agent(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    agent: List[TaskAgentInstance] = TaskAgentInstance.find(
        name=name, owner_id=current_user.email
    )
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent[0].to_schema()


@app.delete("/v1/agents/{name}")
async def delete_agent(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    TaskAgentInstance.delete(name=name, owner_id=current_user.email)


# ---


@app.post("/v1/agenttypes", response_model=AgentTypeModel)
async def create_types(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: CreateAgentTypeModel,
):
    agent = AgentType(
        name=data.name,
        owner_id=current_user.email,
        description=data.description,
        image=data.image,
        env_opts=data.env_opts,
        supported_runtimes=data.supported_runtimes,
        public=data.public,
    )
    return agent.to_schema()


@app.get("/v1/agenttypes", response_model=AgentTypesModel)
async def get_types(current_user: Annotated[V1UserProfile, Depends(get_current_user)]):
    user_types = AgentType.find(owner_id=current_user.email)

    public_types = [
        agent
        for agent in AgentType.find(public=True)
        if agent.id not in [user_agent.id for user_agent in user_types]
    ]
    types = user_types + public_types
    return AgentTypesModel(types=[agent.to_schema() for agent in types])


@app.get("/v1/agenttypes/{name}", response_model=AgentTypeModel)
async def get_type(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    agents = AgentType.find(name=name, owner_id=current_user.email)

    if not agents:
        agents = AgentType.find(name=name, public=True)
        if not agents:
            raise HTTPException(status_code=404, detail="Agent type not found")

    return agents[0].to_schema()


@app.delete("/v1/agenttypes/{name}")
async def delete_type(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], name: str
):
    AgentType.delete(name=name, owner_id=current_user.email)


# ---


@app.post("/v1/tasks", response_model=TaskModel)
async def create_task(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: TaskCreateModel,
):
    task = Task(
        owner_id=current_user.email,
        description=data.description,
        url=data.url,
        status="created",
        created=time.time(),
        started=0.0,
        completed=0.0,
        error="",
        output="",
    )
    return task.to_schema()


@app.put("/v1/tasks/{task_id}", response_model=TaskModel)
def update_task(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    task_id: str,
    data: TaskUpdateModel,
):
    # Fetch the task by ID and owner ID to ensure the current user owns the task
    task = Task.find(id=task_id, owner_id=current_user.email)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task = task[0]

    # Update the task with the provided data
    update_data = data.model_dump(exclude_none=True)
    task.update(**update_data)

    return task.to_schema()


@app.get("/v1/tasks", response_model=TasksModel)
async def get_tasks(current_user: Annotated[V1UserProfile, Depends(get_current_user)]):
    tasks = Task.find(owner_id=current_user.email)
    return TasksModel(tasks=[task.to_schema() for task in tasks])


@app.get("/v1/tasks/{task_id}", response_model=TaskModel)
async def get_task(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], task_id: str
):
    task = Task.find(id=task_id, owner_id=current_user.email)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task[0].to_schema()


@app.delete("/v1/tasks/{task_id}")
async def delete_task(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)], task_id: str
):
    Task.delete(id=task_id, owner_id=current_user.email)
    return {"message": "Task deleted successfully"}


@app.put("/v1/tasks/{task_id}", response_model=TaskModel)
async def update_task(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    data: TaskUpdateModel,
):
    task = Task.find(id=data.id, owner_id=current_user.email)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = task[0]
    if data.description:
        task.description = data.description
    if data.status:
        task.status = data.status
    task.save()
    return task.to_schema()


@app.post("/v1/tasks/{task_id}/msg", response_model=TaskModel)
async def post_task_msg(
    current_user: Annotated[V1UserProfile, Depends(get_current_user)],
    task_id: str,
    data: PostMessageModel,
):
    task = Task.find(id=task_id, owner_id=current_user.email)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = task[0]
    task.post_message(data.role, data.msg, data.images)
    return task.to_schema()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8088)
