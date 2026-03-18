from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import Dict, Any, List
import os
from crewai_tools import SerperDevTool, FileReadTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Projectteam():
    """Projectteam crew"""

    agents_config: Dict[str, Dict[str, Any]]
    tasks_config: Dict[str, Dict[str, Any]]
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def business_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst_agent'], # type: ignore[index]
            name='Business Analyst',
            verbose=True
        )

    @agent
    def architect_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['architect_agent'], # type: ignore[index]
            name='Architect',
            verbose=True,
            tools=tools,
        )

    @agent
    def architect_reviewer_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['architect_reviewer_agent'], # type: ignore[index]
            name='Architect Reviewer',
            verbose=True,
            tools=tools,
        )

    @agent
    def PM_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['PM_agent'], # type: ignore[index]
            name='Project Manager',
            verbose=True,
            tools=[
                FileReadTool(),
            ],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task'], # type: ignore[index]
            name='Business Analyst Task',
        )

    @task
    def architect_task(self) -> Task:
        return Task(
            config=self.tasks_config['architect_task'], # type: ignore[index]
        )

    @task
    def architect_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['architect_review_task'], # type: ignore[index]
        )

    @task
    def project_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_plan_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Projectteam crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
