#Heladería Frosty.

chocolate = 4000.0
vainilla = 3500.0
topping = 1000.0

flag_1 = True

while flag_1:

    while True:
        product = input("""
        Which flavour do you like most:
        
        - Chocolate.
        - Vainilla.
        
        Select one option: """).lower()

        if product == "chocolate":
            product = chocolate
            break

        elif product == "vainilla":
            product = vainilla
            break

        else:
            print("\nFlavour not aviable, please choose one option.")

    while True:

        adition = input("""
    Do you want add any topping?

    - Yes.
    - No.

    Pick one option: """).lower()

        if adition == "no":
            qua_adition = 0
            total = qua_adition + product
            print(f'\nThe total to pay is ${total: .2f}, enjoy your ice cream.')
            break

        elif adition == "yes":

            while True:

                qua_adition = input('Enter quantity do you want add: ')

                if not qua_adition.isnumeric():
                    print('\nPlease enter a valid quantity\n')
                    continue

                qua_adition = int(qua_adition)

                qua_adition = qua_adition * topping

                if qua_adition <= 0:
                    print('\nPlease enter a valid quantity\n')
                    continue
                else:
                    total = qua_adition + product
                    print(f'\nThe total to pay is ${total: .2f}, enjoy your ice cream.')
                    break
        else:
            print("\nInvalid option, please select one.\n")
            continue
        break
    break