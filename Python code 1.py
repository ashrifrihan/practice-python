#define a class
class bike:
    name = ""
    gear = 0
    
# create object of class
bike1 = bike()

# access attributes and assign new variables
bike1.gear = 11
bike1.name = "montains bike"

print (f"name: {bike1.name},Gears: {bike1.gear}")