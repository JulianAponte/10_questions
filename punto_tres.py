#Solo Leveling Fit.

flag_1 = True

while flag_1:

    days_training = input("Enter quantity that you days training last week: ")

    if not days_training.isdigit():
        print("\nInvalid number, please enter a valid number days.\n")
        continue

    if 0 <= days_training.isnumeric() <= 7:

        days_training = int(days_training)

        if 0 <= days_training <= 1:
            print("Don't give up, ¡You can do better!")
            break

        elif 2 <= days_training <= 3:
            print("Good job, ¡But you can give more!")
            break

        elif 4 <= days_training <= 7:
            print("¡Excelent! You win a skill point (Skill point +1)")
            break

        else:
            print('\nInvalid quantity, please enter a valid quantity.\n')
            continue
    else:
        break
