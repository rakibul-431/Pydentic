#import necessary library
from pydantic import BaseModel,AnyUrl,Field,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated

# Define a pydantic model for patient data
class PatientData(BaseModel):
    name : Annotated[str, Field(max_length=50,title="patient name",description='Give the patient full name withing 50 characters',example=['Rakibul islam','Noyon Ahmed'])]
    age : Annotated[int, Field(gt=0,lt=150, description='Age in years',examples=['25','30'])]
    email: Annotated[EmailStr, Field(default=None,description="Email address of the patient",examples='rakibul@gmail.com')]
    linkedin: Annotated[AnyUrl, Field(default=None,description="Linkedin profile Url of the patient")]
    weight : Annotated[float, Field(gt=0 ,lt=500, description='Weight in Kg')]
    married : Annotated[bool, Field(description='Marital status of the patient')]
    allergies :Annotated[Optional[list[str]],Field(default=None,description="List of allergies the patient has")]
    contact_details : Annotated[Dict,Field(description="Contact details of the patient including email and phone number")]

# Insert patient data into the database
def insert_patient_data(patient :  PatientData):
    print(patient.name)
    print(patient.age)
    print("insert value")
patient_info ={'name' : "Rakibul", 'age' : 25,'email':'rakibul@gmail.com','linkedin':'https://rakibul.com/','weight': 57.5 , 'married' : False, 'allergies':['bangladesh','Pakistan'],'contact_details':{'email':"rakibulisal@gmail.com",'phone':"019550069"}}
patient1=PatientData(**patient_info)
insert_patient_data(patient1)