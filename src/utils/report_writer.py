from datetime import datetime
from pathlib import Path

from src.utils.config import settings


def create_markdown_report(
    query: str,
    final_answer: str,
    research_notes: str,
    validation_notes: str,
    recommendations: str,
) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    report = f"""
# Product Intelligence Executive Report

Generated: {now}

## Business Question

{query}

## Executive Summary

{final_answer}

## Research Notes

{research_notes}

## Validation Notes

{validation_notes}

## Recommendations

{recommendations}

## Methodology

This report was generated using a multi-agent RAG workflow:

1. Researcher Agent retrieved and analyzed relevant evidence.
2. Critic Agent validated factual grounding and uncertainty.
3. Summarizer Agent produced an executive-level synthesis.
4. Recommender Agent generated prioritized product actions.
""".strip()

    return report


def save_report(markdown: str) -> str:
    Path(settings.REPORTS_DIR).mkdir(parents=True, exist_ok=True)

    filename = f"executive_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    path = Path(settings.REPORTS_DIR) / filename

    path.write_text(markdown, encoding="utf-8")

    return str(path)
