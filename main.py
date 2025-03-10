import pandas

df = pandas.read_csv("hotels.csv")

class Hotels:
    def __init__(self,id):
        pass

    def book(self,id):
        pass

    def available(self):
        pass

class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        pass
     def generate(self):
         pass

print(df)

id = input("Enter the id of hotel you wanna book: ")

hotel = Hotels(id)
if hotel.available():
    hotel.book()
    name = "Enter your name"
    reservation_ticket = ReservationTicket(name,hotel)
    reservation_ticket.generate()
else:
    print("Sorry,Hotel is not available/free!!!!")