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
import json
params = {
    "ondate": "2022-10-26",
}
response = requests.get("https://www.nbrb.by/api/exrates/rates", params=params)
# response = response.json()
print(type(response.json()))
print(response[65].get(""))
# print(response[0]['Cur_ID'])
