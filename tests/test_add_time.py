from random import randint

import falcon

from tests.common import add_mock_user


def test_add_time(client):
    user = add_mock_user()

    time_data = {
        'hours': randint(1, 10),
    }
    auth_header = {
        'X-IDENTITY': str(user.id),
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
    user = add_mock_user()
    time_data = {
        'hours': randint(1, 10),
    }
    auth_header = {
        'X-IDENTITY': str(user.id),
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
