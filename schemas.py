from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class SubcategorySchemaCreate(BaseModel):
    name: str
    subcategory: int


class SubcategoryScheme(BaseModel):
    id: int
    name: str
    subcategory: int


class CategorySchemaCreate(BaseModel):
    name: str


class CategoryScheme(BaseModel):
    id: int
    name: str
    subcategories: List[SubcategoryScheme]


class ProductListSchema(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    sold_quantity: int


class RequsetDataSchema(BaseModel):
    min: float | None
    max: float | None
    size: list | None
    category: str | None
    brands: list | None







