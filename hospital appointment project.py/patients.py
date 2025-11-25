patients=[
    {
        'id': 1,
        'patient_name': 'shiva',
        'contact': 9492476759
    
    },
    {
        'id': 2,
        'patient_name': 'veera',
        'contact': 9492476758
    }
    ]

def add_patient(id,patient_name,contact):
    patients.append(
        {
        'id': id,
        'patient_name': patient_name,
        'contact': contact
        }
                    )

def delete_patient(id):
    for patient in patients:
        if patient['id']==id:
            patients.remove(patient)
            print("patient deleted successfully: ")
        return
    print("patient not found")
            
    
    
def get_patients():
    return patients