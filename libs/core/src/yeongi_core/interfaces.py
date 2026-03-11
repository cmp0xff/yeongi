from abc import ABC, abstractmethod
from typing import Protocol

from .models import Message


class BotHandler(Protocol):
    """Protocol for handling incoming messages."""

    async def __call__(self, message: Message) -> object: ...


class IBotAdapter(ABC):
    """Interface for messaging platform adapters (e.g., Telegram, Feishu)."""

    @abstractmethod
    async def send_message(
        self,
        chat_id: str,
        text: str,
        reply_to_message_id: str | None = None,
    ) -> Message:
        """Send a text message to a chat."""
        ...

    @abstractmethod
    async def run(self, handler: BotHandler) -> None:
        """Start the bot and listen for events."""
        ...
