# tests/test_db_storage.py

import pytest
from models.db_storage import DBStorage
from models.user import User
from models.website import Website
from models.event import Event


@pytest.fixture(scope="function")
def test_objects(db):
    """Fixture to create test objects for the all() method."""

    # Create User, Website, and Event objects
    user = User(username="test_user", password_hash="hashed_password")
    website = Website(domain="example.com", user_id=user.id)
    event = Event(event_type="page_view", website_id=website.id)

    # Add objects to the session
    db.new(user)
    db.new(website)
    db.new(event)
    db.save()  # Commit the changes to the database
    
    yield {'user': user, 'website': website, 'event': event}

    # Teardown logic: delete the created objects after the test
    db.delete(event)
    db.delete(website)
    db.delete(user)
    db.save()

def test_all(db, test_objects):
    """Test that the all() method retrieves all objects correctly."""
    result = db.all()

    # Ensure objects are in the result
    assert f"User.{test_objects['user'].id}" in result
    assert f"Website.{test_objects['website'].id}" in result
    assert f"Event.{test_objects['event'].id}" in result

def test_all_with_class(db, test_objects):
    """Test that the all() method retrieves objects of a specific class."""
    user_results = db.all(User)
    assert f"User.{test_objects['user'].id}" in user_results

    website_results = db.all(Website)
    assert f"Website.{test_objects['website'].id}" in website_results

    event_results = db.all(Event)
    assert f"Event.{test_objects['event'].id}" in event_results
