# 10. Club “Noche Estelar” — Acceso + validación documento
# Pedir edad y documento.

# Reglas:

# Edad ≥ 18 → puede entrar solo si tiene documento.
# Si la edad < 18 → "Entrada denegada"
# Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

flag_1 = True
print('\nWelcome to "Noche Estelar" Club.')

while flag_1:
    age = input("\nEnter age user -> ")
    if not age.isnumeric():
        print("\nInvalid input, please enter age.")
        continue
    age = int(age)
    if 0 < age < 18:
        print("\nAccess denied, user is a minor.")
        break
    elif 18 <= age <= 55:
        while True:
            id_user = input("\nUser has ID?\n1. Yes.\n2. No.\n\n--> ")
            if not id_user.isnumeric():
                print("\nInvalid input, please enter ID.")
                continue
            id_user = int(id_user)
            if id_user == 1:
                print("\nAccess granted ¡Enjoy your night!")
                break
            elif id_user == 2:
                print("\nAccess denied, come back with ID.")
                break
            else:
                print("\nPlease choose one option.")
                continue
        break
    else:
        print("\nPlease enter a valid age.")
        continue