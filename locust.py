from random import randint

from locust import between, task
from locust.contrib.fasthttp import FastHttpUser


class PerformanceTest(FastHttpUser):
    wait_time = between(0, .1)

    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })

    @task
    def register(self):
        self.client.post(
            '/register',
            json=dict(username=str(randint(10000000, 999999999))),
        )
