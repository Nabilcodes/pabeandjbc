from pydantic import BaseModel
import uuid

class BillingBase(BaseModel):
    billed_name: str
    billed_email: str

class BillingCreate(BillingBase):
    nilai_fob: int
    nilai_pabean: int
    pass

class Billing(BillingBase):
    id: uuid
    status: str
    value: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True
