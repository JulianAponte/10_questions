# 9. Supermercado “AhorroMax” — Descuentos y envío
# Cada producto cuesta $2.000.

# Reglas:

# 30 unidades → 15% descuento

# 10 unidades → 5% descuento

# Si el total después del descuento es < $50.000 → agregar $5.000 de envío
# Calcular total final.

product = 2000.0
delivery = 5000.0

flag_1 = True

print("¡Welcome to 'AhorroMax' SuperMarket!")
while flag_1:
    quantity = input("\nHow many products does the customer buy?\n\n-> ")
    if not quantity.isnumeric():
        print("\nInvalid input, please enter valid quantity.")
        continue
    quantity = int(quantity)
    if quantity >= 30:
        discount = 0.85
        break
    elif quantity >= 10:
        discount = 0.95
        break
    elif 0 < quantity < 10:
        discount = 1
        break
    else:
        print("\nInvalid quantity, please enter a valid quantity.")
        continue
subtotal= (product * quantity) * discount
total = subtotal + delivery

if total < 50000:
    print(f"Products ${subtotal:.0f} + ${delivery:.0f}, total of purchase is ${total:.0f}.")
else:
    print(f"Total of your purchase for {quantity} products is ${subtotal:.0f}.")