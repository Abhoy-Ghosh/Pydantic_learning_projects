# when we use one model into the field of the other pydantic model 
# it is called nested_model

from pydantic import BaseModel,Field
from typing import Optional, List

#example: 
# address is like complex datatype like mix of the  int +str etc
# in that case we can create another pydantic model and used it into the main model

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


address = Address(**{
                  'house_no' :123,
                  'city' : 'abc_city',
                  'state' :'xyz_state',
                  'pin' : 123456})

pateint_info = Patient(**{
    'name' : 'abc',
    'age' : 20,
    'weight' : 60.5,
    'address' : address
})

print("\npatient information: ",pateint_info)
print("\naddress of the patient: ",pateint_info.address)
print("\ncity of the patient: ",pateint_info.address.city)

# Better organizartion of related data(e.g. - vitals, address, insurance )
# Reusability : Use Vitals in multiple models (e.g - Patient ,Medicalrecord)
# Readability : Easier for developers and API consumers to understand
# Validation :  Nested models are validated auomtomatically - reduce work load