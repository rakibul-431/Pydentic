#import necessary library
from pydantic import BaseModel

# Define a pydantic model for patient data
class PatientData(BaseModel):
    name : str
    age : int

# Insert patient data into the database
def insert_patient_data(patient :  PatientData):
    print(patient.name)
    print(patient.age)
    print("insert value")
patient_info ={'name' : "Rakibul", 'age' : 25}
patient1=PatientData(**patient_info)
insert_patient_data(patient1)