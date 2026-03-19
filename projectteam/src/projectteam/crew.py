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
    def application_architect_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['application_architect_agent'], # type: ignore[index]
            name='Application Architect',
            verbose=True,
            tools=tools,
        )

    @agent
    def data_architect_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['data_architect_agent'], # type: ignore[index]
            name='Data Architect',
            verbose=True,
            tools=tools,
        )

    @agent
    def infra_architect_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['infra_architect_agent'], # type: ignore[index]
            name='Infrastructure Architect',
            verbose=True,
            tools=tools,
        )

    @agent
    def security_architect_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['security_architect_agent'], # type: ignore[index]
            name='Security Architect',
            verbose=True,
            tools=tools,
        )

    @agent
    def architecture_assembler_agent(self) -> Agent:
        tools = [FileReadTool()]
        if os.getenv("SERPER_API_KEY"):
            tools.append(SerperDevTool())
        return Agent(
            config=self.agents_config['architecture_assembler_agent'], # type: ignore[index]
            name='Architecture Assembler',
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
    def application_architect_spec_task(self) -> Task:
        return Task(
            config=self.tasks_config['application_architect_spec_task'], # type: ignore[index]
        )

    @task
    def data_architect_spec_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_architect_spec_task'], # type: ignore[index]
        )

    @task
    def infra_architect_spec_task(self) -> Task:
        return Task(
            config=self.tasks_config['infra_architect_spec_task'], # type: ignore[index]
        )

    @task
    def security_architect_spec_task(self) -> Task:
        return Task(
            config=self.tasks_config['security_architect_spec_task'], # type: ignore[index]
        )

    @task
    def architecture_assembler_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_assembler_task'], # type: ignore[index]
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
