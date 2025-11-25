from docters import *
from patients import *
from bookedappointments import *

def show_menu():
    print('''
             1.add a doctor
             2.add a patient
             3.book appointment
             4.show all doctors 
             5.show all patients
             6.show all booked appointments
             7.delete a doctor
             8.delete a patient
             9.delete a appointment
             10.exit
              ''')
    
def main():
      
      while True:
          show_menu()
          choice=input('enter the choice:')
          
          if choice=='1':
              docter_id=int(input('enter doctor id:'))
              name=input('enter doctor name:')
              contact=int(input('enter contact number:' ))
              available_date=(input('enter available date:'))
              available_time=(input('enter doctor available time:'))
              add_docter(docter_id,name,contact,available_date,available_time)
              print("docter added successfully: ")
          elif choice=='2':
              patient_id=int(input('enter patient id:'))
              patient_name=input('enter patient name:')
              contact=int(input('enter contact number:' ))
              add_patient(patient_id,patient_name,contact)
              print("patient added successfully: ")
          elif choice=='3':
              booked_id=int(input("enter booking id:"))
              patient_name=input('enter patient name:')
              docter_id=int(input('enter doctor id:'))
              docter_name=input('enter doctor name:')
              book_a_date=input("enter the date: ")
              book_a_time=input("enter the time: ")
            #   if book_a_date==docter_name["available_date"]:
            #     if book_a_time==docter_name["available_time"]: 
              book_a_appointment(booked_id,patient_name,docter_id,docter_name,book_a_date,book_a_time)
              print('booked appointment successfully:')
            #     else:
            #       print('docter not available at this date: ')
            #   else:
            #       print("docter not available at this time:")
          elif choice=='4':
              show_all_doctrs=get_doctors()
              print(show_all_doctrs)
          elif choice=='5':
              show_all_patients=get_patients()
              print(show_all_patients)
          elif choice=='6':
              show_all_booked_appointments=get_all_bookedappointments()
              print(show_all_booked_appointments)
          elif choice=='7':
              docter_id=int(input("enter docter id to delete: "))
              delete_docter(docter_id)
          elif choice=='8':
              id=int(input("enter patient id to delete:"))
              delete_patient(id)
          elif choice=='9':
              booked_id=int(input("enter booked appointment id to delete:"))
              delete_booked_appointment(booked_id)
          elif choice == '10':
            print("Exiting !!!")
            break
 
          else:
            print("Invalid Option!")
          
          
              
              
              
    
                  
                  
              
              
              
              
              
          




if __name__ == '__main__':
    main()