from typing import List, TypedDict

from langchain.schema import Document


class ProductIntelligenceState(TypedDict):
    query: str
    chat_history: List[str]

    retrieved_docs: List[Document]
    research_notes: str
    validation_notes: str
    summary: str
    recommendations: str

    final_answer: str
    report: str
