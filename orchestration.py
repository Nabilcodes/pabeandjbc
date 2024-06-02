# orchestration.py

import uuid
from typing import Dict

class OrchestrationService:
    def __init__(self, external_service_client):
        self.external_service_client = external_service_client

    def validate_document(self, document: Dict) -> bool:
        # Perform validation (e.g., check required fields, format, etc.)
        if not document.get("document_id") or not document.get("content"):
            return False
        return True

    def generate_billing_code(self) -> str:
        # Generate a unique billing code
        return str(uuid.uuid4())

    def process_document(self, document: Dict) -> str:
        if not self.validate_document(document):
            raise ValueError("Invalid document")
        
        billing_code = self.generate_billing_code()
        document["billing_code"] = billing_code

        response = self.external_service_client.send_document(document)
        return response
