from pathlib import Path
from typing import List

from langchain.schema import Document
from langchain_community.document_loaders import (
    CSVLoader,
    JSONLoader,
    TextLoader,
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.utils.config import settings


def load_documents(data_dir: str) -> List[Document]:
    docs: List[Document] = []
    base_path = Path(data_dir)

    for path in base_path.glob("**/*"):
        if path.is_dir():
            continue

        suffix = path.suffix.lower()

        if suffix == ".csv":
            loader = CSVLoader(file_path=str(path))
            docs.extend(loader.load())

        elif suffix == ".json":
            loader = JSONLoader(
                file_path=str(path),
                jq_schema=".[]",
                text_content=False,
            )
            docs.extend(loader.load())

        elif suffix in [".txt", ".md"]:
            loader = TextLoader(str(path), encoding="utf-8")
            docs.extend(loader.load())

    return docs


def build_vectorstore():
    docs = load_documents(settings.DATA_DIR)

    if not docs:
        raise ValueError(
            f"No documents found in {settings.DATA_DIR}. Run scripts/generate_sample_data.py first."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.CHROMA_PERSIST_DIR,
    )

    vectorstore.persist()

    return vectorstore


if __name__ == "__main__":
    build_vectorstore()
    print("Vectorstore built successfully.")
