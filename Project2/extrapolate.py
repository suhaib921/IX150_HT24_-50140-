import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

bit_sizes = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
times = np.array([1.7754, 1.2068, 2.2104, 0.3446, 23.1459, 23.6331, 26.9525, 118.2895, 111.3844, 846.8159, 1027.0917])

# Define a logarithmic function for fitting
def log_func(x, a, b):
    return a * np.log(x) + b

# Perform the curve fitting
popt, pcov = curve_fit(log_func, bit_sizes, times)

# Predict times for larger key sizes (1024, 2048, 4096 bits)
large_key_sizes = np.array([1024, 2048, 4096])
predicted_times = log_func(large_key_sizes, *popt)

# Plot the original data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(bit_sizes, times, color='blue', label="Original Data")
plt.plot(bit_sizes, log_func(bit_sizes, *popt), color='red', label="Fitted Logarithmic Curve")

# Plot predictions for larger key sizes
plt.scatter(large_key_sizes, predicted_times, color='green', label="Predicted for Larger Keys")
plt.title('Logarithmic Fit: Time to Crack RSA vs. Key Size')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.show()

# Output the predicted times for 1024, 2048, and 4096-bit keys
print(f"Predicted times for 1024-bit, 2048-bit, and 4096-bit RSA keys: {predicted_times}")



#why is i am not using exponential to illustrate:
#the predictions for larger key sizes (1024, 2048, and 4096 bits) are too extreme, which suggests that the exponential curve fitting may not be appropriate in this case. The time estimates appear to grow far too rapidly, leading to unrealistic predictions.