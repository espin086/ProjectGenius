import gpt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def prompt_overview(name, goals, kpis, achieveable, relevance, time_bound):
    """Prompt user for project overview details"""

    prompt = f"""

    Role: you are a certified project manager. 

    Task: You will create a project overview given the following details:
    0. Project Name: {name}
    1. Specific Goals: {goals}
    2. Measurable: {kpis}
    3. Achievable: {achieveable}
    4. Relevance: {relevance}
    5. Time Bound: {time_bound}

    Content: You will write the project plan in a way that is easy to understand and follow. 

    Style: I need the following sections: Introduction, Goals, Scope, and Stakeholders. Use Markdown to format the document.

    You can make some logical assumptions about the project based on the information I provide you

    """
    logger.info("Prompt Overview: %s", prompt)
    return prompt


def prompt_plan(overview, schedule, resources, budget):
    """Prompt user for project plan details"""
    prompt = f"""

    Role: you are a certified project manager. 

    Project Overview: {overview}

    Schedule: {schedule}

    Resources: {resources}

    Budget: {budget}

    Your Task: Write a project plan that includes the following sections: Work Breakdown Structure, Weekly Schedule, Resource Allocation, and Budget.

    Style: Use Markdown to format the document.

    Remember to make logical assumptions about the project based on the information I provide you. Use your skills and impress me.
   
    """
    logger.info("Prompt Overview: %s", prompt)
    return prompt


def prompt_tickets(plan):
    """Prompt user for project tickets"""

    prompt = """
    
    Role: you need to be a technical executor working with a project manager. You need to take the project plan and create detailed task for Jira tickets.

    Your Task: Create Jira tickets for the project plan. Estimate the time and resources (human and otherwise) required for each task. Organize the tasks by features, stories, and tasks.

    Here is the plan: {plan}

    Style: Use Markdown to format the document.

    Remember to make organize your response into features, stories, and tasks. Use your skills and impress me.
    """
    logger.info("Prompt Tickets: %s", prompt)
    return prompt
