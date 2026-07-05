def supervisor_router(state):
    """
    Simple MVP supervisor.

    In a production system this could inspect state quality, confidence,
    query type, and decide whether to loop back to research.
    """

    validation = state.get("validation_notes", "").lower()

    if "confidence level: low" in validation:
        return "researcher"

    return "summarizer"
