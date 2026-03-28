from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import BaseModel, Field

from datetime import datetime


class CalendarEntry(BaseModel):
    dt: datetime = Field("Datetime for event.")
    name: str = Field("Name of event in calendar log.")
    content: str = Field("Short description of calendar event.")
    participants: Optional[str] = Field("Included list of personas participating in event or none.")


class CalendarLog(BaseModel):
    persona: str = Field("Name of persona associated with calendar logs.")
    entries: list[CalendarEntry] = Field("List of calendar entries for the persona.")