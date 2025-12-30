#import necessary library
from pydantic import BaseModel,EmailStr,AnyUrl,field_validator,model_validator
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
   
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age < 18 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients under 18')
        return model

# Insert patient data into the database
def insert_patient_data(patient :  PatientData):
    print(patient.name)
    print(patient.age)
    print("insert value")

patient_info ={'name' : "Rakibul", 'age' : 25}
patient_info ={'name' : "Rakibul", 'age' : 25,'email':'rakibul@hdfc.com','linkedin':'https://rakibul.com/','weight': 57.5 , 'married' : False, 'allergies':['bangladesh','Pakistan'],'contact_details':{'email':"rakibulisal@gmail.com",'phone':"019550069",'emergency_contact':'0193445'}}
patient1=PatientData(**patient_info)
insert_patient_data(patient1)