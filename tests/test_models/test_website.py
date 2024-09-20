#!/usr/bin/env python3
"""This module tests the Website class"""

from datetime import datetime
from models.website import Website
import pytest
import uuid


def test_user():
    """Tests an instance of the User class"""

    kwargs = {
        "id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "name": "Nicrobit",
        "url": "www.nicrobit.com",
    }
    nicrobit = Website(**kwargs)
    d = nicrobit.to_dict()

    assert "__class__" in d and\
        d["__class__"] == 'Website' and\
        "created_at" in d and\
        "id" in d and\
        "name" in d and\
        "user_id" in d and\
        "url" in d and\
        "_sa_instance_state" not in d
