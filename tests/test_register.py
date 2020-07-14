from random import randint

import falcon


def test_register(client):
    username = str(randint(1000, 9999))
    user = {
        'username': username
    }

    response = client.simulate_post('/register', json=user)
    assert response.status == falcon.HTTP_OK

    result = falcon.json.loads(response.content.decode())
    assert result['username'] == user['username']
    assert result['id'] is not None
