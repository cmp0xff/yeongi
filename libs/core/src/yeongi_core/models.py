from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ChatType(StrEnum):
    """Supported chat types."""

    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"


class MediaType(StrEnum):
    """Supported media types."""

    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    VOICE = "voice"
    DOCUMENT = "document"


class User(BaseModel):
    """Domain model for a user."""

    model_config = ConfigDict(frozen=True)

    id: str
    is_bot: bool = False
    first_name: str
    last_name: str | None = None
    username: str | None = None


class Chat(BaseModel):
    """Domain model for a chat or conversation."""

    model_config = ConfigDict(frozen=True)

    id: str
    type: ChatType
    title: str | None = None


class Media(BaseModel):
    """Domain model for an attachment or media file."""

    model_config = ConfigDict(frozen=True)

    file_id: str
    type: MediaType
    mime_type: str | None = None
    file_size: int | None = None
    uri: str | None = None  # Storage URI (e.g., GCS path)


class Message(BaseModel):
    """Domain model for a message."""

    model_config = ConfigDict(frozen=True)

    id: str
    date: datetime
    chat: Chat
    from_user: User | None = Field(None, alias="from")
    text: str | None = None
    media: list[Media] = Field(default_factory=list)


class Snapshot(BaseModel):
    """Domain model for capturing bot conversation state."""

    model_config = ConfigDict(frozen=True)

    user_id: str
    chat_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    state: dict[str, Any] = Field(default_factory=dict)
