from pydantic import BaseModel,field_validator


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    allergies: list[str] = None
    contact_detail: dict[str, str] = None
    
    @field_validator("age")
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age must be a non-negative integer")
        return value

def insert_data(p1: Patient):
    print(f"Patient Name: {p1.name}, Age: {p1.age}, Weight: {p1.weight}, Allergies: {p1.allergies}, Contact Detail: {p1.contact_detail}")
    print("Data inserted successfully")


p1={"name": "Khan", "age": 30, "weight": 83.5, "allergies": ["pollen", "dust"], "contact_detail": {"phone": "1234567890", "email":"mubasir@gmail.com"}}

patient1=Patient(**p1)

print(patient1)