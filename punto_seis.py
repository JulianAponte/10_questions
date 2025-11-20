# 6. Parqueadero “RapidCar” — Tarifa escalonada
# Tarifa:

# 0 a 5 horas: $2.000 x hora
# 5 horas: $2.000 x hora + multa fija de $5.000

# Validar horas:

# No permitir números negativos.
# Mostrar valor total.
import math

hour = 2000.0
ticket = 5000.0
flag_1 = True
total_time = 0.0

print('Ticket system "RapidCar" Parking\n')
while flag_1:
    time = input("\nEnter total time parking in minutes -> ")
    if not time.isnumeric():
        print("\nInvalid input, please enter valid time.")
        continue
    time = float(time)
    if time <=0:
        print("\nTime must be greater than 0.")
    total_time = time/60
    total_time = math.ceil(total_time)
    if 0.1 <=total_time <= 5:
        total = total_time * hour
        print(f"\nTotal for {total_time: .0f} hours is {total: .0f}.")
        break
    elif 5 <= total_time:
        total = (total_time * hour)
        print(f"\nSubtotal for {total_time: .0f} hours is {total: .0f} + {ticket: .0f}, total is:{total+ticket: .0f}.")
        break