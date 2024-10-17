import time
import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy import mod_inverse

# Faktorisera n till två primtal p och q
def faktorisera_n(n):
    faktorer = sympy.factorint(n)
    if len(faktorer) != 2:
        raise ValueError("Inga faktorer hittades eller n är inte produkten av två primtal")
    return tuple(faktorer.keys())

# RSA-avkodningsmetod
def knäck_RSA(chiffer, n, e):
    p, q = faktorisera_n(n)
    
    phi_n = (p - 1) * (q - 1)
    
    # Beräkna den privata nyckeln d
    d = mod_inverse(e, phi_n)
    
    dekrypterat_meddelande = pow(chiffer, d, n)
    
    return dekrypterat_meddelande

# Testa hur lång tid det tar att knäcka RSA för olika nyckelstorlekar
def tid_att_knäcka_rsa(start_bitstorlek, slut_bitstorlek, meddelande):
    tider = []
    bitstorlekar = list(range(start_bitstorlek, slut_bitstorlek + 1, 10))
    
    for bits in bitstorlekar:
        # Generera två slumpmässiga primtal p och q av lämplig bitstorlek
        p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        n = p * q
        e = 65537  # Vanlig offentlig exponent
        
        # Kryptera meddelandet
        chiffer = pow(meddelande, e, n)
        
        # Mät tiden det tar att knäcka
        start_tid = time.time()
        knäck_RSA(chiffer, n, e)
        elapsed_tid = time.time() - start_tid
        
        tider.append(elapsed_tid)
        print(f"Knäckte {bits}-bitars RSA på {elapsed_tid:.4f} sekunder.")
    
    return bitstorlekar, tider

# Visualisera resultaten
def plot_rsa_knäckningstider(bitstorlekar, tider):
    plt.figure(figsize=(10, 6))
    plt.plot(bitstorlekar, tider, marker='o')
    plt.title('Tid att knäcka RSA vs. Nyckelstorlek')
    plt.xlabel('Nyckelstorlek (bitar)')
    plt.ylabel('Tid (sekunder)')
    plt.grid(True)
    plt.show()

# Meddelandet som ska krypteras och knäckas
meddelande = int.from_bytes(b"GO DOWN DEEP ENOUGH INTO ANYTHING AND YOU WILL FIND MATHEMATICS.", "big")

# Knäck RSA för nyckelstorlekar från 100 till 200 bitar
bitstorlekar, tider = tid_att_knäcka_rsa(100, 200, meddelande)

# Plotta resultaten
plot_rsa_knäckningstider(bitstorlekar, tider)

# Extrapolera för att förutse knäckningstiden för större nyckelstorlekar
def förutse_tid_for_stora_nycklar(bitstorlekar, tider, stora_nyckelstorlekar):
    log_tider = np.log(tider)
    koeffs = np.polyfit(bitstorlekar, log_tider, 1)
    förutsagda_tider = np.exp(np.polyval(koeffs, stora_nyckelstorlekar))
    
    plt.figure(figsize=(10, 6))
    plt.plot(bitstorlekar, tider, marker='o', label='Observerade tider')
    plt.plot(stora_nyckelstorlekar, förutsagda_tider, marker='x', linestyle='--', label='Förutsagda tider')
    plt.title('Förutsagd tid att knäcka RSA för större nyckelstorlekar')
    plt.xlabel('Nyckelstorlek (bitar)')
    plt.ylabel('Tid (sekunder)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Förutse tid för 1024, 2048, och 4096-bitars RSA-nycklar
stora_nyckelstorlekar = [1024, 2048, 4096]
förutse_tid_for_stora_nycklar(bitstorlekar, tider, stora_nyckelstorlekar)
