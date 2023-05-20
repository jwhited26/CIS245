# Display a welcome message for your program
print("Welcome to the fantastic cable cost calculator program!")

#Get the company name from the user
company_name = input("Please enter your company name:")

#Get the number of feet of fiber optic to be installed from the user
feet_of_cable = input("Please enter amount of cable in feet:")

#Cast length of cable as int and multiply for total cost
feet_of_cable = float(feet_of_cable)
total_cost_cable = feet_of_cable * .87

#Display the calculated information and company name
message = "The total cost is: " + str(total_cost_cable) + ". Thank you " + str(company_name) + "!"
print(message)