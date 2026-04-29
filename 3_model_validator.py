# when we need single field vaildation we use field validator 
# when we need validate multiple field validation we use model validation

from pydantic  import BaseModel,Field, EmailStr, field_validator, model_validator
from typing import Optional,List,Dict,Annotated

class Patient(BaseModel):
    name : str
    # email: EmailStr
    age: int = Field(gt = 0,le= 100)
    weight:float
    # married : Optional[bool] =None
    # allergies : Optional[List[str]] = None
    contact: Dict[str,int]
    disease : str
   

    @model_validator(mode = 'after') # do not need to mention any field 
    def validate_emergency_contact(cls, model):
        if model.age < 18 and 'parents_contact' not in model.contact:
            raise ValueError("Minor should provide their parents contact number")
        return model
    
patients_info ={
    'name':'xyz',
    'age':5,
    'weight': 60.5,
    'contact' : {
        'patient_contact' : 9876543210,
        'parents_contact' : 1234567890,
        'emergency_contact': 4201651458
    },
    'disease':'cold'
}

pateint_1 = Patient(**patients_info)
# print(pateint_1)

def check_minor_patient(patient :Patient):
    print(patient.name)
    print(patient.age)
    # print(patient.contact['emergency_contact'])
    print("minor patient checked successfully")


check_minor_patient(pateint_1)
    