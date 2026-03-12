from datetime import UTC, datetime

import pytest
from pydantic import ValidationError
from yeongi_core.models import Chat, ChatType, Message, User


def test_user_creation() -> None:
    user = User(id="123", first_name="Test", last_name="User", username="testuser")
    assert user.id == "123"
    assert user.first_name == "Test"
    assert user.is_bot is False


def test_chat_creation() -> None:
    chat = Chat(id="456", type=ChatType.PRIVATE, title="Test Chat")
    assert chat.id == "456"
    assert chat.type == ChatType.PRIVATE


def test_message_creation() -> None:
    user = User(id="123", first_name="Test")
    chat = Chat(id="456", type=ChatType.PRIVATE)
    now = datetime.now(UTC)

    # Test using 'from' alias
    message = Message(
        id="789",
        date=now,
        chat=chat,
        **{"from": user},
        text="Hello world",
    )

    assert message.id == "789"
    assert message.from_user.id == "123"
    assert message.text == "Hello world"


def test_immutable_models() -> None:
    user = User(id="123", first_name="Test")
    with pytest.raises(ValidationError):
        # Pydantic v2 raises ValidationError (FrozenInstanceError is a subclass)
        # when trying to mutate a frozen model
        user.first_name = "New Name"
