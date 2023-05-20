# Display a welcome message for your program
print("Welcome to the super fantastic cable cost calculator program!")

#Get the company name from the user
business = input("Please enter your company name:")

#Get the number of feet of fiber optic to be installed from the user
feet_of_cable = input("Please enter amount of cable in feet:")

#Cast length of cable as int and calculate cost for varying lengths using if-elif-else
feet_of_cable = float(feet_of_cable)
if feet_of_cable < 101:
  total_cost_cable = feet_of_cable * .87
elif feet_of_cable < 251:
  total_cost_cable = feet_of_cable * .80
elif feet_of_cable < 501:
  total_cost_cable = feet_of_cable * .70
else:
  total_cost_cable = feet_of_cable * .5

#Display the calculated information and company name
message = "The total cost is: " + str(total_cost_cable) + ". Thank you " + str(business_name) + "!"
print(message)