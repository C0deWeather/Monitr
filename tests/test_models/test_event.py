#!/usr/bin/env python3
"""This module tests the Website class"""

from datetime import datetime
from models.event import Event
import pytest
import uuid


def test_user():
    """Tests an instance of the User class"""

    kwargs = {
        "id": str(uuid.uuid4()),
        "website_id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "event_type": "url",
        "event_data": "www.nicrobit.com",
    }
    page_views = Event(**kwargs)
    d = page_views.to_dict()

    assert "__class__" in d and\
        d["__class__"] == 'Event' and\
        "created_at" in d and\
        "id" in d and\
        "event_type" in d and\
        "website_id" in d and\
        "event_data" in d and\
        "_sa_instance_state" not in d
