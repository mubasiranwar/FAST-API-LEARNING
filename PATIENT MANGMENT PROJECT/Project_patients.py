from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,model_validator,computed_field
from typing import Annotated,Literal,Optional
import json
app=FastAPI()


class Patient(BaseModel):
    id:str
    name: str
    city: str
    age:Annotated[int,Field(...,gt=0,lt=120,description="Age must be between 1 and 119")] 
    gender:Annotated[Literal['male','female','other'],Field(...,description="Gender must be male, female, or other")] 
    height:Annotated[float,Field(...,gt=0,description="Height must be positive")] 
    weight:Annotated[float,Field(...,gt=0,description="Weight must be positive")]
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = self.weight / ((self.height / 100) ** 2)  # height converted to meters
        return round(bmi, 2)
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
#for update patient
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]  
                                             


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


###get request
@app.get("/mubasir")

def mubasir():
    return {"message": "This page contain information about mubasir!"}
         

### post request
@app.post("/greet")
def greet_user(name:str):
    return {"message": f"Hello, {name}!"}
    

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

#utility funcation save data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
        

@app.get("/view")
def view_data():
    data = load_data()
    return data


@app.get("/view/{patient_id}")
def get_patient(patient_id: str= Path(..., description="The ID of the patient to retrieve")):
    data = load_data()
    
    if patient_id in data:  
            return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort by height, weight, or age"),
    order: str = Query("asc", description="Sorting order: asc or desc")
):
    data = load_data()

    # Validate sort key
    valid_fields = ["height", "weight", "age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort parameter")

    # Validate order
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order value")

    # Actual sorting
    sorted_data = dict(
        sorted(
            data.items(),
            key=lambda item: item[1][sort_by],
            reverse=(order == "desc")     # reverse=True for descending
        )
    )

    return sorted_data


@app.post("/add_patient")
def add_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists.")

    # Add new patient
    data[patient.id] = patient.model_dump(exclude={"id"})

    # Save back to JSON file---->utility function
    save_data(data)

    return {"message": "Patient added successfully", "patient": patient}

@app.put("/update_patient/{patient_id}")
def update_patient(
    patient_id: str = Path(..., description="The ID of the patient to update"),
    patient_update: PatientUpdate = ...
):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update only provided fields
    existing_patient = data[patient_id]
    update_data = patient_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        existing_patient[key] = value

    # Save back to JSON file
    save_data(data)

    return {"message": "Patient updated successfully", "patient": existing_patient}


# delete patient
@app.delete("/delete_patient/{patient_id}")
def delete_patient(patient_id: str = Path(..., description="The ID of the patient to delete")):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Delete patient
    deleted_patient = data.pop(patient_id)

    # Save back to JSON file
    save_data(data)

    return {"message": "Patient deleted successfully", "patient": deleted_patient}