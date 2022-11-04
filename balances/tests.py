from django.test import TestCase

# Create your tests here.

# from pycbrf import ExchangeRates, Banks
#
#
# rates = ExchangeRates('2022-10-25', locale_en=True)
#
# print(rates.date_requested)  # 2016-06-26 00:00:00
# print(rates.date_received)  # 2016-06-25 00:00:00
# print(rates.dates_match)  # False
# # Note: 26th of June was a holiday, data is taken from the 25th.
#
# # Various indexing is supported:
# print(rates['USD'].name)  # US Dollar
# print(rates['R01235'].name)  # US Dollar
# print(rates['840'].name) # US Dollar
# print(rates["USD"])

import requests

# response = requests.get("https://www.nbrb.by/api/exrates/rates/RUB?parammode=2")
# response = response.json()
# print(response.get("Cur_OfficialRate", "Empty"))

response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
response = response.json()
print(response)
response = [
    (
        i.get("Cur_Name"),
        i.get("Cur_Abbreviation"),
    )
    for i in response
]
print(response)
