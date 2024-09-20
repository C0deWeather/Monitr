#!/usr/bin/env python3
"""This module tests the BaseModel class and its methods"""

from datetime import datetime
import pytest
from models.base_model import BaseModel
import uuid


def is_valid_uuid4(id_str):
    try:
        # Parse the string into a UUID object
        val = uuid.UUID(id_str, version=4)
    except ValueError:
        # If parsing raises an error, it's not a valid UUID
        return False

    # Ensure that the ID is exactly a uuid4 by checking the version
    return val.version == 4

def test_basemodel_without_args():
    """Tests an instance of BaseModel without args"""

    b = BaseModel()
    assert is_valid_uuid4(b.id) and isinstance(b.created_at, datetime)

def test_kwargs():
    """Tests an instance of BaseModel with kwargs"""

    kwargs = {
        "name": "Bright",
        "email": "bflloyd1653@gmail.com",
        "password": "FRank1640"
    }
    b = BaseModel(**kwargs)
    assert is_valid_uuid4(b.id) and isinstance(b.created_at, datetime)
    assert b.name == "Bright"
    assert b.email == "bflloyd1653@gmail.com"
    assert b.password == "FRank1640"

def test_to_dict():
    """Tests the to_dict() method"""

    b = BaseModel()
    d = b.to_dict()
    assert isinstance(d, dict) and\
    "__class__" in d and\
    "created_at" in d and\
    "id" in d and\
    "_sa_instance_state" not in d

    isinstance(d["created_at"], str)
    try:
        datetime.fromisoformat(d["created_at"])
    except ValueError:
        pytest.fail("created_at is not a valid ISO format datetime")