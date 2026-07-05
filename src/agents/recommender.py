from src.utils.llm import get_llm


RECOMMENDER_PROMPT = """
You are the Recommender Agent.

Based on the summary and validation notes, produce actionable product recommendations.

Prioritize by:
- Customer impact
- Revenue or retention risk
- Technical feasibility
- Strategic differentiation

User query:
{query}

Summary:
{summary}

Validation notes:
{validation_notes}

Return:
1. Recommended priorities
2. Rationale
3. Risks and trade-offs
4. Suggested next steps
"""


def recommender_node(state):
    llm = get_llm(temperature=0.25)

    response = llm.invoke(
        RECOMMENDER_PROMPT.format(
            query=state["query"],
            summary=state["summary"],
            validation_notes=state["validation_notes"],
        )
    )

    final_answer = f"""
## Answer

{state["summary"]}

## Recommendations

{response.content}
""".strip()

    return {
        **state,
        "recommendations": response.content,
        "final_answer": final_answer,
    }
