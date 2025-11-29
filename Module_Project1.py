#!/usr/bin/env python
# coding: utf-8

# # PART 3 – FUNCTIONS AND CLASSES

# In[3]:


#Parent Class & Function
class Passenger:
    def __init__(self, firstname, lastname, passport, destination):
        self.name = f"{firstname} {lastname}"
        self.passport = passport
        self.destination = destination
 
    def display_info(self):
        return f"Name: {self.name.upper()}, Passport: {self.passport.upper()}, Destination: {self.destination.upper()}"
 
    def passenger_type(self):
        return "Regular Passenger"
 

# Inheritance
class EconomyPassenger(Passenger):
    def __init__(self, firstname, lastname, passport, destination, baggage_allowance):
        super().__init__(firstname, lastname, passport, destination)
        self.baggage_allowance = baggage_allowance
 
    def passenger_type(self):
        return "Economy Class"
 
    def display_info(self):
        base_info = super().display_info()   #to call out the parent class
        return f"{base_info}, Baggage Allowance: {self.baggage_allowance}kg"
 
 
class BusinessPassenger(Passenger):
    def __init__(self, firstname, lastname, passport, destination, lounge_access, meal_type):
        super().__init__(firstname, lastname, passport, destination)
        self.lounge_access = lounge_access
        self.meal_type = meal_type
 
    def passenger_type(self):
        return "Business Class"
 
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Lounge Access: {self.lounge_access}, Meal: {self.meal_type}"
 
 
# Testing instances
 
# print("=== ECONOMY PASSENGERS ===")
# economy_passengers = [
#     EconomyPassenger("Aiman", "Bin Hassan", "A123456", "Tokyo", 20),
#     EconomyPassenger("Sara", "Binti Ab Rahman", "A234567", "Seoul", 25),
#     EconomyPassenger("David", "White", "A345678", "Danang", 20),
#     EconomyPassenger("Katherine", "Yen", "A456789", "Jakarta", 25),
#     EconomyPassenger("Pei Hwa", "Lee", "A567899", "Taipei", 20)
# ]
 
# for p in economy_passengers:
#     print(p.display_info(), "| Type:", p.passenger_type())
 
# print("\n=== BUSINESS PASSENGERS ===")
# business_passengers = [
#     BusinessPassenger("Anna", "Liu", "A562489", "London", "Yes", "Vegan"),
#     BusinessPassenger("Rahman", "Ali", "A623953", "Dubai", "Yes", "Seafood"),
#     BusinessPassenger("Kim", "Low", "A395835", "Paris", "Yes", "Vegetarian"),
#     BusinessPassenger("Siti", "Binti Ahmad", "A739145", "Istanbul", "Yes", "Halal"),
#     BusinessPassenger("Bernard", "Teng", "A132980", "Frankfurt", "Yes", "Standard")
# ]
 
# for p in business_passengers:
#     print(p.display_info(), "| Type:", p.passenger_type())
 


# In[4]:


# === Interactive Input ===
print("=== ENTER PASSENGER DETAILS ===")
firstname = input("First Name: ")
lastname = input("Last Name: ")
passport = input("Passport Number: ")
destination = input("Destination: ")
ticket_type = input("Ticket Type (Economy/Business): ")

if ticket_type.lower() == "economy":
    baggage = int(input("Baggage Allowance (kg): "))
    passenger = EconomyPassenger(firstname, lastname, passport, destination, baggage)

elif ticket_type.lower() == "business":
    lounge = input("Lounge Access (Yes/No): ")
    meal = input("Meal Preference: ")
    passenger = BusinessPassenger(firstname, lastname, passport, destination, lounge, meal)

else:
    passenger = Passenger(firstname, lastname, passport, destination)

# Display result
print("\n=== PASSENGER INFO ===")
print(passenger.display_info(), "| Type:", passenger.passenger_type())


# In[ ]:




