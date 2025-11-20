# 5. Librería “El Saber” — Descuento estudiante + cupón
# Libro cuesta $25.000.

# Si es estudiante → 15% descuento
# Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
# Validar:

# Si no es estudiante, el cupón no aplica.
# Si ingresa cupón incorrecto, ignorarlo.
# Mostrar total.

book = 25000.0
cupon = 1

flag_1 = True
flag_2 = True
flag_3 = True

print('¡Welcome to Library "El saber"')

while flag_1:
    client = input("""
You're student? 

1. Yes.
2. No

Select one option -> """)
    if not client.isnumeric():
        print("\nInvalid input, choose one option.")
        continue
    client = int(client)
    if client == 1:
        discount = 0.85
        break
    elif client == 2:
        discount = 1
        break
    else:
        print("\nInvalid option, please choose one option.")
        continue
while flag_2:
    question = input("""
Do you have any cupon?

1. Yes.
2. No.

-> """)
    if not question.isnumeric():
        print("\nInvalid input, choose one option.")
        continue
    question = int(question)
    if question == 1:
        cupon = input("\nPlease enter cupon: ")
        if cupon == "LIBRO10":
            print("Apply discount. . .")
            cupon = 0.90
        else:
            print("Cupon not found.")
            cupon =1
        break
    elif question == 2:
        cupon = 1
        break
    else:
        print("\nInvalid option, please choose one option.")
        continue
while flag_3:
    qua_book = input("\nEnter quantity books bought: ")
    if not qua_book.isnumeric():
        print("\nPlease enter a quantity of books bought.")
        continue
    qua_book = int(qua_book)
    if qua_book <= 0:
        print("\nPlease enter a valid quantity.")
        continue
    else:
        normal_price = qua_book * book
        break
subtotal = normal_price * discount
total = subtotal * cupon
flag_1 = False
print(f"Total of your purchase is: {total}, please cme again.")

