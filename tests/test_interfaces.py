import pytest
from yeongi_core.interfaces import IBotAdapter
from yeongi_storage.interfaces import IBlobStore, IStorage


def test_ibotadapter_is_abstract() -> None:
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        # Can't instantiate abstract class with abstract methods
        IBotAdapter()


def test_istorage_is_abstract() -> None:
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        IStorage()


def test_iblobstore_is_abstract() -> None:
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        IBlobStore()
