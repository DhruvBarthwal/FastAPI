from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List,Dict, Optional, Annotated
#Step 1 : Create a base model
class Patient(BaseModel):
    name : Annotated[str, Field(max_length = 50, title = 'Name of the patient', description = 'Give the name of the patient in less than 50 chars', examples=['Dhruv', 'Chinu'])]
    
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt = 0, lt = 120)
    weight : Annotated[float, Field(gt= 0, strict = True)]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]
    
    allergies : Annotated[Optional[List[str]], Field(default= None, max_length = 5)] = None # optional
    contact_details : Dict[str,str]
    
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')
    
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {"name" : 'Dhruv','email':'abc@gmail.com','linkedin_url':'https://linkedin.com/123', 'age' : '30','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details' : {'email' : 'abc@gmail.com','phone':'24343434'}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
    
    