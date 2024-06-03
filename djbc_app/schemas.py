from pydantic import BaseModel
import uuid

class BillingBase(BaseModel):
    billed_name: str
    billed_email: str
    value: int

class BillingCreate(BillingBase):
    pass

class Billing(BillingBase):
    id: uuid
    status: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True
