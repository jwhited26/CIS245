# Display a welcome message for your program
print("This program will tell you how long it will take for an amount of money to double given a certain interest rate.")

#Get the annualized interest rate and initial investment from user
rate = float(input("Please enter the annualized interest rate as a whole number:"))
investment = int(input("Please enter the amount of the initial investment:"))

#setting variables for calculation
years = 0
value = investment

#add up investment interest and count years
while value <= investment*2:
  value = value + value*(rate/100)
  years = years + 1

print("It will take ",years," years for this investment to double.")

