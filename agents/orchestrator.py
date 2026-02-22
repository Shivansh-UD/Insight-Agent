from agents.planner import generate_plan
from agents.writer import write_report
from tools.search_tools import search_topic
from rag.vector_store import add_documents, retrieve
from utils.pdf_generator import generate_pdf
import datetime


def run_research(topic):

    print("\nGenerating Research Plan...\n")
    plan = generate_plan(topic)

    print("\nCollecting Research Findings...\n")

    findings_list = []
    subtopics = plan.split("\n")

    for sub in subtopics:
        if sub.strip() != "":
            print(f"Researching: {sub}")
            result = search_topic(sub)
            findings_list.append(result)

    # Add to vector memory
    add_documents(findings_list)

    print("\nRetrieving Relevant Context...\n")
    retrieved_docs = retrieve(topic)

    combined_context = "\n".join(retrieved_docs)

    print("\nWriting Final Report...\n")
    report = write_report(topic, combined_context)

    # Generate PDF
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.pdf"

    generate_pdf(report, filename)

    print(f"\nResearch complete. Saved as: {filename}\n")

    print("\nResearch complete. PDF generated successfully.\n")