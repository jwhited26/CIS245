#Establish stock dictionary
stock_dict = {
  "AMZN": "105.45",
  "TSLA": "164.31",
  "BA": "206.78",
  "IBM": "126.41",
  "MSFT": "307.26",
  "NKE": "126.72",
  "CAT": "218.8",
  "KO": "64.15",
  "MMM": "106.22",
  "AAPL": "169.68"
}

while True:
  
  #Prompt user for stock symbol
  stock_symbol = input("Please enter a stock symbol to see the current price:")

  #Get stock price and return message if         stock not found
  stock_price = stock_dict.get(stock_symbol,    'Stock not found. Please make sure to type the symbol in all CAPS, and you are entering one of the following stocks: AMZN, TSLA, BA, IBM, MSFT, NKE, CAT, KO, MMM, OR AAPL.')
  print (stock_price)

  try_again = int(input("Press 1 to try again, 0 to exit. "))
  if try_again == 0:
    break