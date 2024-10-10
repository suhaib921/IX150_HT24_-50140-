from math import comb

# Function to calculate valid sequences where A is always ahead of B
def ballot_problem(a, b):
    # Formula for the ballot problem:
    valid_sequences = (a - b) * comb(a + b, b) // (a + b)
    return valid_sequences

# Total number of ways to arrange the votes without any restriction
def total_ways(a, b):
    return comb(a + b, b)

# Number of valid sequences and total sequences
a_votes = 9
b_votes = 2

valid_sequences = ballot_problem(a_votes, b_votes)
total_sequences = total_ways(a_votes, b_votes)

# Probability that A will always be ahead of B
probability = valid_sequences / total_sequences

print(f"Number of valid sequences where A is always ahead: {valid_sequences}")
print(f"Total number of sequences without restrictions: {total_sequences}")
print(f"Probability that A is always ahead: {probability:.4f}")
