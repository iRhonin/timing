from datetime import datetime
from random import randint
from time import sleep

import falcon


def _register(client):
    username = str(randint(1000, 9999))
    user_data = {
        'username': username
    }

    register_response = client.simulate_post('/register', json=user_data)
    user = falcon.json.loads(register_response.content.decode())
    return user


def test_add_time(client):
    user = _register(client)

    time_data = {
        'hours': randint(1, 10),
    }
    auth_header = {
        'X-IDENTITY': str(user['id']),
    }

    time_response = client.simulate_post(
        '/time/add',
        json=time_data,
        headers=auth_header,
    )
    assert time_response.status == falcon.HTTP_OK

    result = falcon.json.loads(time_response.content.decode())
    assert result['createdAt'] is not None
    assert result['hours'] == time_data['hours']


def test_forgotten_add_time(client):
    user = _register(client)

    time_data = {
        'hours': randint(1, 10),
    }
    auth_header = {
        'X-IDENTITY': str(user['id']),
    }

    t = '1010-07-14T17:42:53'

    time_response = client.simulate_post(
        f'/time/add?t={t}',
        json=time_data,
        headers=auth_header,
    )
    assert time_response.status == falcon.HTTP_OK

    result = falcon.json.loads(time_response.content.decode())
    assert result['createdAt'] == t
    assert result['hours'] == time_data['hours']
