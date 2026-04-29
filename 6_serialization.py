# how to export existing pydantic model object as json or dictionary 
# helpful for the Build the APIs like FastAPI

from pydantic import BaseModel,Field
from typing import Optional, List


class Address(BaseModel):
    house_no : int
    city : str
    state : str 
    pin :int = Field(le = 999999)


class Patient(BaseModel):
    name : str
    age : int
    weight : float
    address : Address
    gender: str = "male" #defsult male -> tes for exclude unset

address = Address(**{
                  'house_no' :123,
                  'city' : 'abc_city',
                  'state' :'xyz_state',
                  'pin' : 123456})

patient_info={
    'name' : 'abc',
    'age' : 20,
    'weight' : 60.5,
    'address' : address
}

patient= Patient(**patient_info)

print("\npatient information: ",patient)
print("\naddress of the patient: ",patient.address)
print("\ncity of the patient: ",patient.address.city)
print()



validated_patient_data_dict =patient.model_dump(include = ['name','age','address'], exclude={'address' : ['state']})
print(validated_patient_data_dict)
print(type(validated_patient_data_dict))

print()


validated_patient_data_json = patient.model_dump_json( exclude_unset=True) # gender excluded
print(validated_patient_data_json)
print(type(validated_patient_data_json))