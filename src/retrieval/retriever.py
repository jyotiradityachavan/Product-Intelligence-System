from typing import List

from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from src.utils.config import settings


def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
    )

    return Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIR,
        embedding_function=embeddings,
    )


def retrieve_documents(query: str, k: int | None = None) -> List[Document]:
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k or settings.TOP_K},
    )

    return retriever.get_relevant_documents(query)


def format_docs_for_prompt(docs: List[Document]) -> str:
    formatted = []

    for index, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        content = doc.page_content.strip()
        formatted.append(
            f"[Source {index}: {source}]\n{content}"
        )

    return "\n\n".join(formatted)
