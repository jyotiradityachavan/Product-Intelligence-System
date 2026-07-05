from langgraph.graph import StateGraph, END

from src.graph.state import ProductIntelligenceState
from src.agents.researcher import researcher_node
from src.agents.critic import critic_node
from src.agents.summarizer import summarizer_node
from src.agents.recommender import recommender_node
from src.agents.supervisor import supervisor_router


def build_graph():
    workflow = StateGraph(ProductIntelligenceState)

    workflow.add_node("researcher", researcher_node)
    workflow.add_node("critic", critic_node)
    workflow.add_node("summarizer", summarizer_node)
    workflow.add_node("recommender", recommender_node)

    workflow.set_entry_point("researcher")

    workflow.add_edge("researcher", "critic")

    workflow.add_conditional_edges(
        "critic",
        supervisor_router,
        {
            "researcher": "researcher",
            "summarizer": "summarizer",
        },
    )

    workflow.add_edge("summarizer", "recommender")
    workflow.add_edge("recommender", END)

    return workflow.compile()


def run_product_intelligence_graph(query: str, chat_history: list[str] | None = None):
    app = build_graph()

    initial_state = {
        "query": query,
        "chat_history": chat_history or [],
        "retrieved_docs": [],
        "research_notes": "",
        "validation_notes": "",
        "summary": "",
        "recommendations": "",
        "final_answer": "",
        "report": "",
    }

    return app.invoke(initial_state)
