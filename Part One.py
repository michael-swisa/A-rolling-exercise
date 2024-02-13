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
product = int(input("Type a product number\n"
                    "1. Water - 4₪\n"
                    "2. Orange juice - 4₪\n"
                    "3. Apple juice - 8₪\n"
                    "4. Sprite - 8₪\n"
                    "5. Cole - 9₪\n"))
if product == 1:
    print("insert", PRICE_WATER, "₪")
elif product == 2:
    print("insert", PRICE_ORANGE_JUICE, "₪")
elif product == 3:
    print("insert", PRICE_APPLE_JUICE, "₪")
elif product == 4:
    print("insert", PRICE_SPRITE, "₪")
elif product == 5:
    print("insert", PRICE_COLA, "₪")
else:
    print("Your choice is wrong")
if 0 < product < 6:
    coins_1 = int(input("Type how many 1₪ coins you insert\n"))
    coins_2 = int(input("Type how many 2₪ coins you insert\n"))
    coins_5 = int(input("Type how many 5₪ coins you insert\n"))
    coins_10 = int(input("Type how many 10₪ coins you insert\n"))
    amount_entered = coins_1 + coins_2 * 2 + coins_5 * 5 + coins_10 * 10
    if product == 1:
        if amount_entered >= PRICE_WATER:
            print("Thank you for shopping with us")
            print("The excess is", (amount_entered - PRICE_WATER),
                  "\n(in coins 10)", (amount_entered - PRICE_WATER) // 10,
                  "\n(in coins 5)", (amount_entered - PRICE_WATER) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - PRICE_WATER) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - PRICE_WATER) % 10 % 5 % 2)
        else:
            print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
    if product == 2:
        if amount_entered >= PRICE_ORANGE_JUICE:
            print("Thank you for shopping with us")
            print("The excess is", (amount_entered - PRICE_ORANGE_JUICE),
                  "\n(in coins 10)", (amount_entered - PRICE_ORANGE_JUICE) // 10,
                  "\n(in coins 5)", (amount_entered - PRICE_ORANGE_JUICE) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - PRICE_ORANGE_JUICE) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - PRICE_ORANGE_JUICE) % 10 % 5 % 2)
        else:
            print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
    if product == 3:
        if amount_entered >= PRICE_APPLE_JUICE:
            print("Thank you for shopping with us")
            print("The excess is", (amount_entered - PRICE_APPLE_JUICE),
                  "\n(in coins 10)", (amount_entered - PRICE_APPLE_JUICE) // 10,
                  "\n(in coins 5)", (amount_entered - PRICE_APPLE_JUICE) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - PRICE_APPLE_JUICE) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - PRICE_APPLE_JUICE) % 10 % 5 % 2)
        else:
            print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
    if product == 4:
        if amount_entered >= PRICE_SPRITE:
            print("Thank you for shopping with us")
            print("The excess is", (amount_entered - PRICE_SPRITE),
                  "\n(in coins 10)", (amount_entered - PRICE_SPRITE) // 10,
                  "\n(in coins 5)", (amount_entered - PRICE_SPRITE) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - PRICE_SPRITE) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - PRICE_SPRITE) % 10 % 5 % 2)
        else:
            print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
    if product == 5:
        if amount_entered >= PRICE_COLA:
            print("Thank you for shopping with us")
            print("The excess is", (amount_entered - PRICE_COLA),
                  "\n(in coins 10)", (amount_entered - PRICE_COLA) // 10,
                  "\n(in coins 5)", (amount_entered - PRICE_COLA) % 10 // 5,
                  "\n(in coins 2)", (amount_entered - PRICE_COLA) % 10 % 5 // 2,
                  "\n(in coins 1)", (amount_entered - PRICE_COLA) % 10 % 5 % 2)
        else:
            print("You did not insert enough coins and your money is returned\n"
                  "You can log in again from the beginning\nYour surplus", amount_entered, "₪")
