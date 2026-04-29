# when we calculate any field on the go(runtime) by using the others field
# we use computed_fields

from pydantic  import BaseModel,Field, EmailStr, computed_field
from typing import Optional,List,Dict,Annotated

class Patient(BaseModel):
    name : str
    age : int = Field(gt = 0,le= 100)
    weight  : float
    height : float = Field(gt = 0)
    married : Optional[bool] =None
    # allergies : Optional[List[str]] = None
    contact: Dict[str,int]
    disease : str

    @computed_field
    @property
    def calculate_bmi(self) -> float: # here we get a instance of pydantic model

        # in that case method(function) name is the computed_field of the model
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi # return type mentioned earlier to check the type validation
    
patients_info ={
    'name':'xyz',
    'age':5,
    'weight': 60.5,
    'height':48,
    'contact' : {
        'patient_contact' : 9876543210,
        'parents_contact' : 1234567890,
        'emergency_contact': 4201651458
    },
    'disease':'cold'
}

pateint = Patient(**patients_info)

def insert_patient_details(patient :Patient):
    print(patient.name)
    print(patient.age)
    print(patient.calculate_bmi)

insert_patient_details(pateint)