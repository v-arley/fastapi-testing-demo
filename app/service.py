
from app.database import Database

def calculate_note_priority(title: str, content: str) -> str:
    """Lógica pura: determina prioridad sin tocar HTTP ni DB"""
    total_length = len(title) + len(content)
    if total_length > 200:
        return "high"
    if total_length > 100:
        return "medium"
    return "low"

def validate_color(color: str) -> bool:
    allowed = {"yellow", "blue", "red", "green", "purple"}
    return color in allowed
    