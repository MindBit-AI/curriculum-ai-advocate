from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TrelloCard(BaseModel):
    """
    Represents a Trello card with its core properties
    """
    name: str = Field(description="Title of the card")
    desc: str = Field(description="Description of the card")
    labels: List[str] = Field(default_factory=list, description="Labels attached to the card")
    