#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from pathlib import Path

from projectteam.crew import Projectteam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

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

repo_root = _find_repo_root(Path(__file__).parent)
templates_dir = repo_root / "Templates"

def run():
    """
    run the projectteam crew
    """
    inputs = {
        #"project_idea": "We want to build a Smart Gym Capacity & Booking Platform that allows gym members to book gym entry slots, reserve equipment, and join classes while preventing overcrowding. Gym managers should be able to control capacity limits and view analytics. The system must support multiple gyms and real-time updates for availability.",
        "project_idea": "We want to build an AI Travel Planning Assistant that can plan trips end-to-end.The system should:- understand travel goals- search flights - search hotels - generate itineraries - estimate travel cost - allow the user to refine plans.",
        "current_year": str(datetime.now().year),
        "version": "1.0",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "product_requirements_template": _read_text(templates_dir / "product_requirements.md-template"),
        "architecture_template": _read_text(templates_dir / "Architecture.md-template"),
        "phase_plan_template": _read_text(templates_dir / "phase-plan.md-template"), 
            }
    projectteam = Projectteam()
    crew = projectteam.crew()
    result = crew.kickoff(inputs)
    print(result.raw)

if __name__ == "__main__":
    run()