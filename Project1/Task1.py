from itertools import permutations
# a) Antal v¨agar fr˚an (0, 3) till (7, 2)
vagar = set(permutations(['U'] * 3 + ['L'] * 4)) # 3 U och 4 L r¨orelser
print("a) Antalet v¨agar fr˚an (0, 3) till (7, 2): ", len(vagar))
for vag in vagar:
print(''.join(vag))
# b) Antal v¨agar fr˚an (0, 3) till (7, 2) som vidr¨or x-axeln
def vagar_som_vidror_x_axeln():
vagar = set(permutations(['U'] * 3 + ['L'] * 4)) # 3 U och 4 L r¨orelser
vagar_som_vidror = set()
for vag in vagar:
x, y = 0, 3
for steg in vag:
if steg == 'L':
y -= 1
else:
y += 1
if y == 0: # Ej framme, men vi vidr¨or x-axeln
vagar_som_vidror.add(vag)
break
return vagar_som_vidror
vagar = set(permutations(['U'] * 3 + ['L'] * 4)) # 3 U och 4 L r¨orelser
print("b) Antal v¨agar som vidr¨or x-axeln: ", len(vagar))
for vag in vagar:
print(''.join(vag))
# c) Antal v¨agar fr˚an (0, 3) till (7, 2) som EJ vidr¨or x-axeln
vagar = set(permutations(['U'] * 3 + ['L'] * 4))
vagar = vagar - vagar_som_vidror_x_axeln()
print("Antal v¨agar fr˚an (0, 3) till (7, 2) som EJ vidr¨or x-axeln: ", len(vagar))
for vag in vagar:
print(''.join(vag))
# d) Antal v¨agar fr˚an (7, 6) till (20, 5) som EJ vidr¨or x-axeln
def vagar_ej_vidror_x_axeln_7_6_till_20_5():
5
vagar = set(permutations(['U'] * 6 + ['L'] * 7))
icke_vagar_som_vidror = set()
vagar_som_vidror = set()
for vag in vagar:
x, y = 7, 6 # Startpunkt (7, 6)
korsat_x_axeln = False
for steg in vag:
if steg == 'L':
y -= 1
else:
y += 1
if y == 0: # Om v¨agen n˚ar x-axeln
korsat_x_axeln = True
break
if not korsat_x_axeln:
icke_vagar_som_vidror.add(vag)
else:
vagar_som_vidror.add(vag)
print("Antal v¨agar fr˚an (7, 6) till (20, 5) som EJ vidr¨or x-axeln: ",
len(icke_vagar_som_vidror),
". De som vidr¨or x-axeln: ", len(vagar_som_vidror))
i = 0
for vag in icke_vagar_som_vidror:
if (i < 20):
print(''.join(vag))
i = i + 1
vagar_ej_vidror_x_axeln_7_6_till_20_5()
