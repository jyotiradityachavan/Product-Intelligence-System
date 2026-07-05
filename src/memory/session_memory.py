from typing import Dict, List


class SessionMemory:
    """
    Simple in-memory session store for MVP.

    For production:
    - Use LangGraph checkpointing
    - Store sessions in Redis/Postgres
    - Add summary memory for long conversations
    """

    def __init__(self):
        self.sessions: Dict[str, List[str]] = {}

    def get_history(self, session_id: str) -> List[str]:
        return self.sessions.get(session_id, [])

    def add_turn(self, session_id: str, user_message: str, assistant_message: str):
        history = self.sessions.setdefault(session_id, [])
        history.append(f"User: {user_message}")
        history.append(f"Assistant: {assistant_message}")

    def clear(self, session_id: str):
        self.sessions[session_id] = []
