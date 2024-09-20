import pytest
from models.db_storage import DBStorage


@pytest.fixture(scope="module")
def db():
    """Fixture to set up and tear down a database instance for testing."""

    # Setup
    storage = DBStorage()
    storage.reload()  # Load tables
    yield storage

    # Teardown
    storage.close()
    