import gpt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def prompt_learning_resources(plan):
    """Prompt user for learning resources details"""
    prompt = f"""
    
    Role: you are a technical executor working with a project manager. 

    Task: You will create a list of learning resources for the project plan. Don't include links to websites just the names of useful youtube channels, wikipedia pages, and books that will help the team learn the skills they need to complete the project.
    
    Here is the learning plan you will use and add resources to at the bottom: 

    {plan}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Learning resources prompt generated")
    return prompt


def prompt_deliverables(project_plan):
    """Prompt user for project deliverables details"""
    prompt = f"""
    
    Role: you are a certified project manager. 

    Task: You will create a list of deliverables for this project, based on the project plan. provided here:

    {project_plan}

    Content: You will write a list of deliverables for a project. 

    Style: Use Markdown to format the document.

     I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Deliverables prompt generated")
    return prompt


def prompt_writing_critic(text):
    """Prompt user for writing critic details"""
    prompt = f"""
    
    Role: you are a writing critic. 

    Task: You will rewrite the following text to make it very professional and easy to understand.:
    {text}

    I don't want your thoughts, just the revised text in it's entirety with your improvements.

    """
    logger.info("writing critic prompt generated")
    return prompt


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

    You can make some logical assumptions about the project based on the information I provide you.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Executive summary prompt generated")
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

     I don't want your thoughts, just the revised text with your improvements.

   
    """
    logger.info("Planning prompt generated")
    return prompt


def prompt_tickets(existing_plan):
    """Prompt user for project tickets"""

    prompt = f"""
    
    Role: you need to be a technical executor working with a project manager. You need to take the project plan and create detailed tasks for Jira tickets.

    Your Task: Create Jira tickets for the project plan. Estimate the time and resources (human and otherwise) required for each task. 
   

    Here is the plan: {existing_plan}

    Style: Use Markdown to format the document.

    Use your skills and impress me with how you create clear and concise tasks

     I don't want your thoughts, just the revised text.

    """
    logger.info("Jira tickets prompt generated")
    return prompt
