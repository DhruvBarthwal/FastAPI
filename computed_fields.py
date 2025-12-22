from pydantic import BaseModel, EmailStr,computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age : int
    weight: float
    married : float
    height : float
    allergies : List[str]
    contact_details : Dict[str,str]
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.height)
    print(patient.weight)
    print('BMI',patient.calculate_bmi )    
    print('updated')

patient_info = {
    "name": "Dhruv",
    "email": "dhruv@example.com",
    "age": 22,
    "weight": 75.2,
    "married": False,
    "height": 1.72,
    "allergies": ["dust"],
    "contact_details": {"phone": "1234567890"}
}
patient1 = Patient(**patient_info)
update_patient_data(patient1)