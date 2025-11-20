# 8. Empresa “TecnoPlus” — Evaluación compuesta
# El usuario ingresa dos notas (0.0 - 5.0):

# Prueba técnica (70%)
# Prueba lógica (30%)
# Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

# Condiciones:

# nota_final ≥ 3 → “Aprobado”
# 2 ≤ nota_final < 3 → “Revisión”
# < 2 → “Reprobado”
# Validar que las notas estén en rango.

flag_1 = True
print('\nResults tests "TecnoPlus" S.A.S \n')

while flag_1:
    pt_note = input("\nEnter technical test note: ")
    if pt_note.isalpha():
        print("\nPlease enter valid note.")
        continue
    pt_note = float(pt_note)
    if 0 <= pt_note <= 5:
        break
    else:
        print("\nPlease enter a valid note.")
        continue
while flag_1:
    pl_note = input("\nEnter logic test note: ")
    if pl_note.isalpha():
        print("\nPlease enter valid note.")
        continue
    pl_note = float(pl_note)
    if 0 <= pl_note <= 5:
        break
    else:
        print("\nPlease enter valid note.")
        continue
final_note =  (pt_note * 0.7) + (pl_note * 0.30)

if final_note >= 3:
    print(f"\nYou aprove, final note is {final_note: .1f}.")
elif 2 <= final_note < 3:
    print(f"\nYou need review, final note is {final_note: .1f}")
else:
    print(f"\nReprove, you need review & feedback, final note is {final_note: .1f}")