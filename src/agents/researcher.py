from src.retrieval.retriever import retrieve_documents, format_docs_for_prompt
from src.utils.llm import get_llm


RESEARCHER_PROMPT = """
You are the Researcher Agent for a Product Intelligence system.

Your task:
- Retrieve and analyze relevant customer, product, support, roadmap, and competitor evidence.
- Identify patterns, recurring pain points, and business impact.
- Ground every insight in the provided sources.
- Do not invent facts.

User query:
{query}

Conversation history:
{chat_history}

Retrieved evidence:
{evidence}

Return:
1. Key findings
2. Evidence references
3. Important uncertainties
"""


def researcher_node(state):
    query = state["query"]
    chat_history = "\n".join(state.get("chat_history", []))

    docs = retrieve_documents(query)

    evidence = format_docs_for_prompt(docs)

    llm = get_llm(temperature=0.1)

    response = llm.invoke(
        RESEARCHER_PROMPT.format(
            query=query,
            chat_history=chat_history,
            evidence=evidence,
        )
    )

    return {
        **state,
        "retrieved_docs": docs,
        "research_notes": response.content,
    }
