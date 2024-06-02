# service_clients.py

import httpx

class ExternalServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url)

    def send_document(self, document: dict) -> str:
        response = self.client.post("/api/receive-document", json=document)
        response.raise_for_status()
        return response.text
