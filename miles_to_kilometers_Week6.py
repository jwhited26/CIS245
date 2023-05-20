#Program that converts miles to kilometers

def main():
    #Display intro
    intro()

  #Function for intro prompt
def intro():
    print('Greetings and salutations!')
    print('Welcome to the Kilo Kalculator!')
    print('')
    print('This program will convert miles to kilometers.')
    print('For your reference the formula is:')
    print(' 1 mile = 1.60934 kilometers')
    print()

    try:
  #Prompt user for number of miles driven
      miles_needed = int(input('Enter the number of miles driven: '))

  #Convert miles to kilometers
      miles_to_kilometers(miles_needed)

    except:
      print('Uh oh! It seems something went wrong.')
      print('An invalid character has been entered. Please enter only numeric values.')
      print()
      main()

  #miles_to_kilometers function accepts a number of miles and displays equivalent kilometers
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    print('')
    print('If you drive',miles, 'miles, that equals',kilometers, 'kilometers.')
    print('Thank you, and drive safe!')

  #Call main function
main()