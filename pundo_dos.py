#Cinema "La Estrella".

flag_1 = True
age = 0

while flag_1:

        age = input('\n¡Welcome to La Estrella cinema!\n   Please enter your age: ')

        if not age.isdigit():
            print('\nInvalid input, please enter a valid age.')
            continue

        age = int(age)

        if age <=0:
            print("\n\nPlease enter a valid age.")
            continue

        
        elif age < 5:
            print("¡Your ticket is free, enjoy the movie!")

        elif 5 <= age <= 11:
            print("The price of your ticket is $5.000, thanks for your purchase.")

        elif 12 <= age <=59:
            print("The price of your Ticket is $8.000, thanks for your purchase.")

        else:
            print("THe price of your ticket is 4.000, theanks for your purchase.")
        break
