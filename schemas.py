"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

# ---------------- VoiceForge App Schemas ----------------

class DemoRequest(BaseModel):
    name: str = Field(..., min_length=2, description="Full name")
    email: EmailStr
    company: Optional[str] = Field(None, description="Company name")
    phone: Optional[str] = Field(None, description="Phone number")
    interest: Optional[str] = Field(None, description="Interested agent or package")
    message: Optional[str] = Field(None, description="Optional message")

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    phone: Optional[str] = None
    company: Optional[str] = None
    message: str = Field(..., min_length=5)

class OrderItem(BaseModel):
    agent: str = Field(..., description="Agent or package identifier")
    quantity: int = Field(1, ge=1, le=10)

class OrderRequest(BaseModel):
    customer_name: str
    customer_email: EmailStr
    company: Optional[str] = None
    phone: Optional[str] = None
    selection: List[OrderItem]
    setup_fee: float
    monthly_total: float
    notes: Optional[str] = None

# Example schemas (kept for reference; not used in app)
class User(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
