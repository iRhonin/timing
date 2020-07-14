from random import randint
import falcon


def test_list_images(client):
    username = str(randint(1000, 9999))

    user = {
        'username': username
    }

    response = client.simulate_post('/register', json=user)
    result = falcon.json.loads(response.content.decode())

    assert result['username'] == user['username']
    assert result['id'] is not None
    assert response.status == falcon.HTTP_OK
