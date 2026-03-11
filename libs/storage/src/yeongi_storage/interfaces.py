from abc import ABC, abstractmethod

from yeongi_core.models import Message, Snapshot


class IStorage(ABC):
    """Interface for persistence of messages and snapshots."""

    @abstractmethod
    async def save_message(self, message: Message) -> None:
        """Persist a message to the database."""
        ...

    @abstractmethod
    async def save_snapshot(self, snapshot: Snapshot) -> None:
        """Capture and save a bot state snapshot."""
        ...

    @abstractmethod
    async def get_latest_snapshot(
        self,
        user_id: str,
        chat_id: str,
    ) -> Snapshot | None:
        """Retrieve the most recent snapshot for a user in a chat."""
        ...


class IBlobStore(ABC):
    """Interface for saving and retrieving large media files (GCS/Local)."""

    @abstractmethod
    async def upload(self, content: bytes, filename: str) -> str:
        """Upload a file and return its storage URI."""
        ...

    @abstractmethod
    async def download(self, uri: str) -> bytes:
        """Download a file's content by its URI."""
        ...
