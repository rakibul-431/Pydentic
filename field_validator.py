#import necessary library
from pydantic import BaseModel,EmailStr,AnyUrl,field_validator
from typing import List,Dict

# Define a pydantic model for patient data
class PatientData(BaseModel):
    name : str
    age : int
    email: EmailStr
    linkedin: AnyUrl
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]
   
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        # abd@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f'Not a Valid email domain')
        return value



# Insert patient data into the database
def insert_patient_data(patient :  PatientData):
    print(patient.name)
    print(patient.age)
    print("insert value")

patient_info ={'name' : "Rakibul", 'age' : 25}
patient_info ={'name' : "Rakibul", 'age' : 25,'email':'rakibul@hdfc.com','linkedin':'https://rakibul.com/','weight': 57.5 , 'married' : False, 'allergies':['bangladesh','Pakistan'],'contact_details':{'email':"rakibulisal@gmail.com",'phone':"019550069"}}
patient1=PatientData(**patient_info)
insert_patient_data(patient1)