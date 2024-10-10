# Ballot Problem - Always Ahead

## Problem Description

The candidates A and B are the finalists for an award. A committee of 11 members will place their vote (in favor of one of the candidates) into a ballot box. Suppose that A receives 9 votes and B receives 2 votes. We need to calculate how many ways the ballots can be selected, one at a time, so that there are always more votes in favor of A than B throughout the count.

### Task
- **Part 1**: Find the number of ways to select ballots ensuring that A is always strictly ahead of B during the vote counting process.
- **Part 2**: Calculate the probability that A will be strictly ahead of B throughout the vote counting.

## Solution

The problem can be modeled as a **ballot problem** or **lattice path problem** where we count valid sequences of "U" (up for A's vote) and "L" (left for B's vote), ensuring that A is always ahead.

The number of valid sequences where candidate A is always ahead of candidate B can be solved using the **Catalan number** or the **ballot theorem** formula:

\[
C_n = \frac{(a - b)}{a + b} \times \binom{a + b}{b}
\]

Where:
- `a` is the number of votes for A.
- `b` is the number of votes for B.
- \(\binom{a + b}{b}\) is the binomial coefficient for choosing the votes in total.