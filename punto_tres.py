#Solo Leveling Fit.

flag_1 = True

days_training = input("Enter quantity that you days training last week: ")

while flag_1:

    if not 0 <= days_training.isdigit() <= 7:
        print("Invalid number, please enter a valid number days.")
        continue


    days_training = int(days_training)

    if 0 <= days_training <= 1:
        print("Don't give up, ¡You can do better!")

    elif 2 <= days_training <= 3:
        print("Good job, ¡But you can give more!")
    
    else:
        print("¡Excelent! You win a skill point (Skill point +1)")
    
    break