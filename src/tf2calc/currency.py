from utils import get_new_prices

prices = get_new_prices()

refmetal_usd_value = prices[1][1]
currency_value =    {
                        "Key": prices[0][1],
                        "RefinedMetal": 1.0,
                        "ReclaimedMetal": 0.33333,
                        "ScrapMetal": 0.11111,
                        "Weapon": 0.0555
                    }


# A single currency item from the 'currency_value' dict
class CurrencyItem:
    def __init__(self, name, count=0):
        if name in currency_value.keys():
            self.name = name
            self.count = count
            self.value = currency_value[self.name]
        else:
            raise Exception("Currency name is not inside 'currency_value' dictionary!")

    def total_value(self) -> float:
        return self.count * self.value

    def __repr__(self):
        return self.name
    # return f"[x{self.count}] {self.name} - ({self.total_value()} ref)"



# This class holds and manages all currency items defined by currency_value dictionary
class CurrencyContainer:
    def __init__(self):
        self.currency_items: list[CurrencyItem] = []
        for item in currency_value.keys():
            self.add_currency(CurrencyItem(item))

    def update_currencies(self):
        refmetal_usd_value

    def add_currency(self, item_to_add: CurrencyItem):
        if item_to_add not in self.currency_items:
            self.currency_items.append(item_to_add)

    def get_currency_item(self, name: str):
        for item in self.currency_items:
            if item.name == name:
                return item
        return None

    def change_item_amount(self, item_name:str, new_amount: int) -> bool:
        for item in self.currency_items:
            if item.name == item_name:
                item.count = new_amount
                return True
        return False

    def price_to_currency(self, price: float, window_ref):
        remaining = price
        if window_ref.KeyItemFrame.Toggled.get():
            remaining = self.value_to_key(price)[0]
        if window_ref.RefItemFrame.Toggled.get():
            remaining = self.value_to_ref(remaining)[0]
        if window_ref.RecItemFrame.Toggled.get():
            remaining = round(self.value_to_rec(remaining)[0], 2)
        if window_ref.ScrapItemFrame.Toggled.get():
            remaining = self.value_to_scrap(remaining)[0]
        if window_ref.WeaponItemFrame.Toggled.get():
            if not any([window_ref.KeyItemFrame.Toggled.get(),
                 window_ref.RefItemFrame.Toggled.get(),
                 window_ref.RecItemFrame.Toggled.get(),
                 window_ref.ScrapItemFrame.Toggled.get()]):
                self.value_to_wep_solo(remaining)
            else:
                self.value_to_wep(remaining)
        window_ref.update_item_count()

    def value_to_key(self, value: float) -> (float, float):
        new_key_amount = 0
        if value >= currency_value["Key"]:
            new_key_amount = int(value / currency_value["Key"])
        self.change_item_amount("Key", new_key_amount)
        return (value - (new_key_amount * currency_value["Key"]), new_key_amount)

    def value_to_ref(self, value: float) -> (float, float):
        new_ref_amount = int(value) if value >= 1.0 else 0.0
        self.change_item_amount("RefinedMetal", new_ref_amount)
        return (value - new_ref_amount, new_ref_amount)

    def value_to_rec(self, value: float) -> (float, float):
        value = round(value,2)
        new_rec_amount = int((value * 100) / 33) if value >= 0.33 else 0.0
        self.change_item_amount("ReclaimedMetal", new_rec_amount)
        return ((value * 100 % 33) * 0.01, new_rec_amount)

    def value_to_scrap(self, value: float) -> (float, float):
        new_scrap_amount = int((value * 100) / 11) if value >= 0.11 else 0.0
        self.change_item_amount("ScrapMetal", new_scrap_amount)
        return ((value * 100 % 11) * 0.01, new_scrap_amount)

    def value_to_wep(self, value: float) -> (float, float):
        new_wep_amount = int((value * 100) / 5) if value >= 0.05 else 0.0
        self.change_item_amount("Weapon", new_wep_amount)
        return ((value * 100 % 5) * 0.01, new_wep_amount)

    def value_to_wep_solo(self, value: float) -> (float, float):
        new_wep_amount = int((value * 100) / 5.5555) if value >= 0.05 else 0.0
        self.change_item_amount("Weapon", new_wep_amount)
        return ((value * 100 % 5) * 0.01, new_wep_amount)

    def items_to_value(self) -> float:
        total = str(self.get_total_value())
        return float(total[0:len(total)-1:1])

    def get_total_value(self) -> float:
        total = sum([item.value * item.count for item in self.currency_items])
        return round(total, 3)