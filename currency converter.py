import requests

class CurrencyCon():

    rates  = {}                                                                # empty dictionary to store rates

    def __init__(self,url):
        data = requests.get(url).json()
        self.rates = data['rates']                                             # Getting only rates data from json data

    def convert(self,from_curr,to_curr,amount):                                # Function to carry out the main operation
        initial_amount = amount
        if from_curr != 'EUR':                                                 # Because the exchange rate for EUR is 1
            amount = amount / self.rates[from_curr]

        final_amount = round(amount*self.rates[to_curr],2)                     # Converting the currency and setting the value upto 2 decimal places
        print(initial_amount,from_curr,':',final_amount,to_curr)

if __name__=='__main__':   # Driver code
    YOUR_ACCESS_KEY = 'bf714bb4c815eeb79ce30d645600bffc'                       # Access key from fixer.io ( different for every individual )

    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)

    x = CurrencyCon(url)                                                       # Call for class

    from_ = input('From : ').upper()

    to_ = input('To : ').upper()

    amount = int(input('Enter amount : '))

    x.convert(from_, to_, amount)                                               # Call for method
