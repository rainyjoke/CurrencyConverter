# final stage
import requests
import json

my_currency = input().lower()

link = "http://www.floatrates.com/daily/"+my_currency+".json"
req = requests.get(link)
data = json.loads(req.text)
cache={}

if my_currency != 'usd':
    cache['usd'] = data['usd']['rate']
if my_currency != 'eur':
    cache['eur'] = data['eur']['rate']

def get_rate(curr):
    return data[curr]['rate']

def add_to_cache(curr, rate):
    cache[curr] = rate

def check_cache(curr, dict):
    print("Checking the cache...")
    if curr in dict:
        print("Oh! It is in the cache!")
        return True

    print("Sorry, but it is not in the cache!")
    return False

def result(curr, amount):
    if check_cache(curr, cache)==True:
        result = cache[curr]*amount

    else:
        rate = get_rate(curr)
        add_to_cache(curr, rate)
        result = amount * rate
    return result

def main():
    while exchange_curr := input().lower():
        amount = float(input())
        print(f"You received {result(exchange_curr, amount)} {exchange_curr.upper()}.")

main()






