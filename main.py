import pandas

df = pandas.read_csv("hotels.csv",dtype={"id":str})

class Hotels:

    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"]==self.hotel_id,"name"].squeeze()

    def available(self):
        """ Check if the hotel is available """
        availability = df.loc[df["id"]== self.hotel_id,"available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book a hotel by changing its availability to no """
        availability = df.loc[df["id"]== self.hotel_id,"available"] ="no"
        df.to_csv(path_or_buf="hotels.csv",index=False)



class ReservationTicket:

     def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
     def generate(self):
         content = f"""
         Thank you for your reservation!!
         Here are your booking data:
         Name : {self.customer_name}
         Hotel Name : {self.hotel.name}
         """
         return content

print(df)

hotel_ID = input("Enter the id of hotel you wanna book: ")
hotel = Hotels(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Sorry,Hotel is not available/free!!!!")