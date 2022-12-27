from tkinter import *
from PIL import Image, ImageTk

from currency import currency_value, refmetal_usd_value
from utils import is_price_input_valid, is_metal_input_valid



# ----- Variables -----

MAINGRAY_BG = "#3d3735"
LIGHTERGRAY_BG = "#332d2b"
LIGHTGRAY_BG = "#615b59"



# ----- Widgets -----

# Creates a GUI widget on initialization
class MainWindow():
    def __init__(self, currency_container):
        # Create a GUI window
        self.root = Tk()
        self.root.title("TF2 Metal Calculator")
        self.root.geometry("550x360")
        self.root.resizable(False, False)
        self.currency_container = currency_container

        # ----- Icons -----

        KEY_ICON = Image.open('../img/key_icon.png')
        KEY_ICON_60x60 = ImageTk.PhotoImage(KEY_ICON.resize((48, 48)))
        KEY_ICON = ImageTk.PhotoImage(KEY_ICON.resize((40, 40)))

        REFMETAL_ICON = Image.open('../img/refined_metal_icon.png')
        REFMETAL_ICON_60x60 = ImageTk.PhotoImage(REFMETAL_ICON.resize((60, 60)))
        REFMETAL_ICON = ImageTk.PhotoImage(REFMETAL_ICON.resize((40, 40)))

        RECMETAL_ICON = Image.open('../img/reclaimed_metal_icon.png')
        RECMETAL_ICON_60x60 = ImageTk.PhotoImage(RECMETAL_ICON.resize((60, 60)))

        SCRAPMETAL_ICON = Image.open('../img/scrap_metal_icon.png')
        SCRAPMETAL_ICON_60x60 = ImageTk.PhotoImage(SCRAPMETAL_ICON.resize((60, 60)))

        WEAPON_ICON = Image.open('../img/weapon_icon.png')
        WEAPON_ICON_60x60 = ImageTk.PhotoImage(WEAPON_ICON.resize((60, 60)))

        NAMETAG_ICON = Image.open('../img/nametag_icon.png')
        NAMETAG_ICON = ImageTk.PhotoImage(NAMETAG_ICON.resize((128, 128)))

        RIGHT_ICON = Image.open('../img/icons8_right.png')
        RIGHT_ICON = ImageTk.PhotoImage(RIGHT_ICON.resize((25, 25)))

        LEFT_ICON = Image.open('../img/icons8_left.png')
        LEFT_ICON = ImageTk.PhotoImage(LEFT_ICON.resize((25, 25)))

        RESYNC_ICON = Image.open('../img/icons8_sync.png')
        RESYNC_ICON = ImageTk.PhotoImage(RESYNC_ICON.resize((25, 25)))


        self.root.iconphoto(False, REFMETAL_ICON)
        self.root.config(bg=MAINGRAY_BG)


        # Key/Metal Price
        self.DEFAULT_KEY_PRICE = currency_value['Key']
        self.DEFAULT_METAL_PRICE = refmetal_usd_value

        self.input_key_price = StringVar(self.root)
        self.input_key_price.set(self.DEFAULT_KEY_PRICE)
        self.input_key_price.trace_add("write", self.clamp_key_value)

        self.input_metal_price = StringVar(self.root)
        self.input_metal_price.set(self.DEFAULT_METAL_PRICE)
        self.input_metal_price.trace_add("write", self.clamp_metal_value)

        self.price_input = StringVar(self.root)
        self.price_input.set("0.00")
        self.price_input.trace_add("write", self.clamp_price_input)


        # ----- Widgets -----

        # Main Widget Container
        self.MainFrame = Frame(self.root, bg=MAINGRAY_BG)
        self.MainFrame.pack(fill=X)

        # Top Frame
        self.TopFrame = Frame(self.MainFrame)
        self.TopFrame.grid(row=0, column=0, columnspan=10)
        self.TopFrame.grid(sticky="we")

            # Key Price Frame
        self.KeyPriceFrame = Frame(self.TopFrame, padx=13, bg=LIGHTERGRAY_BG)
        self.KeyPriceFrame.grid(row=0, column=0, columnspan=3)

        self.KeyPriceIcon = Label(self.KeyPriceFrame,
                                  image=KEY_ICON,
                                  width=30,
                                  height=30,
                                  padx=5,
                                  bg=LIGHTERGRAY_BG)
        self.KeyPriceIcon.grid(row=0, column=0)

        self.KeyPriceSpacer = Label(self.KeyPriceFrame, padx=2, bg=LIGHTERGRAY_BG)
        self.KeyPriceSpacer.grid(row=0, column=1)

        self.KeyPriceText = Entry(self.KeyPriceFrame,
                                  justify=CENTER,
                                  width=6,
                                  font=("Arial", 12, "bold"),
                                  bg=LIGHTGRAY_BG,
                                  fg="white",
                                  textvariable=self.input_key_price)
        self.KeyPriceText.grid(row=0, column=2)

        self.KeyPriceRefText = Label(self.KeyPriceFrame,
                                     padx=5,
                                     font=("Arial", 13),
                                     text="ref",
                                     bg=LIGHTERGRAY_BG,
                                     fg="white")
        self.KeyPriceRefText.grid(row=0, column=3)

            # Metal Price Frame
        self.MetalPriceFrame = Frame(self.TopFrame, padx=5, bg=LIGHTERGRAY_BG)
        self.MetalPriceFrame.grid(row=0, column=3, columnspan=2)

        self.MetalPriceIcon = Label(self.MetalPriceFrame,
                                    image=REFMETAL_ICON,
                                    width=30,
                                    height=30,
                                    padx=5,
                                    bg=LIGHTERGRAY_BG)
        self.MetalPriceIcon.grid(row=0, column=0)

        self.MetalPriceSpacer = Label(self.MetalPriceFrame, padx=2, bg=LIGHTERGRAY_BG)
        self.MetalPriceSpacer.grid(row=0, column=1)

        self.MetalPriceText = Entry(self.MetalPriceFrame,
                                    justify=CENTER,
                                    width=6,
                                    font=("Arial", 12, "bold"),
                                    bg=LIGHTGRAY_BG,
                                    fg="white",
                                    textvariable=self.input_metal_price)
        self.MetalPriceText.grid(row=0, column=2)

        self.MetalPriceUSDText = Label(self.MetalPriceFrame,
                                       padx=5,
                                       font=("Arial", 13),
                                       text="$",
                                       bg=LIGHTERGRAY_BG,
                                       fg="white")
        self.MetalPriceUSDText.grid(row=0, column=3)

        self.KeyPriceText.bind('<FocusOut>', self.restore_key_value)
        self.MetalPriceText.bind('<FocusOut>', self.restore_metal_value)

            # Last Update Date Text
        self.LastPriceText = Label(self.MetalPriceFrame,
                                      padx=8,
                                      bg=LIGHTERGRAY_BG,
                                      font=("Arial", 12),
                                      text="[01/12/2022]",
                                      fg="white")
        self.LastPriceText.grid(row=0, column=5)

        # Refresh Key, Metal Price
        self.PriceUpdateButton = Button(self.MetalPriceFrame,
                                   padx=5,
                                   bg=LIGHTGRAY_BG,
                                   font=("Arial", 10, "bold"),
                                   text="UPDATE PRICES",
                                   fg="white", image=RESYNC_ICON, compound=RIGHT)
        self.PriceUpdateButton.grid(row=0, column=6)


        # Bottom Frame

        self.BottomFrame = Frame(self.MainFrame, bg=MAINGRAY_BG, padx=60)
        self.BottomFrame.grid(row=1, column=0, columnspan=10, rowspan=10, sticky="we")

            # Value Frame
        self.ValueFrame = Frame(self.BottomFrame, bg=MAINGRAY_BG)
        self.ValueFrame.grid(row=0, column=0, columnspan=2)

        self.PriceIcon = Label(self.ValueFrame,
                               image=NAMETAG_ICON,
                               bg=MAINGRAY_BG)
        self.PriceIcon.grid(row=0, column=0, columnspan=2)

        self.PriceEntryFrame = Frame(self.ValueFrame, bg=MAINGRAY_BG)
        self.PriceEntryFrame.grid(row=1, column=0, columnspan=2)

        self.PriceEntry = Entry(self.PriceEntryFrame,
                                bg=LIGHTGRAY_BG,
                                fg="white",
                                font=("Arial", 15),
                                width=9,
                                justify=CENTER,
                                textvariable=self.price_input)
        self.PriceEntry.grid(row=0, column=0, columnspan=2)

        self.PriceErrorLabel = Label(self.PriceEntryFrame, justify=CENTER,
                                     bg=MAINGRAY_BG,
                                     fg="#ff1400",
                                     font=("Arial", 10, "bold"),
                                     text="")
        self.PriceErrorLabel.grid(row=1, column=0, columnspan=2)

        self.RefText = Label(self.PriceEntryFrame,
                             bg=MAINGRAY_BG,
                             text="ref",
                             fg="white",
                             padx=5,
                             font=("Arial", 12,"bold"))
        self.RefText.grid(row=0, column=2)

            # Equality Sign
        self.ArrowSignFrame = Frame(self.BottomFrame, bg=MAINGRAY_BG, padx=50)
        self.ArrowSignFrame.grid(row=0, column=2, columnspan=2)

        self.LeftButton = Button(self.ArrowSignFrame,
                                bg=LIGHTERGRAY_BG,
                                image=LEFT_ICON,
                                fg="white",
                                font=("Arial", 15, "bold"),
                                padx=8,
                                command=self.items_to_value)
        self.LeftButton.grid(row=0, column=0)

        self.RightButton = Button(self.ArrowSignFrame,
                                bg=LIGHTERGRAY_BG,
                                image=RIGHT_ICON,
                                fg="white",
                                font=("Arial", 15, "bold"),
                                padx=8,
                                command=self.price_to_currency)
        self.RightButton.grid(row=1, column=0)

            # Item Currency Frame
        self.ItemFrame = Frame(self.BottomFrame, bg=MAINGRAY_BG, pady=10)
        self.ItemFrame.grid(row=0, column=5, columnspan=3)

        self.KeyItemFrame = CurrencyFrame(self.root, self, self.ItemFrame, KEY_ICON_60x60, 0, "Key")
        self.RefItemFrame = CurrencyFrame(self.root, self, self.ItemFrame, REFMETAL_ICON_60x60, 1, "RefinedMetal")
        self.RecItemFrame = CurrencyFrame(self.root, self, self.ItemFrame, RECMETAL_ICON_60x60, 2, "ReclaimedMetal")
        self.ScrapItemFrame = CurrencyFrame(self.root, self, self.ItemFrame, SCRAPMETAL_ICON_60x60, 3, "ScrapMetal")
        self.WeaponItemFrame = CurrencyFrame(self.root, self, self.ItemFrame, WEAPON_ICON_60x60, 4, "Weapon")


        # ----- Main Script -----
        self.root.mainloop()


    # ----- Functions -----

    def widget_stay_on_top(self, stay_on_top: bool):
        self.root.attributes("-topmost", stay_on_top)

    def clamp_price_input(self, *args):
        if self.PriceEntry.get() == "":
            self.display_price_error(False)
            return
        if self.price_input.get().islower() or self.price_input.get().isupper():
            self.PriceEntry.delete(len(self.PriceEntry.get()) - 1, END)

    def display_price_error(self, show: bool):
        if show:
            self.PriceErrorLabel.config(text="Invalid Price")
        else:
            self.PriceErrorLabel.config(text="")

    def clamp_key_value(self, *args):
        if self.input_key_price == self.DEFAULT_KEY_PRICE:
            return
        if self.input_key_price.get().islower() or self.input_key_price.get().isupper():
            self.KeyPriceText.delete(len(self.KeyPriceText.get())-1, END)
            currency_value['Key'] = self.DEFAULT_KEY_PRICE
        else:
            currency_value['Key'] = float(self.input_key_price.get()) if self.input_key_price.get() else ...

    def clamp_metal_value(self, *args):
        if self.input_metal_price == self.DEFAULT_METAL_PRICE:
            return
        if self.input_metal_price.get().islower() or self.input_metal_price.get().isupper():
            self.MetalPriceText.delete(len(self.MetalPriceText.get()) - 1, END)

    def restore_metal_value(self, *args):
        if is_metal_input_valid(self.input_metal_price.get()):
            return
        else:
            self.MetalPriceText.delete(0, END)
            self.MetalPriceText.insert(0, self.DEFAULT_METAL_PRICE)

    def restore_key_value(self, *args):
        if is_price_input_valid(self.input_key_price.get()) and self.input_key_price.get() != "":
            return
        else:
            self.KeyPriceText.delete(0, END)
            self.KeyPriceText.insert(0, self.DEFAULT_KEY_PRICE)

    def price_to_currency(self):
        if is_price_input_valid(self.price_input.get()):
            self.display_price_error(False)
            self.currency_container.price_to_currency(float(self.price_input.get().replace(",", ".")), self)
        else:
            self.display_price_error(True)

    def items_to_value(self):
        self.currency_container.items_to_value(self) # from main.py

    def update_item_count(self):
        self.KeyItemFrame.update_currency_amount(self.currency_container.get_currency_item('Key').count)
        self.RefItemFrame.update_currency_amount(self.currency_container.get_currency_item('RefinedMetal').count)
        self.RecItemFrame.update_currency_amount(self.currency_container.get_currency_item('ReclaimedMetal').count)
        self.ScrapItemFrame.update_currency_amount(self.currency_container.get_currency_item('ScrapMetal').count)
        self.WeaponItemFrame.update_currency_amount(self.currency_container.get_currency_item('Weapon').count)

    def reset_item_count_text(self):
        self.KeyItemFrame.update_currency_amount(0)
        self.RefItemFrame.update_currency_amount(0)
        self.RecItemFrame.update_currency_amount(0)
        self.ScrapItemFrame.update_currency_amount(0)
        self.WeaponItemFrame.update_currency_amount(0)



class CurrencyFrame:
    def __init__(self, root: Tk, window_ref, frame_ref, image, row: int, item_name: str):
        self.root = root
        self.window_ref = window_ref
        self.frame_ref = frame_ref
        self.image = image
        self.row = row
        self.item_name = item_name

        self.item_count = StringVar(self.root)
        self.item_count.set("0")
        self.item_count_rev = self.item_count.get()

        self.Toggled = BooleanVar(self.root)
        self.Toggled.set(True)


        # ----- Main Widget -----

        self.ItemFrame = Frame(self.frame_ref, bg=MAINGRAY_BG)
        self.ItemFrame.grid(row=self.row, column=0, columnspan=2)

        self.Checkbox = Checkbutton(self.ItemFrame,
                                    bg=MAINGRAY_BG,
                                    variable=self.Toggled,
                                    activebackground=MAINGRAY_BG,
                                    command=self.currency_toggle)
        self.Checkbox.grid(row=0, column=0)

        self.ItemIcon = Label(self.ItemFrame,
                              image=self.image,
                              bg=MAINGRAY_BG,
                              padx=5)
        self.ItemIcon.grid(row=0, column=1, columnspan=2)

        self.ItemEntryFrame = Frame(self.ItemFrame, bg=MAINGRAY_BG)
        self.ItemEntryFrame.grid(row=0, column=3, columnspan=2)

        self.xText = Label(self.ItemEntryFrame,
                           bg=MAINGRAY_BG,
                           text="x",
                           fg="white",
                           padx=5,
                           font=("Arial", 12, "bold"))
        self.xText.grid(row=0, column=0)

        self.AmountEntry = Entry(self.ItemEntryFrame,
                                 bg=LIGHTGRAY_BG,
                                 fg="white",
                                 font=("Arial", 15),
                                 width=5,
                                 justify=CENTER,
                                 textvariable=self.item_count)
        self.AmountEntry.grid(row=0, column=1, columnspan=2)

        self.item_count.trace_add("write", self.on_value_change)

    def update_currency_amount(self, amount: int):
        self.AmountEntry.delete(0, END)
        self.AmountEntry.insert(0, int(amount))

    def on_value_change(self, *args):
        if self.item_count.get().islower() or self.item_count.get().isupper():
            self.AmountEntry.delete(len(self.AmountEntry.get())-1, END)
        self.window_ref.currency_container.change_item_amount(self.item_name, int(self.item_count.get()))

    def currency_toggle(self):
        if self.Toggled:
            self.item_count_rev = self.item_count.get()
            self.item_count.set("0")
        else:
            self.item_count.set(self.item_count_rev)
        self.window_ref.price_to_currency()
