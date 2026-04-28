from pydantic import BaseModel
from typing import List,Dict,Optional

# step1 : make pydatic class 
class Patient(BaseModel):
    name: str
    age: int
    weight:float 
    allergies :List[str] # <- means List of str - 2 level validation (do not use list directly as it can not use for type check)
    contact: Dict[str,str] # <- means key value both are str

    # making optional fields
    married : Optional[bool] = None # <- none is important for optional fields  else it throw validation error
    family_members : Optional[Dict[str,str]] =None


# step2: create a object out of the class
patient_info_dict = {
    'name':'abcde',
    'age':20,
    'weight':60.5,
    'allergies':['dust','pollen'],
    'contact' : {'email':'abc@xyz.com', 'address' : 'pqr road'}
    } # <- we need to put all the required fields in the raw data which fields are intialized in pydantic model

patient_obj1=Patient(**patient_info_dict)# object intiate with raw data also checking at this step
# ** unpack dictionary syntax

def insert_patient_data(patient_dummy : Patient) :#patient_dummy variable of custom Patient type
    print(patient_dummy.name)
    print(patient_dummy.age)
    print(patient_dummy.family_members)
    print(patient_dummy.married)
    print('inserted successfully')
    print()


def update_patient_data(patient : Patient):
    print(patient.name,'name updated successfully')
    print(patient.age,"age updated successfully")
    print("updated successfully")
    

insert_patient_data(patient_obj1)

update_patient_data(patient_obj1)



# def insert_pateint_data(name,age):
#     print(name)

#