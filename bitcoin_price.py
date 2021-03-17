import requests
from pprint import pprint

def api_call():
  url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

  try:

      response = requests.get(url)
      data = response.json()
      pprint(data)
      return data
  except Exception as e:
      print('There was an error contacting the API' + e)

def main():
  data = api_call()
  bitcoin = user_input()
  bitcoin_value = get_exchange_rate(data, bitcoin)
  display_exchange_rate(bitcoin, bitcoin_value)

def user_input():
  bitcoin = float(input('Enter the number of bitcoin: '))
  return bitcoin

def get_exchange_rate(data, bitcoin):
  dollars_exchange_rate = data['bpi']['USD']['rate_float']
  bitcoin_value = bitcoin * dollars_exchange_rate
  return bitcoin_value


def display_exchange_rate(bitcoin, bitcoin_value):
  print(f'{bitcoin} Bitcoin is worth ${bitcoin_value}')

if __name__ == '__main__':
  main()