from re import match

def is_price_input_valid(price: str) -> bool:
    check = match(r"(([0-9]*)$|([0-9]*)[,.]([0-9]){1,2})", price)
    return True if check else False

def is_metal_input_valid(value: str) -> bool:
    check = match(r"^0[.,]([0-9]){2,3}$", value)
    return True if check else False