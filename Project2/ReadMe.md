When the problem refers to **"different sizes on your public key \(n\) (100-200 bits)"**, it is asking you to test how long it takes to crack RSA encryption with moduli (the public key \(n\)) of various sizes between 100 and 200 bits. Specifically, RSA public keys are composed of a modulus \(n\) that is the product of two large prime numbers \(p\) and \(q\). The bit size of \(n\) refers to the number of bits used to represent this number. For instance:
- A **100-bit** public key means that \(n\) is a number composed of around 100 bits, which is roughly a 30-digit decimal number.
- A **200-bit** public key means \(n\) is a number composed of 200 bits, or about 60 decimal digits.

### Objective Breakdown:

1. **Cracking the Cipher for Different Public Key Sizes**:
   - You need to **factor** \(n\) (the modulus), which is the most computationally difficult part of cracking RSA.
   - You are asked to **measure the time** it takes to factor \(n\) and hence crack the cipher for various values of \(n\) where \(n\) has bit lengths ranging from 100 to 200 bits.
   - As part of the task, you would:
     - Generate RSA public keys of size \(n\) for different bit lengths between 100 and 200 bits.
     - Attempt to crack the RSA encryption (factor \(n\) into \(p\) and \(q\)) for each key size.
     - Record how long it takes to crack each key.

2. **Plotting a Graph**:
   - Once you've recorded how long it takes to crack RSA for different public key sizes between 100 and 200 bits, plot a graph that shows the **relationship between key size (in bits)** and **time to crack**.
   - Typically, factoring algorithms like GNFS have **sub-exponential** time complexity, meaning the time required to crack RSA increases dramatically as \(n\) grows larger. The graph should reflect this.

3. **Modeling the Time for Larger Key Sizes (1024, 2048, and 4096 bits)**:
   - Based on the graph for smaller bit sizes (100-200 bits), you are expected to **extrapolate** or create a **mathematical model** that predicts how long it would take to crack RSA for **larger key sizes**, such as:
     - **1024 bits** (commonly used for lower-security applications but considered insecure today)
     - **2048 bits** (currently widely used and considered secure)
     - **4096 bits** (used in high-security scenarios)
   - The goal is to predict how the **cracking time** scales with **key size** using the trend you observed from your experiments with 100-200 bit keys. This might involve fitting a curve (e.g., exponential or sub-exponential) based on your data points.

### Explanation of Each Step in More Detail:

#### 1. **Cracking RSA for Key Sizes between 100 and 200 bits**:
   - **Generate RSA public keys**: Start by generating moduli \(n = p \times q\) of different bit sizes (100, 110, 120, ..., 200 bits).
   - **Crack the encryption**: For each generated key, use a factoring algorithm (like `sympy.factorint` or any other efficient factoring method) to find the prime factors \(p\) and \(q\).
   - **Measure the cracking time**: For each key size, measure how long it takes to factor \(n\) and hence crack the RSA key.

#### 2. **Plotting the Cracking Time for Different Key Sizes**:
   - **X-axis**: Key size in bits (ranging from 100 to 200 bits).
   - **Y-axis**: Time taken to crack the key.
   - You should observe that the time increases dramatically as the key size increases because factoring becomes much harder for larger numbers.

#### 3. **Predicting Cracking Times for Larger Keys (1024, 2048, 4096 bits)**:
   - After plotting the results for the 100-200 bit keys, you can **fit a curve** (e.g., exponential or sub-exponential) to your data. This will allow you to model the relationship between **key size** and **cracking time**.
   - Once the model is built, you can use it to **predict how long** it would take to crack RSA keys of larger sizes, such as 1024, 2048, and 4096 bits.
   - For example, if the relationship between key size and cracking time is exponential, you might expect that cracking a 1024-bit key will take exponentially longer than a 200-bit key, and cracking a 4096-bit key will take even longer.

### Key Insights:
- **Smaller keys (100-200 bits)**: These are easier to factor, and it’s feasible to crack them with common factorization methods. You’ll be able to measure the time directly.
- **Larger keys (1024, 2048, 4096 bits)**: These keys are much harder to factor. Since it’s impractical to actually crack such large keys within a reasonable time, you’ll rely on the model based on your smaller key experiments to **estimate** how long it would take.
  
  - For example:
    - If it takes 1 second to factor a 100-bit key, and your model shows that cracking time increases exponentially, you might estimate that cracking a 1024-bit key could take thousands or millions of years.

### Steps to Achieve This:
1. **Generate RSA moduli** of 100-200 bits.
2. **Crack the RSA moduli** and measure the time taken to factor \(n\).
3. **Plot the cracking time** as a function of key size.
4. **Fit a curve** to model the time complexity.
5. **Extrapolate** the model to predict the time required to crack 1024-bit, 2048-bit, and 4096-bit RSA keys.

### Example of Extrapolation Model:
If you observe that the cracking time \(T\) follows an exponential relationship with key size \(n\), you could use a model like:
\[
T(n) = a \cdot \exp(b \cdot n)
\]
Where \(a\) and \(b\) are constants that you determine from the data you collected for the 100-200 bit keys.

Once you have \(a\) and \(b\), you can **predict** the time required for larger key sizes, such as 1024, 2048, and 4096 bits.

### Conclusion:
- The task is about **measuring** how cracking time grows as the public key \(n\) increases from 100 to 200 bits.
- **Extrapolate** from this data to **predict** the time it would take to crack larger keys (1024, 2048, 4096 bits).
- This will help you understand how **exponentially harder** it becomes to break RSA as the key size increases, which is why larger key sizes are used in modern cryptography for security.