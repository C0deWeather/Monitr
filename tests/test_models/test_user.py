#!/usr/bin/env python3
"""This module tests the User class"""

from datetime import datetime
from models.user import User
import pytest
import uuid


def test_user():
    """Tests an instance of the User class"""

    kwargs = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "name": "Bright Frank",
        "email": "frankbright211@gmail.com",
        "password_hash": "this is a hash"
    }
    Bola = User(**kwargs)
    d = Bola.to_dict()

    assert "__class__" in d and\
        d["__class__"] == 'User' and\
        "created_at" in d and\
        "id" in d and\
        "name" in d and\
        "email" in d and\
        "password_hash" in d and\
        "_sa_instance_state" not in d
