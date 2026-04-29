from pydantic import BaseModel,Field,EmailStr,AnyUrl ,field_validator
from typing import Annotated,Optional, List,Dict
# use of field validator check the data according to custom bussiness logic

# 1.
# like email except only the gmail or yahoo or hotemail domain but not others in this case we can use field valiidator
# to implement that we need to make a method in the class
#  along with the decorator -> @field_validator('email')
                        #   -> @classmethod
                        #    -> function or method defination

# 2. 
# we can use field_validator for transformation 
# like capitalize


class Patient(BaseModel):
    name : str
    email: EmailStr
    age: int = Field(gt = 0,le= 100)
    weight:float
    married : Optional[bool] =None
    allergies : List[str]
    contact: Dict[str,str]
    disease : str

    @field_validator('email')
    @classmethod 
    def email_validator(cls,value): #cls->class and value -> value of field here email
        valid_domains = ['gmail.com','hotmail.com','yahoo.com']

        # example: abc@gmail.com
        domain_name = value.split('@')[-1] #-> @gmail.com
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domains')
        
        return value
    

    
    @field_validator('name','disease')
    @classmethod
    def capitalize_transform (cls,value):
        return value.upper()

# 3.dual mode of field_validator
# mode = after(default) :value (value's datatype) receive in the field_validator after type coercion
# mode = before : value(datatype) receive before type coercion in the field_validator 

    @field_validator('age',mode= 'before')
    @classmethod
    def age_check(cls,value):
        # it raises error as the age is given in string format  and not coerce to the int datatype as mode is before
        if type(value) == int:
            return value
        else:
            value = int(value)
            return value # -> explicitly type conversion is needed to avoid the error
        # we can use field validator in default mode means after mode
            raise ValueError('please give proper datatype here int ')






def insert_patient_details(patient:Patient):
    print(patient.email)
    print(patient.name)
    print(patient.disease)




# date comes raw
patient_details ={
    'name':'abcde',
    'age':'20',
    'weight':60.5,
    'allergies':['dust','pollen'],
    'contact' : {'address' : 'pqr road'},
    'email': 'xyz@gmail.com',
    'disease' : 'cough'
}

# making pydantic object out of raw data
patient = Patient(**patient_details) # validation perform in this step -> type coercion also if needed


insert_patient_details(patient)