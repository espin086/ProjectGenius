import argparse
import logging

# Project Genius Modules
import prompts
import gpt


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generative AI Project Planning Tool")
    parser.add_argument("--create", help="Create a new project plan")
    parser.add_argument("--view", help="View existing project plans")
    parser.add_argument("--update", help="Update a project plan")
    parser.add_argument("--delete", help="Delete a project plan")

    args = parser.parse_args()

    if args.create:
        logger.info(" Creating a project plan for: %s", args.create)
        logger.info("************** STEP 1: Project Overview **************")
        goals = input("Specific Goals?: ")
        kpis = input("Measurable?: ")
        achieveable = input("Achievable?: ")
        relevance = input("Relevance?: ")
        time_bound = input("Time Bound?: ")
        prompt_overview = prompts.prompt_overview(
            args.create, goals, kpis, achieveable, relevance, time_bound
        )
        text_overview = gpt.text_generation(prompt_overview)
        logger.info("************** STEP 2: Creating the Project Plan **************")
        schedule = input("Your Schedule?: ")
        resources = input("Resources?: ")
        budget = input("Budget?: ")
        prompt_plan = prompts.prompt_plan(text_overview, schedule, resources, budget)
        text_plan = gpt.text_generation(prompt_plan)

        prompt_tickets = prompts.prompt_tickets(text_overview + text_plan)
        text_tickets = gpt.text_generation(prompt_tickets)

        print(text_overview)
        print(text_plan)
        print(text_tickets)

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
