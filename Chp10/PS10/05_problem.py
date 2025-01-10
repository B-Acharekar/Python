# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint
class train:

    def __init__(self, train_number):
        self.train_number = train_number


    def book_ticket(self,source,destination):
        print (f"Ticket is booked in train no: {self.train_number}\nfrom {source} to {destination}")
    def get_status(self):
        print (f"Train no: {self.train_number} is running on time")
    def get_fare(self,source,destination):
        print (f"Fare for travel from {source} to {destination} is {randint(255,4599)}")


t = train(1112)
t.book_ticket("Thane","Madgoan")
t.get_status()
t.get_fare("Thane","Madgoan")
