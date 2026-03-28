from __future__ import annotations

from typing import List, Literal
from pydantic import BaseModel, Field

from datetime import datetime


class Scene(BaseModel):
    speaker: str = Field("Name of focal persona.")
    recipient: str = Field("Name of recipient persona (close circle of focal persona).")
    summary: str = Field("Summary of the overall tone and content of the converstaion described in the scene between speaker and recipient.")

class SceneList(BaseModel):
    scenes: list[Scene] = Field("List of scenes.")


class Message(BaseModel):
    speaker: str = Field("Persona name of the speaker or sender of this message.")
    content: str = Field("Content in the message.")
    timestamp: datetime = Field(..., description="UTC timestamp of when the message was sent")


class Transcript(BaseModel):
    focal_persona: str = Field("Name of focal persona involved in transcript.")
    recipient_persona: str = Field("Name of recipient persona involved in transcript.")
    msgs: list[Message] = Field("List of messages between 2 individuals")