import requests
from config import BITRIX_WEBHOOK


class Bitrix24API:
    def __init__(self):
        self.base_url = BITRIX_WEBHOOK.rstrip("/") + "/"
        self.session = requests.Session()

    def call(self, method: str, params: dict | None = None):
        url = f"{self.base_url}{method}"
        response = self.session.post(url, json=params or {}, timeout=180)
        response.raise_for_status()

        data = response.json()

        if "error" in data:
            raise Exception(f"Bitrix24: {data.get('error_description', data['error'])}")

        return data["result"]