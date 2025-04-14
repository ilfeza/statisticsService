from locust import HttpUser, task, between
import random
from datetime import datetime


class DeviceMeasureUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(0.5, 1.5)

    def on_start(self):
        self.device_id = random.randint(1, 10)

    @task(3)
    def post_measure(self):
        # Имитация данных измерения
        payload = {
            "x": round(random.uniform(-10.0, 10.0), 3),
            "y": round(random.uniform(-10.0, 10.0), 3),
            "z": round(random.uniform(-10.0, 10.0), 3),
            "timestamp": datetime.utcnow().isoformat()
        }

        self.client.post(
            f"/devices/{self.device_id}/measures/",
            json=payload
        )

    @task(1)
    def get_stats(self):
        # Параметры start_time и end_time опциональны — можно не указывать
        self.client.get(f"/devices/{self.device_id}/status/")
