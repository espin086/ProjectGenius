# ProjectGenius
A generative AI tool that helps create project plans, breaks down work, estimates level of effort, creates tasks, and so much more.


## Command Line Commands



### cli module

**How do I get help?**

Getting help for the module to see the individual commands.


**command:**

```zsh
python cli.py --help 
```

**output:**

```zsh
usage: cli.py [-h] [--master MASTER] [--test TEST] [--ds DS] [--de DE]

Generative AI Project Planning Tool

options:
  -h, --help       show this help message and exit
  --master MASTER  Create a master project plan
  --test TEST      Create a plan for experimentation
  --ds DS          create a plan for data science project
  --de DE          create a plan for data engineering project
```

**How do I create a Master Plan?**

```zsh
python cli.py --master "TITLE OF YOUR PROJECT HERE"

```

You will be asked a series of questions:

```zsh
Q1 of 8: Specific Goals?:
Q2 of 8:Measurable?:
Q3 of 8:Achievable?:
Q4 of 8:Relevance?:
Q5 of 8:Time Bound?:
Q6 of 8:Your Schedule?:
Q7 of 8:Resources?:
Q8 of 8:Budget?:
```

The program will then do the following ...

