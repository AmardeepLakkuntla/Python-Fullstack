from docters import *

bookedappointments=[
    {
        
    }]

def book_a_appointment(booked_id,patient_name,docter_id,doctor_name,available_date,available_time):
    bookedappointments.append(
        {
            'booked_id':booked_id,
            'patient_name':patient_name,
            'docter_id':docter_id,
            'doctor_name': doctor_name,
            'available_date':available_date,
            'available_time':available_time
            
        }
                               )
def delete_booked_appointment(booked_id):
    target = str(booked_id)     # normalize to string for comparison
    for idx, ba in enumerate(bookedappointments):
        if str(ba.get('booked_id', '')) == target:
            del bookedappointments[idx]
            print("Appointment deleted successfully!")
            return True
    print("Appointment not found")
    return False
    
def get_all_bookedappointments():
    return bookedappointments