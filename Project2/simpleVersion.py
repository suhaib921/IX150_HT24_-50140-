import random
from math import gcd

# Step 1: Pick two large prime numbers (p, q)
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_candidate():
    """Generate an odd prime candidate (for simplicity, small primes)."""
    while True:
        prime_candidate = random.randint(50, 100)
        if is_prime(prime_candidate):
            return prime_candidate

# Generate two prime numbers
p = generate_prime_candidate()
q = generate_prime_candidate()
print(f"Prime p: {p}, Prime q: {q}")

# Step 2: Calculate N = p * q
N = p * q
print(f"Modulus N (p * q): {N}")

# Step 3: Calculate Euler's Totient function O(N) = (p - 1)(q - 1)
phi_N = (p - 1) * (q - 1)
print(f"Euler's Totient φ(N): {phi_N}")

# Step 4: Choose public exponent e such that 1 < e < phi(N) and gcd(e, phi(N)) = 1
def find_public_exponent(phi_N):
    """Find a public exponent e that is coprime with phi(N)."""
    e = random.randint(2, phi_N - 1)
    while gcd(e, phi_N) != 1:
        e = random.randint(2, phi_N - 1)
    return e

# Step 5: Calculate private exponent d using the Extended Euclidean Algorithm
def extended_gcd(a, b):
    """The Extended Euclidean Algorithm to find the modular inverse of e mod φ(N)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # Return the coefficient for a (old_s), which is the modular inverse of e
    return old_s

# Generate valid e and d (using the correct modular inverse calculation)
e = find_public_exponent(phi_N)
d = extended_gcd(e, phi_N)

# Make sure d is positive
if d < 0:
    d += phi_N

# Avoid d = e situation
while d == e:
    e = find_public_exponent(phi_N)
    d = extended_gcd(e, phi_N)
    if d < 0:
        d += phi_N

print(f"Public exponent e: {e}")
print(f"Private exponent d: {d}")

# Step 6: Generate Public and Private Keys
public_key = (N, e)
private_key = (N, d)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Step 7: Encrypt a message using the public key
def encrypt(message, public_key):
    N, e = public_key
    ciphertext = [pow(ord(char), e, N) for char in message]
    return ciphertext

# Step 8: Decrypt the message using the private key
def decrypt(ciphertext, private_key):
    N, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, N)) for char in ciphertext])
    return decrypted_message

# Example usage
message = "A few miles south of Soledad, the Salinas River drops in close to the hillside bank and runs deep and"
print(f"\nOriginal Message: {message}")

# Encrypt the message
ciphertext = encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, private_key)
print(f"Decrypted Message: {decrypted_message}")
