import gpt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def prompt_test_designer(input_text):
    """Prompt user for test design details"""
    prompt = f"""
    
    Role: you are a marketing scientist you have expertise in designing a/b tests, brand lift tests, conversion tests, and other marketing experiments.

    Task: You need to describe an experiment and test design you will need to run.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document. You will need to have the following sections: background, opportunity, solution, how test meets our values, primary hypothesis, secondary hypothesis, and KPIs

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Test designer prompt generated")
    return prompt


def prompt_kpis(input_text):
    """Prompt user for KPI details"""
    prompt = f"""
    
    Role: you are a marketing scientist and lead analyst. 

    Task: You will take the KPIs provided and expand on them also making sure to include counter KPIs

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document. You will need to have the following sections: background, opportunity, solution, how test meets our values, primary hypothesis, secondary hypothesis, and KPIs

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("KPI prompt generated")
    return prompt


def prompt_create_test_plan(input_text):
    """Prompt user for summary details"""
    prompt = f"""
    
    Role: you are a manager of marketing experimentation and analysis. 

    Task: You will review a proposal for a test plan and rewrite it to make it very professional and easy to understand.
    You will find any inconsistencies and remove, incorporate, or rewrite them.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document. You will need to have the following sections: background, opportunity, solution, how test meets our values, primary hypothesis, secondary hypothesis, and KPIs

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Marketing plan prompt generated")
    return prompt


def prompt_summary(input_text):
    """Prompt user for summary details"""
    prompt = f"""
    
    Role: YOu are an excellent summarizer of information. You balance the need for detail with the need for brevity. 

    Task: YOu will expand on the following text and summarize it in a way that is easy to understand and follow.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Summary prompt generated")
    return prompt


def prompt_values(input_text):
    """Prompt user for value statement details"""
    prompt = f"""
    
    Role: you are an expert on how to connect tasks with value statements. 

    Context: Our corporate values are community leadership, continuous innovation, and our vision of to facilitate the financial security of its members, associates, and their families through the provision of a full range of highly competitive financial products and services; in so doing, USAA seeks to be the provider of choice for the military community.

    Task: You will read the text I provide you and see how you can connect my goals to the company's values and mission.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Value statement prompt generated")
    return prompt


def prompt_solution(input_text):
    """Prompt user for solution details"""
    prompt = f"""
    
    Role: you specialize in drafting solutions to busienss problems. You are given some text and can orgnize, summarize, and expand on the solutions provided.

    Task: Your task will be to prioritize and expand on solutions based on input I give you.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Solution prompt generated")
    return prompt


def prompt_opportunity(input_text):
    """Prompt user for opportunity details"""
    prompt = f"""
    
    Role: you are a Marketing scientist and Lead Analyst and you need to write a test plan. 

    Task: You will need to expand and summarize the following opportunity in terms of business impact and context.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Opportunity prompt generated")
    return prompt


def prompt_background(input_text):
    """Prompt user for background details"""
    prompt = f"""
    
    Role: you are a Marketing scientist and Lead Analyst and you need to write a test plan. 

    Task: You will take my summary I am going to give and you will rewrite it to make it very professional and easy to understand.

    Here is the input you need to summarize and expand on: {input_text}

    Style: Use Markdown to format the document.

    I don't want your thoughts, just the revised text with your improvements.

    """
    logger.info("Background prompt generated")
    return prompt


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
    
    Role: you are a writing critic and expert write of corporate documents and reports.

    Task: You will rewrite the following text to make it very professional and easy to understand. You will reorder concepts where they make most sense and remove any inconsistencies. Keep all of the main sections of the document intact:
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
