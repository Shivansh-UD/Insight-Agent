from agents.planner import generate_plan
from agents.writer import write_report
from tools.search_tools import search_topic

def run_research(topic):

    print("\nGenerating Research Plan...\n")
    plan = generate_plan(topic)
    print(plan)

    print("\nCollecting Research Findings...\n")

    findings = ""

    subtopics = plan.split("\n")

    for sub in subtopics:
        if sub.strip() != "":
            print(f"Researching: {sub}")
            result = search_topic(sub)
            findings += f"\n{sub}\n{result}\n"

    print("\nWriting Final Report...\n")
    report = write_report(topic, findings)  # Writer now uses collected research, not hallucination.

    return report