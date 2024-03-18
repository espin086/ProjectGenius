import argparse
import logging

# Project Genius Modules
import prompts
import gpt


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def inputs_overview():
    goals = input("Q1 of 8: Specific Goals?: ")
    kpis = input("Q2 of 8:Measurable?: ")
    achieveable = input("Q3 of 8:Achievable?: ")
    relevance = input("Q4 of 8:Relevance?: ")
    time_bound = input("Q5 of 8:Time Bound?: ")
    schedule = input("Q6 of 8:Your Schedule?: ")
    resources = input("Q7 of 8:Resources?: ")
    budget = input("Q8 of 8:Budget?: ")
    return goals, kpis, achieveable, relevance, time_bound, schedule, resources, budget


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generative AI Project Planning Tool")
    parser.add_argument("--create", help="Create a new project plan")
    parser.add_argument("--view", help="View existing project plans")
    parser.add_argument("--update", help="Update a project plan")
    parser.add_argument("--delete", help="Delete a project plan")

    args = parser.parse_args()

    if args.create:
        logger.info(" Creating a project plan for: %s", args.create)
        logger.info("************** STEP 1: Collect Input **************")
        goals, kpis, achieveable, relevance, time_bound, schedule, resources, budget = (
            inputs_overview()
        )
        prompt_overview = prompts.prompt_overview(
            args.create, goals, kpis, achieveable, relevance, time_bound
        )
        text_overview = gpt.text_generation(prompt_overview)

        prompt_plan = prompts.prompt_plan(text_overview, schedule, resources, budget)
        text_plan = gpt.text_generation(prompt_plan)

        prompt_tickets = prompts.prompt_tickets(text_overview + text_plan)
        text_tickets = gpt.text_generation(prompt_tickets)

        text_all = text_overview + text_plan + text_tickets

        prompt_text_all = prompts.prompt_writing_critic(text_all)
        text_all = gpt.text_generation(prompt_text_all)

        prompt_deliverables = prompts.prompt_deliverables(text_all)
        text_deliverables = gpt.text_generation(prompt_deliverables)

        prompt_learning_resources = prompts.prompt_learning_resources(text_all)
        text_learnings_resources = gpt.text_generation(prompt_learning_resources)

        text_all = text_all + text_deliverables + text_learnings_resources

        prompt_final = prompts.prompt_writing_critic(text_all)
        text_final = gpt.text_generation(prompt_final)

        logger.info(text_final)

    elif args.view:
        print("Viewing existing project plans...")
    elif args.update:
        print("Updating a project plan...")
    elif args.delete:
        print("Deleting a project plan...")
    else:
        print(
            "PROJECT GENIUS: Welcome to the Generative AI Project Planning Tool. Please use --help for available options."
        )
