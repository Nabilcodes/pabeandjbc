# service_clients.py

# import httpx

# class ExternalServiceClient:
#     def __init__(self, base_url: str):
#         self.base_url = base_url
#         self.client = httpx.Client(base_url=self.base_url)

#     def send_document(self, document: dict) -> str:
#         response = self.client.post("/api/receive-document", json=document)
#         response.raise_for_status()
#         return response.text

from sqlalchemy.orm import Session

from . import models, schemas

def get_billing(db: Session, billing_id: int):
    return db.query(models.Billing).filter(models.Billing.id == billing_id).first()

def get_billings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Billing).offset(skip).limit(limit).all()

def get_billing_by_name(db: Session, name: str):
    return db.query(models.Billing).filter(models.Billing.billed_name == name)

def create_billing(db: Session, billing: schemas.BillingCreate):
    db_billing = models.Billing(billed_name=billing.billed_name,
                                billed_email=billing.billed_email,
                                status="UNPAID", 
                                value= 5*billing.nilai_fob/100 + billing.nilai_pabean)
    db.add(db_billing)
    db.commit()
    db.refresh(db_billing)
    return db_billing
