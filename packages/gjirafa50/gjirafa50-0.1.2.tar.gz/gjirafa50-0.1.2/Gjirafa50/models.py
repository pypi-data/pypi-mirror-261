# models.py

from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    title: str
    price: str
    discount: Optional[str]
    link: str
    availability: str
    image_url: str
    full_description: str

class ScrapeResult(BaseModel):
    total_pages: str
    views: str
    products: List[Product]
