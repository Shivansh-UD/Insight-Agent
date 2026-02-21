from agents.orchestrator import run_research

if __name__ == "__main__":

    topic = input("Enter research topic: ")

    final_report = run_research(topic)

    print("\n===== FINAL REPORT =====\n")
    print(final_report)