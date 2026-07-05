from langchain_groq import ChatGroq

from src.utils.config import settings


def get_llm(temperature: float = 0.2):
    if not settings.GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. Create a .env file using .env.example."
        )

    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name=settings.LLM_MODEL,
        temperature=temperature,
    )
