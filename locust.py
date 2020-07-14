from random import randint

from locust.contrib.fasthttp import FastHttpUser

from locust import between, task, SequentialTaskSet


class PerformanceTest(FastHttpUser):
    wait_time = between(0, .1)

    user_id = None

    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })

    # @task
    def on_start(self):
        register_resp = self.client.post(
            '/register',
            json=dict(username=str(randint(10000000, 999999999))),
        ).json()
        self.user_id = register_resp['id']

    @task
    def add(self):
        self.client.post(
            '/time/add',
            json=dict(
                hours=randint(1, 24),
            ),
            headers={
                'X-IDENTITY': self.user_id,
            },
        )

    @task
    def add_missing(self):
        t = '1010-07-14T17:42:53'
        self.client.post(
            f'/time/add?t={t}',
            json=dict(
                hours=randint(1, 24),
            ),
            headers={
                'X-IDENTITY': self.user_id,
            },
        )

    @task
    def get(self):
        self.client.get(
            f'/time/get?from=2020-01-01T00:00:00&to=2021-01-01T00:00:00',
            headers={
                'X-IDENTITY': self.user_id,
            },
        )

    @task
    def get_sum(self):
        self.client.get(
            f'/time/calculator?from=2020-01-01T00:00:00&to=2021-01-01T00:00:00',
            headers={
                'X-IDENTITY': self.user_id,
            },
        )
