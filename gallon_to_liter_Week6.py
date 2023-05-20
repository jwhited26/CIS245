#Modified program that converts gallons to liters

def main():
    #Display introduction
    intro()

    try:
  #Get number of gallons from user
      gallons_needed = int(input('Enter the number of gallons: '))

  #Convert gallons to liters
      gallons_to_liters(gallons_needed)

    except:
      print("It seems you entered an invalid character. Please enter only numeric values")
      print()
      main()

  #Function to display introduction
def intro():
    print('This program converts measurements')
    print('from gallons to liters.')
    print('For your reference the formula is:')
    print(' 1 gallon = 3.78541 liters')
    print()

  #gallons_to_liters function accepts a number of gallons and displays equivalent liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    print('That converts to', liters, 'liters.')

  #Call main function
main()

