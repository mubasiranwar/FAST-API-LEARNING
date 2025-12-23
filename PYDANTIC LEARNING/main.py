from pydantic import BaseModel,Field
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50,default="Unknown",description="Patient Name",examples=["John Doe","Jane Smith"])]
    age:int
    weight:float
    allergies:Optional[List[str]]=None
    contact_detail:Optional[Dict[str,str]]=None
    
    
    
    
def insert_data(p1:Patient):
    print(f"Patient Name: {p1.name}, Age: {p1.age}, Weight: {p1.weight},allergies: {p1.allergies}, Contact Detail: {p1.contact_detail}")
    print("Data inserted successfully")
    
def update_data(p1:Patient):
    print(f"Patient Name: {p1.name}, Age: {p1.age}")
    print("Data updated successfully")
    
    
patient1={"name":"Khan", "age":30,"weight":83.5,"allergies":["pollen","dust"],"contact_detail":{"phone":"1234567890","email":"mubasir@gmail,com"}}  
    
patient2={"name":"Ali", "age":25,"weight":70.2}
# p1=Patient(**patient1)
# insert_data(p1)
# update_data(p1)
p2=Patient(**patient2)
update_data(p2)
