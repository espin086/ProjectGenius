import argparse
import logging


# Project Genius Modules
import prompts
import gpt


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def inputs_test():
    background = input("Q: background?: ")
    opportunity = input("Q: describe opportunity?: ")
    solution = input("Q: describe solution?: ")
    value_statement = input("Q: value statement?: ")
    primary_hypothesis = input("Q: primary hypothesis?: ")
    secondary_hypothesis = input("Q: secondary hypothesis?: ")
    kpis = input("Q: kpis?: ")
    return (
        background,
        opportunity,
        solution,
        value_statement,
        primary_hypothesis,
        secondary_hypothesis,
        kpis,
    )


def inputs_master():
    goals = input("Q1 of 8: Specific Goals?: ")
    kpis = input("Q2 of 8:Measurable?: ")
    achieveable = input("Q3 of 8:Achievable?: ")
    relevance = input("Q4 of 8:Relevance?: ")
    time_bound = input("Q5 of 8:Time Bound?: ")
    schedule = input("Q6 of 8:Your Schedule?: ")
    resources = input("Q7 of 8:Resources?: ")
    budget = input("Q8 of 8:Budget?: ")
    return goals, kpis, achieveable, relevance, time_bound, schedule, resources, budget


def main_master():
    logger.info(" Creating a project plan for: %s", args.master)
    logger.info("************** STEP 1: Collect Input **************")
    goals, kpis, achieveable, relevance, time_bound, schedule, resources, budget = (
        inputs_master()
    )
    prompt_overview = prompts.prompt_overview(
        args.master, goals, kpis, achieveable, relevance, time_bound
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

    logger.info("Completed Project Plan: %s", args.master)
    return text_final


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generative AI Project Planning Tool")
    parser.add_argument("--master", help="Create a master project plan")
    parser.add_argument("--test", help="Create a plan for experimentation")
    parser.add_argument("--ds", help="create a plan for data science project")
    parser.add_argument("--de", help="create a plan for data engineering project")

    args = parser.parse_args()

    if args.master:
        master_plan = main_master()
        logger.info("********** Completed Project Plan: %s **********", args.master)
        print(master_plan)

    elif args.test:
        initiative_name = args.test
        logger.info("Creating a project plan for: %s", initiative_name)
        (
            background,
            opportunity,
            solution,
            value_statement,
            primary_hypothesis,
            secondary_hypothesis,
            kpis,
        ) = inputs_test()
        logging.info("SUCCESSFULL INPUT: %s", initiative_name)

        # TODO: create prompts and generate tests
        prompt_background = prompts.prompt_background(background)
        text_background = gpt.text_generation(prompt_background)

        prompt_opportunity = prompts.prompt_opportunity(opportunity)
        text_opportunity = gpt.text_generation(prompt_opportunity)

        prompt_solution = prompts.prompt_test_designer(solution)
        text_solution = gpt.text_generation(prompt_solution)

        prompt_values = prompts.prompt_values(value_statement)
        text_values = gpt.text_generation(prompt_values)

        prompt_primary_hypothesis = prompts.prompt_summary(primary_hypothesis)
        text_primary_hypothesis = gpt.text_generation(prompt_primary_hypothesis)

        prompt_secondary_hypothesis = prompts.prompt_summary(secondary_hypothesis)
        text_secondary_hypothesis = gpt.text_generation(prompt_secondary_hypothesis)

        prompt_kpis = prompts.prompt_kpis(kpis)
        text_kpis = gpt.text_generation(prompt_kpis)

        raw_text = (
            text_background
            + text_opportunity
            + text_solution
            + text_values
            + text_primary_hypothesis
            + text_secondary_hypothesis
            + text_kpis
        )

        raw_prompt = prompts.prompt_create_test_plan(raw_text)
        text_raw = gpt.text_generation(raw_prompt)

        print(text_raw)

        # print(text_solution)

    elif args.ds:
        print("Updating a project plan...")
    elif args.de:
        print("Deleting a project plan...")
    else:
        print(
            "PROJECT GENIUS: Welcome to the Generative AI Project Planning Tool. Please use --help for available options."
        )
