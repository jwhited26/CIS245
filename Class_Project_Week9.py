# Class Project - Create an application that interacts with a web service
# in order to obtain data. Your program will use all of the information you’ve 
# learned in the class in order to create a useful application. Your program must 
# prompt the user for their city or zip code and request weather forecast data from
# openweathermap.org. Your program must display the weather information in a READABLE 
# format to the user.

import requests

# Make calls to operweathermap.org website and request data

def get_web_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    appid = "896a7d4dff0a49f069b223124f86bf5b" #My API key

    # Ask user to supply a zip or city name
    if zip is not None:
        baseUrl += "&zip="+str(zip)+",us"
    else:
        baseUrl += "&q="+str(city)+",us"
    # API ID at end of string 
    baseUrl += "&appid="+str(appid)
    # Call requests library
    r = requests.get(baseUrl)
    # Response
    return r

# Display weather data to user

def display(resp):
    # For a successful request, code is 200, else return error
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} Weather Forecast:
        Condition: {data['weather'][0]['description']}
        Wind:  {data['wind']['speed']} miles/hr
        Low Temp: {data['main']['temp_min']} F
        High Temp: {data['main']['temp_max']} F
        """)
    else:
        print("Request Failed. Please try a different zip or city: ", resp.status_code)

def main():
    while True:
        # Ask user if search by zip or city is wanted
        choice = int(
            input("How would you like to search? :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if choice == 1:
            try:
                # User inputs zip
                zCode = int(input("Enter zip code: "))
                # Get data from site
                resp = get_web_data(zCode, None)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 2:
            try:
				# User inputs city name
                city_name = input("Enter city name: ")
                # Get data from site
                resp = get_web_data(None, city_name)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 3:
            break
        else:
            print("Please type a 1, 2, or 3 as your choice.\n")

if __name__ == "__main__":
    main()