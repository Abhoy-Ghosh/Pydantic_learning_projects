from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List,Dict,Optional,Annotated

# step1 : make pydantic class 
class Patient(BaseModel):
    # type validation
    name: str
    age: int
    weight:float 
    allergies :List[str] # <- means List of str - 2 level validation (do not use list directly as it can not use for type check)
                        # list  ❌ no inner validation
                        # List[str] ✅ strict validation
    contact: Dict[str,str] # <- means key value both are str
    new_visit : bool = True # <- default value(True is set)

    # making optional fields
    married : Optional[bool] = None # <- none is important for optional fields  else it throw validation error
    family_members : Optional[Dict[str,str]] =None

    # data validation (custom validators by pydantic)
    email : EmailStr
    linkedin_url:Optional[AnyUrl] = None

    #data validation (using Field function)
    height: float = Field(gt  = 0) # it means we can not set the value less than 0 (always greater than 0)
    working_hours : int= Field(gt = 0, lt = 24) # gt,lt,ge,le
    diagonsed_by : List[str] = Field(max_items = 5) # max items 5 for the list(max length of list 5)
    # max_length works for strings

    # field function also help to add metadata <- shown in api documentation (swagger ui in FastAPI)
    disease : Annotated[str, Field(max_length = 50, 
                                   default='unknown', # unknown as default  
                                   title = 'Disease Name', # metadata using Annoted and Field
                                   description = 'give Disease name in 50 characters',
                                   examples= ["Fever","Cough","Cold"])]

    # sirict mode -> suppress the coerence of the datatype
    # if float or int is needed  we need to provide exact datatype int or float but numeric string through an error
    num_of_patient : Annotated[int,Field(strict = True)]
    num_of_family: Annotated[int,Field(strict= True,
                                              title= 'Number of patients family')]


# step2: create a object out of the class
patient_info_dict = {
    'name':'abcde',
    'age':20,
    'weight':60.5,
    'allergies':['dust','pollen'],
    'contact' : {'email':'abc@xyz.com', 'address' : 'pqr road'},
    'email' : 'abc@xyz.com',
    'linkedin_url' : 'https:/linkedin.com/abc123',
    'height' : 80.2,
    'working_hours' : 12,
    'diagonsed_by':['abc','xyz','pqr','lmn'],
    'disease' : 'cold',
    'num_of_patient':1234567890,
    'num_of_family': 987654321

    } # <- we need to put all the required fields in the raw data which fields are intialized in pydantic model

patient_obj1=Patient(**patient_info_dict)# object intiate with raw data also checking at this step
# ** unpack dictionary syntax

def insert_patient_data(patient_dummy : Patient) :#patient_dummy variable of custom Patient type
    print(patient_dummy.name)
    print(patient_dummy.age)
    print(patient_dummy.family_members)
    print(patient_dummy.married)
    print(patient_dummy.new_visit)
    print(patient_dummy.email)
    print(patient_dummy.linkedin_url)
    print(patient_dummy.height)
    print(patient_dummy.working_hours)
    print(patient_dummy.diagonsed_by)
    print(patient_dummy.num_of_patient)
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