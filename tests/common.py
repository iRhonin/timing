from random import randint

from timing.db.session import Session
from timing.models.user import User


def add_mock_user():
    user = User(username=randint(1000, 99999))
    Session.add(user)
    Session.commit()
    Session.expire(user)
    return user
