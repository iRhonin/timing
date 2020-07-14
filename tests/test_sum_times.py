from datetime import datetime

import falcon

from tests.common import add_mock_user
from timing.db.session import Session
from timing.models.time import Time


def test_sum_times(client):
    user = add_mock_user()
    other_user = add_mock_user()

    user.times = [
        Time(hours=i)
        for i in range(50)
    ]
    expected_sum = sum(t.hours for t in user.times)

    out_of_date_time = Time(
        hours=3,
        created_at=datetime.strptime(
            '1010-07-14T17:42:53',
            '%Y-%m-%dT%H:%M:%S',
        ),
    )
    user.times.append(out_of_date_time)

    other_user.times.append(
        Time(hours=1),
    )
    Session.commit()

    headers = {
        'X-IDENTITY': str(user.id),
    }

    time_response = client.simulate_get(
        f'/time/calculator?from=2020-01-01T00:00:00&to=2021-01-01T00:00:00',
        headers=headers,
    )
    assert time_response.status == falcon.HTTP_OK

    result = falcon.json.loads(time_response.content.decode())
    assert result['hours'] == expected_sum
