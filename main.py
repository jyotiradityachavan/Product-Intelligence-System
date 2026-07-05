from src.graph.workflow import run_product_intelligence_graph
from src.utils.report_writer import create_markdown_report, save_report


def main():
    query = "What product areas should we prioritize next quarter and why?"

    result = run_product_intelligence_graph(query)

    print(result["final_answer"])

    report = create_markdown_report(
        query=query,
        final_answer=result["final_answer"],
        research_notes=result["research_notes"],
        validation_notes=result["validation_notes"],
        recommendations=result["recommendations"],
    )

    path = save_report(report)

    print(f"\nReport saved to: {path}")


if __name__ == "__main__":
    main()
