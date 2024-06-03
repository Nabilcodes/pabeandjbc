from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .database import Base

class Billing(Base):
    '''
    Status:
    Unpaid
    Paid
    '''
    __tablename__ = "billings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    billed_name = Column(String, index=True)
    billed_email = Column(String, index=True)
    value = Column(Integer, index=True)
    status = Column(String, index=True)