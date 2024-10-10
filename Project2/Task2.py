import time
import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy import mod_inverse

def factor_n(n):
    faktorer = sympy.factorint(n)
    if len(faktorer) != 2:
        raise ValueError("Inga faktorer hittades eller n är inte produkten av två primtal")
    return tuple(faktorer.keys())

# RSA crack method
def RSAcrack(cipher, n, e):
    p, q = factor_n(n)
    
    phi_n = (p - 1) * (q - 1)
    
    # Calculate the private key d
    d = mod_inverse(e, phi_n)
    
    decrypted_message = pow(cipher, d, n)
    
    return decrypted_message

# Test how long it takes to crack RSA for different n bit sizes
def time_to_crack_rsa(bit_size_start, bit_size_end, message):
    times = []
    bit_sizes = list(range(bit_size_start, bit_size_end + 1, 10))
    
    for bits in bit_sizes:
        # Generate two random prime numbers p and q of appropriate bit length
        p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        n = p * q
        e = 65537  # Commonly used public exponent
        
        # Encrypt the message
        cipher = pow(message, e, n)
        
        # Time how long it takes to crack
        start_time = time.time()
        RSAcrack(cipher, n, e)
        elapsed_time = time.time() - start_time
        
        times.append(elapsed_time)
        print(f"Cracked {bits}-bit RSA in {elapsed_time:.4f} seconds.")
    
    return bit_sizes, times

# Visualize the results
def plot_rsa_crack_times(bit_sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(bit_sizes, times, marker='o')
    plt.title('Time to Crack RSA vs. Key Size')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

message = int.from_bytes(b"GO DOWN DEEP ENOUGH INTO ANYTHING AND YOU WILL FIND MATHEMATICS.", "big")

# Crack RSA for key sizes from 100 to 200 bits
bit_sizes, times = time_to_crack_rsa(100, 200, message)

# Plot the results
plot_rsa_crack_times(bit_sizes, times)

# Extrapolate to predict the cracking time for larger key sizes
def predict_time_for_large_keys(bit_sizes, times, large_key_sizes):
    log_times = np.log(times)
    coeffs = np.polyfit(bit_sizes, log_times, 1)
    predicted_times = np.exp(np.polyval(coeffs, large_key_sizes))
    
    plt.figure(figsize=(10, 6))
    plt.plot(bit_sizes, times, marker='o', label='Observed Times')
    plt.plot(large_key_sizes, predicted_times, marker='x', linestyle='--', label='Predicted Times')
    plt.title('Predicted Time to Crack RSA for Larger Key Sizes')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Predict time for 1024, 2048, and 4096-bit RSA keys
large_key_sizes = [1024, 2048, 4096]
predict_time_for_large_keys(bit_sizes, times, large_key_sizes)
