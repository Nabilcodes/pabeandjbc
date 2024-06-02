from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from pabeandjbc.service_clients import PIBDocument
from service_clients import ExternalServiceClient
from orchestration import OrchestrationService

app = FastAPI()

# Initialize the external service client
external_service_client = ExternalServiceClient(base_url="http://external-service")

# Initialize the orchestration service
orchestration_service = OrchestrationService(external_service_client)

@app.post("/submit-pib")
async def submit_pib(document: PIBDocument):
    try:
        document_dict = document.dict()
        response = orchestration_service.process_document(document_dict)
        return JSONResponse(content={"message": "Document processed successfully", "response": response})
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
