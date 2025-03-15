import pandas

df = pandas.read_csv("hotels.csv",dtype={"id":str})
df_cards = pandas.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_secure_cards = pandas.read_csv("card_security.csv",dtype=str)


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

class CreditCard(): #Parent class

    def __init__(self,number):
        self.number = number

    def validate(self,expiration,holder,cvc):
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "cvc": cvc,
                     "holder": holder
                     }
        if card_data in df_cards:
            return True

        return False

class SecureCreditCard(CreditCard): #This is the child class or inherited class from parent class CreditCard

    def authenticate(self,given_password):
        password = df_secure_cards.loc[df_secure_cards["number"]== self.number,"password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

print(df)
print(df_cards)

hotel_ID = input("Enter the id of hotel you wanna book: ")
hotel = Hotels(hotel_ID)


if hotel.available():
    creditcard = SecureCreditCard(number="1234567890123456")
    if creditcard.validate(expiration="12/26", cvc="252",holder="Misha" ):
        if creditcard.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name,
                                                   hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit Card Authentication failed")
    else:
        print("There is some issue with your payment!!!")
else:
    print("Sorry,Hotel is not available/free!!!!")