WATER = 1
ORANGE_JUICE = 2
APPLE_JUICE = 3
SPRITE = 4
COLA = 5
PRICE_WATER = 4
PRICE_ORANGE_JUICE = 4
PRICE_APPLE_JUICE = 8
PRICE_SPRITE = 8
PRICE_COLA = 9
payment = 0
product = int(input("Type a product number\n"
                    "1. Water\n"
                    "2. Orange juice\n"
                    "3. Apple juice\n"
                    "4. Sprite\n"
                    "5. Cole\n"))
if product == WATER:
    print("insert", PRICE_WATER, "₪")
    payment = PRICE_WATER
elif product == ORANGE_JUICE:
    print("insert", PRICE_ORANGE_JUICE, "₪")
    payment = PRICE_ORANGE_JUICE
elif product == APPLE_JUICE:
    print("insert", PRICE_APPLE_JUICE, "₪")
    payment = PRICE_APPLE_JUICE
elif product == SPRITE:
    print("insert", PRICE_SPRITE, "₪")
    payment = PRICE_SPRITE
elif product == COLA:
    print("insert", PRICE_COLA, "₪")
    payment = PRICE_COLA
else:
    print("Your choice is wrong")
if 0 < product < 6:
    coins_1 = int(input("Type how many 1₪ coins you insert\n"))
    coins_2 = int(input("Type how many 2₪ coins you insert\n"))
    coins_5 = int(input("Type how many 5₪ coins you insert\n"))
    coins_10 = int(input("Type how many 10₪ coins you insert\n"))
    amount_entered = coins_1 + coins_2 * 2 + coins_5 * 5 + coins_10 * 10
    if amount_entered >= payment:
        print("Thank you for shopping with us")
        print("The excess is", (amount_entered - payment),
                  "\n(in coins 10)", (amount_entered - payment) // 10,
                  "\n(in coins 5)", (amount_entered - payment) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - payment) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - payment) % 10 % 5 % 2)
    else:
        print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
