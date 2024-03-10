from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rich.console import Console
from typing import List
import os

from guisurfer.agent.models import SolveTaskModel

from .agent import DinOCR
from .tool import SemanticDesktop

HUB_SERVER = os.environ.get("SURF_HUB_SERVER", "https://surf.agentlabs.xyz")
AGENTD_ADDR = os.environ.get("AGENTD_ADDR")
if not AGENTD_ADDR:
    raise Exception("$AGENTD_ADDR not set")
AGENTD_PRIVATE_SSH_KEY = os.environ.get("AGENTD_PRIVATE_SSH_KEY")
if not AGENTD_PRIVATE_SSH_KEY:
    raise Exception("$AGENTD_PRIVATE_SSH_KEY not set")

app = FastAPI()

console = Console()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.post("/task", response_model=SolveTaskModel)
async def solve_task(task: SolveTaskModel):

    desktop: SemanticDesktop = SemanticDesktop(
        agentd_url=AGENTD_ADDR, requires_proxy=True
    )
    desktop._add_session_data("task", task.task.description)

    console.print("running agent loop...", style="green")
    agent = DinOCR()
    task = Task()
    result = agent.solve_task(task, desktop, task.max_steps, args.site)
