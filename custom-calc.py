# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the description. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

print("\n")
print("In order to calculate your remaining balance after the purchase\nof a vehicle, we need some information:\n")
input_cost = float(input("What is the purchase price of your vehicle? "))
input_currentBalance = float(input("What is your current cash balance? "))
input_tax = (float(input("What is your state sales tax? ")) / 10) / 10

def vehicle_cost_plus_tax(cost, tax):
    return cost + (cost * tax)

costPlusTax = vehicle_cost_plus_tax(input_cost, input_tax)
remainingBalance = input_currentBalance - costPlusTax

print(f"When purchasing a vehicle at a cost of ${costPlusTax} after tax, your remaining cash balance will be ${remainingBalance}")

