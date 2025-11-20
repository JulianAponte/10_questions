# 7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
# Menú: $12.000

# Opciones bebida:

# sí → $3.000
# no → $0
# Luego aplicar IVA del 8% al total final.
# Mostrar valor con IVA incluido.
import sys
menu = 12000.0
flag_1 = True
iva = 1.08
print('\nWelcome to "El Sabor Colombiano" restaurant.')

while flag_1:
    print("""

the menu lunch today is:

- Sopa de lentejas o Crema de Espinca.
- Res, pechuga, cerdo o chicharrón.
- Arroz blanco o pasta

Would you like to come in for lunch?""")
    option = input("\n1. Yes\n2. No.\n\n-> ")
    if not option.isnumeric():
        print("\nInvalid input, please choose one.")
        continue
    option = int(option)
    if option == 1:
        while True:
            drink = input("""
Would you like to add drinks?

-1. Yes.
-2. No.

Please choose one -> """)
            if drink == "1":
                drink = 3000.0
                break
            elif drink == "2":
                drink = 0.0
                break
            else:
                print("\nInvalid input, please choose one.")
                continue
        break
    elif option == 2:
        print("\nCome back soon, have a good day.")
        sys.exit()
        break
    else:
        print("\nInvalid option, please choose one.")
        continue
subtotal = menu + drink
total = subtotal * iva

print(f"Subtotal = ${subtotal:.0f} + %IVA, total is ${total:.0f}, Thanks for your purchase.")