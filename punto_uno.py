#Panadería de Don Pancho.

u_bread = 300
flag_1 = True

while flag_1:
    qua_bread = int(input("Enter the quantity of bread loaves you want to buy: "))

    total_bread = qua_bread * u_bread

    if qua_bread >= 50:
        
        total = total_bread * 0.80
        total = float(total)
        print(f"The total to pay for {qua_bread} breads is {total: .2f} with 20% of discount, thanks for your purchase.")
        
        flag_1 = False

    elif qua_bread >= 20:

        total = total_bread * 0.90
        total = float(total)
        print(f"The total to pay for {qua_bread} breads is ${total: .2f} with 10% of discount, thanks for your purchase.")
        
        flag_1 = False

    elif 0 < qua_bread < 20:
        total_bread = float(total_bread)
        print(f"The total to pay is ${total_bread: .2f}, thanks for your purchase.")
        
        flag_1 = False

    else:
        print("Invalid quantity, please try again.")