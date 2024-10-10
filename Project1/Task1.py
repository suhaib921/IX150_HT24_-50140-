from itertools import permutations

# a) Antal vägar från (0, 3) till (7, 2)
def antal_vagar_0_3_till_7_2():
    vagar = set(permutations(['U'] * 3 + ['L'] * 4))  # 3 U and 4 L movements
    print("a) Antalet vägar från (0, 3) till (7, 2):", len(vagar))
    for vag in vagar:
        print(''.join(vag))

# b) Antal vägar från (0, 3) till (7, 2) som vidrör x-axeln
def vagar_som_vidror_x_axeln():
    vagar = set(permutations(['U'] * 3 + ['L'] * 4))  # 3 U and 4 L movements
    vagar_som_vidror = set()
    for vag in vagar:
        x, y = 0, 3
        for steg in vag:
            if steg == 'L':
                y -= 1
            else:
                y += 1
            if y == 0:  # The path touches the x-axis
                vagar_som_vidror.add(vag)
                break
    return vagar_som_vidror

# c) Antal vägar från (0, 3) till (7, 2) som EJ vidrör x-axeln
def vagar_ej_vidror_x_axeln():
    vagar = set(permutations(['U'] * 3 + ['L'] * 4))  # 3 U and 4 L movements
    vagar_som_vidror = vagar_som_vidror_x_axeln()
    icke_vagar_som_vidror = vagar - vagar_som_vidror
    print("c) Antalet vägar från (0, 3) till (7, 2) som EJ vidrör x-axeln:", len(icke_vagar_som_vidror))
    for vag in icke_vagar_som_vidror:
        print(''.join(vag))

# d) Antal vägar från (7, 6) till (20, 5) som EJ vidrör x-axeln
def vagar_ej_vidror_x_axeln_7_6_till_20_5():
    vagar = set(permutations(['U'] * 6 + ['L'] * 7))  # 6 U and 7 L movements
    icke_vagar_som_vidror = set()
    vagar_som_vidror = set()
    
    for vag in vagar:
        x, y = 7, 6  # Startpoint (7, 6)
        korsat_x_axeln = False
        for steg in vag:
            if steg == 'L':
                y -= 1
            else:
                y += 1
            if y == 0:  # The path touches the x-axis
                korsat_x_axeln = True
                break
        
        if not korsat_x_axeln:
            icke_vagar_som_vidror.add(vag)
        else:
            vagar_som_vidror.add(vag)
    
    print("Antal vägar från (7, 6) till (20, 5) som EJ vidrör x-axeln:", len(icke_vagar_som_vidror))
    print("Antal vägar som vidrör x-axeln:", len(vagar_som_vidror))

    i = 0
    for vag in icke_vagar_som_vidror:
        if i < 20:
            print(''.join(vag))
        i += 1

# Running the code
antal_vagar_0_3_till_7_2()
vagar_som_vidror_x_axeln()
vagar_ej_vidror_x_axeln()
vagar_ej_vidror_x_axeln_7_6_till_20_5()
