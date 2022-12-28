from re import match
from requests import get

def is_price_input_valid(price: str) -> bool:
    check = match(r"(([0-9]*)$|([0-9]*)[,.]([0-9]){1,2})", price)
    return True if check else False

def is_metal_input_valid(value: str) -> bool:
    check = match(r"^0[.,]([0-9]){2,3}$", value)
    return True if check else False

# Use Backpack.tf API to pull updated key and ref metal prices
def request_currency_values():
    return get('https://backpack.tf/api/IGetCurrencies/v1?key=63ac861d8e93da2b95081cb4')

def get_new_prices():
    data = request_currency_values().json()
    key_value = data['response']['currencies']['keys']['price']
    metal_value = data['response']['currencies']['metal']['price']
    return ((key_value['value'], key_value['value_high']), (metal_value['value'], metal_value['value_high']))