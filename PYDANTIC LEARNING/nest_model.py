from pydantic import BaseModel,Field
from typing import List,Dict,Optional,Annotated

class Supplier(BaseModel):
    name: Annotated[str, Field(max_length=100, default="Unknown Supplier", description="Supplier Name")]
    contact_info: Optional[Dict[str, str]] = None

class Product(BaseModel):
    product_name: Annotated[str, Field(max_length=100, default="Unnamed Product", description="Product Name")]
    price: float
    quantity_in_stock: int
    supplier: Optional[Supplier] = None
    
p1={"product_name": "Laptop", "price": 999.99, "quantity_in_stock": 50, "supplier": {"name": "Tech Supplies", "contact_info": {"phone": "9876543210", "email":"mubasir@gmail"}}}

Product1=Product(**p1)
print(Product1)
print(Product1.supplier.name)