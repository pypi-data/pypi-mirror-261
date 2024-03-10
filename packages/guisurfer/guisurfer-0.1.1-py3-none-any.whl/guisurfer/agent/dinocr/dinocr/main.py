import argparse
import logging

from rich.console import Console
from agentdesk.vm.gce import GCEProvider

from .agent import DinOCR
from .tool import SemanticDesktop


console = Console()

parser = argparse.ArgumentParser(description="Run the agent with optional debug mode.")
parser.add_argument(
    "--debug",
    action="store_true",
    help="Enable debug mode for more verbose output.",
    default=False,
)
parser.add_argument(
    "--task",
    type=str,
    help="Specify the task to run.",
    required=True,
)
parser.add_argument(
    "--max_steps",
    type=int,
    help="Max steps the agent can take",
    default=10,
)
parser.add_argument(
    "--site",
    type=str,
    help="Max steps the agent can take",
    default=None,
)
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

console.print(
    f"solving task '{args.task}' on site '{args.site}' with max steps {args.max_steps}",
    style="green",
)

# Find or create a local desktop with the simplified action space
provider = GCEProvider(project_id="agentsea-dev")
desktop: SemanticDesktop = SemanticDesktop.ensure("gpt4v-demo1", provider=provider)
desktop._add_session_data("task", args.task)

# View the desktop, we'll run in the background so it doesn't block
desktop.view(background=True)

# Call our simple agent to solve the task
console.print("running agent loop...", style="green")
agent = DinOCR()
result = agent.solve_task(args.task, desktop, args.max_steps, args.site)
