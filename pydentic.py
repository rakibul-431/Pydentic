#import necessary library
from pydantic import BaseModel
from typing import List,Dict

# Define a pydantic model for patient data
class PatientData(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

# Insert patient data into the database
def insert_patient_data(patient :  PatientData):
    print(patient.name)
    print(patient.age)
    print("insert value")
patient_info ={'name' : "Rakibul", 'age' : 25, 'weight': 57.5 , 'married' : False, 'allergies':['bangladesh','Pakistan'],'contact_details':{'email':"rakibulisal@gmail.com",'phone':"019550069"}}
patient1=PatientData(**patient_info)
insert_patient_data(patient1)