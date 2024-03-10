from typing import List, Optional, Dict
import uuid
import time

from pydantic import BaseModel, Field
from deepthread.models import RoleThreadModel


class DesktopRuntimeModel(BaseModel):
    id: str
    name: str
    provider: str
    created: float
    updated: float
    metadata: dict = {}


class CreateDesktopRuntimeModel(BaseModel):
    name: str
    provider: str
    credentials: dict


class DesktopRuntimesModel(BaseModel):
    runtimes: List[DesktopRuntimeModel]


class AgentRuntimeModel(BaseModel):
    id: str
    name: str
    provider: str
    created: float
    updated: float
    metadata: dict = {}


class CreateAgentRuntimeModel(BaseModel):
    name: str
    provider: str
    credentials: dict


class AgentRuntimesModel(BaseModel):
    runtimes: List[AgentRuntimeModel]


class SSHKeyModel(BaseModel):
    name: str
    public_key: str
    created: float
    id: str


class SSHKeyCreateModel(BaseModel):
    name: str
    public_key: str
    private_key: str


class SSHKeysModel(BaseModel):
    keys: List[SSHKeyModel]


class TaskCreateModel(BaseModel):
    description: str
    url: Optional[str] = None


class TaskUpdateModel(BaseModel):
    id: str
    status: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None


class TaskModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    status: str
    thread: RoleThreadModel
    assigned_to: Optional[str] = None
    url: Optional[str] = None
    created: float = Field(default_factory=time.time)
    started: float = 0.0
    completed: float = 0.0
    error: str = ""
    output: str = ""


class PostMessageModel(BaseModel):
    role: str
    msg: str
    images: List[str] = []


class GCEProviderOptions(BaseModel):
    zone: str = "us-central1-a"
    region: str | None = "us-central1"


class EC2ProviderOptions(BaseModel):
    region: str | None = "us-east-1"


class CreateDesktopModel(BaseModel):
    runtime: str
    ssh_key_name: Optional[str] = None
    gce_opts: Optional[GCEProviderOptions] = None
    ec2_opts: Optional[EC2ProviderOptions] = None
    name: Optional[str] = None
    image: Optional[str] = None
    memory: int = 4
    cpu: int = 2
    disk: str = "30gb"
    tags: Optional[Dict[str, str]] = None
    reserve_ip: bool = False


class V1UserProfile(BaseModel):
    email: Optional[str] = None
    display_name: Optional[str] = None
    handle: Optional[str] = None
    picture: Optional[str] = None
    created: Optional[int] = None
    updated: Optional[int] = None


class ActionModel(BaseModel):
    name: str
    parameters: dict = {}


class ActionResponseModel(BaseModel):
    action: str
    response: str
    parameters: dict = {}


class AgentModel(BaseModel):
    id: str
    name: str
    runtime: str
    type: str
    desktop: str
    created: float
    updated: float
    metadata: dict = {}
    secrets: dict = {}
    envs: dict = {}


class AgentsModel(BaseModel):
    agents: List[AgentModel]


class CreateAgentModel(BaseModel):
    name: str
    runtime: str
    type: str
    desktop: Optional[str] = None
    desktop_request: Optional[CreateDesktopModel] = None
    metadata: dict = {}
    envs: dict = {}
    secrets: dict = {}
    wait_ready: bool = True


class EnvVarOptModel(BaseModel):
    name: str
    description: Optional[str] = None
    required: bool = False
    default: Optional[str] = None
    secret: bool = False


class CreateAgentTypeModel(BaseModel):
    id: str
    name: str
    description: str
    image: str
    env_opts: List[EnvVarOptModel] = []
    supported_runtimes: List[str] = []
    public: bool = False


class AgentTypeModel(BaseModel):
    id: str
    name: str
    description: str
    image: str
    env_opts: List[EnvVarOptModel] = []
    supported_runtimes: List[str] = []
    created: float
    updated: float
    public: bool = False


class AgentTypesModel(BaseModel):
    types: List[AgentTypeModel]
