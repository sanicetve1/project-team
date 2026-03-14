# Projectteam Crew

Welcome to the Projectteam Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
cd projectteam
uv sync
```

This creates a virtual environment and installs all required packages (including CrewAI). You can then run the crew with the CrewAI CLI via uv.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/projectteam/config/agents.yaml` to define your agents
- Modify `src/projectteam/config/tasks.yaml` to define your tasks
- Modify `src/projectteam/crew.py` to add your own logic, tools and specific args
- Modify `src/projectteam/main.py` to add custom inputs for your agents and tasks

## Running the Project

From the project root (`projectteam/`), run:

```bash
uv run crewai run
```

This uses the project’s uv-managed environment and runs the CrewAI CLI, which initializes the ProjectTeam Crew and runs the PM, Architect, and Product Owner agents. Outputs are written to `output/product_requirements.md`, `output/architecture.md`, and `output/project_plan.md` (relative to the repo root that contains the `Templates` folder).

## Understanding Your Crew

The ProjectTeam Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Projectteam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
