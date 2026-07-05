from src.utils.llm import get_llm


CRITIC_PROMPT = """
You are the Critic and Validator Agent.

Your job:
- Check whether the research notes are supported by evidence.
- Flag unsupported claims.
- Identify missing context.
- Suggest what should be treated as uncertain.
- Keep the response concise and rigorous.

User query:
{query}

Research notes:
{research_notes}

Return:
1. Supported claims
2. Unsupported or weak claims
3. Missing evidence
4. Confidence level: Low, Medium, or High
"""


def critic_node(state):
    llm = get_llm(temperature=0.0)

    response = llm.invoke(
        CRITIC_PROMPT.format(
            query=state["query"],
            research_notes=state["research_notes"],
        )
    )

    return {
        **state,
        "validation_notes": response.content,
    }
