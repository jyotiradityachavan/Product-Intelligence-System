from src.utils.llm import get_llm


SUMMARIZER_PROMPT = """
You are the Summarizer Agent.

Create a clear, executive-friendly answer.

Use:
- The user query
- Research notes
- Validation notes

Requirements:
- Explain the main insight first.
- Include evidence-backed reasoning.
- Mention uncertainty where relevant.
- Keep it useful for a product leader.

User query:
{query}

Research notes:
{research_notes}

Validation notes:
{validation_notes}

Return a structured summary.
"""


def summarizer_node(state):
    llm = get_llm(temperature=0.2)

    response = llm.invoke(
        SUMMARIZER_PROMPT.format(
            query=state["query"],
            research_notes=state["research_notes"],
            validation_notes=state["validation_notes"],
        )
    )

    return {
        **state,
        "summary": response.content,
    }
