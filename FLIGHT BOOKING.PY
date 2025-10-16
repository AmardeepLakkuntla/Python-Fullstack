flights = {
   "AI101": {
         "route": "Delhi → Mumbai",
         "seats": 5, 
         "price": 4500
      },
   "AI102": {
       "route": "Delhi → Bangalore", 
       "seats": 3, 
       "price": 6500
       },
   "AI103": {
       "route": "Mumbai → Chennai",
         "seats": 2, 
         "price": 7000
         },
}

bookings = []

def book_flight(user_choice, sn,payment):
   selected_flight = flights.get(user_choice)
   if selected_flight['seats'] >= sn:
      selected_flight['seats'] = selected_flight['seats'] - sn
      selected_flight["booked"]=sn
      bookings.append(selected_flight)
      print(f'Booking is successful for {user_choice}\n  Your price is {selected_flight["price"] *sn}')
   else:
      print('No Seats')
     

def main():
    
   while True:
      print('-' * 20)
      print('1. Show Flights')
      print('2. Book Flight')
      print('3. View Bookings')
      print('4. Exit')

      choice = input('Choose an option:')
      print('-' * 20)
      
      if choice == '1':
         print(flights)
      elif choice == '2':
         fn = input('Enter flight number:')
         sn=int(input("enter the no of seats: "))
         payment=(input("enter the payment mode: "))
         if payment=="yes":
            print("payment done:")
            book_flight(fn,sn,payment)
         # elif payment=="no":
         #    print("please complete payment: ")
         else:
            print("payment is failed please try again")
            
         # book_flight(fn,sn,payment)
      elif choice == '3':
         print(bookings)
      elif choice == '4':
         print('Bye')
         break
      else:
         print('Invalid option')



if __name__ == '__main__':
    main()