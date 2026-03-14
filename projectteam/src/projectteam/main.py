#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from pathlib import Path

from projectteam.crew import Projectteam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def _find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for _ in range(10):
        if (current / "Templates").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
    raise FileNotFoundError("Could not locate repo root containing 'Templates' directory")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run():
    """
    Run the crew.
    """
    repo_root = _find_repo_root(Path(__file__).parent)
    templates_dir = repo_root / "Templates"

    inputs = {
        "project_idea": "build a web application to create a calculator",
        "project_name": "Calculator Web App",
        "current_year": str(datetime.now().year),
        "version": "1.0",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "product_requirements_template": _read_text(templates_dir / "product_requirements.md-template"),
        "architecture_template": _read_text(templates_dir / "Architecture.md-template"),
        "phase_plan_template": _read_text(templates_dir / "phase-plan.md-template"),
    }

    try:
        Projectteam().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "project_idea": "build a web application to create a calculator",
        "project_name": "Calculator Web App",
        "current_year": str(datetime.now().year),
        "version": "1.0",
    }
    # Templates are required for the YAML task interpolation.
    repo_root = _find_repo_root(Path(__file__).parent)
    templates_dir = repo_root / "Templates"
    inputs["product_requirements_template"] = _read_text(templates_dir / "product_requirements.md-template")
    inputs["architecture_template"] = _read_text(templates_dir / "Architecture.md-template")
    inputs["phase_plan_template"] = _read_text(templates_dir / "phase-plan.md-template")
    inputs["date"] = datetime.now().strftime("%Y-%m-%d")
    try:
        Projectteam().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Projectteam().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "project_idea": "build a web application to create a calculator",
        "project_name": "Calculator Web App",
        "current_year": str(datetime.now().year),
        "version": "1.0",
    }
    # Templates are required for the YAML task interpolation.
    repo_root = _find_repo_root(Path(__file__).parent)
    templates_dir = repo_root / "Templates"
    inputs["product_requirements_template"] = _read_text(templates_dir / "product_requirements.md-template")
    inputs["architecture_template"] = _read_text(templates_dir / "Architecture.md-template")
    inputs["phase_plan_template"] = _read_text(templates_dir / "phase-plan.md-template")
    inputs["date"] = datetime.now().strftime("%Y-%m-%d")

    try:
        Projectteam().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    repo_root = _find_repo_root(Path(__file__).parent)
    templates_dir = repo_root / "Templates"

    # Trigger payload can include: project_idea, project_name. Defaults provided if missing.
    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "project_idea": trigger_payload.get("project_idea", "build a web application to create a calculator"),
        "project_name": trigger_payload.get("project_name", "Calculator Web App"),
        "current_year": str(datetime.now().year),
        "version": trigger_payload.get("version", "1.0"),
        "product_requirements_template": _read_text(templates_dir / "product_requirements.md-template"),
        "architecture_template": _read_text(templates_dir / "Architecture.md-template"),
        "phase_plan_template": _read_text(templates_dir / "phase-plan.md-template"),
        "date": datetime.now().strftime("%Y-%m-%d"),
    }

    try:
        result = Projectteam().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
