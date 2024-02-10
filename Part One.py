WATER = 1
ORANGE_JUICE = 2
APPLE_JUICE = 3
SPRITE = 4
COLA = 5
PRICE_WATER = "4₪"
PRICE_ORANGE_JUICE = "4₪"
PRICE_APPLE_JUICE = "8₪"
PRICE_SPRITE = "8₪"
PRICE_COLA = "9₪"
product = int(input("Type a product number\n"
                    "1. Water - 4₪\n"
                    "2. Orange juice - 4₪\n"
                    "3. Apple juice - 8₪\n"
                    "4. Sprite - 8₪\n"
                    "5. Cole - 9₪\n"))
if product == 1:
    print("insert", PRICE_WATER)
elif product == 2:
    print("insert", PRICE_ORANGE_JUICE)
elif product == 3:
    print("insert", PRICE_APPLE_JUICE)
elif product == 4:
    print("insert", PRICE_SPRITE)
elif product == 5:
    print("insert", PRICE_COLA)
else:
    print("Your choice is wrong")
