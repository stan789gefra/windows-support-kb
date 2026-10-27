#====================================================================
# Practical 2: Practical 2: Continuous & Discrete Probability Distributions
#====================================================================

# --- [Question 1] Normal Distribution: Modeling & Fitting Examination Scores ---
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Generate 500 examination scores
data = np.random.normal(loc=70, scale=10, size=500)

# Fit normal distribution to estimate parameters (mu, sigma)
mu, sigma = stats.norm.fit(data)

# Plot density histogram
plt.figure(figsize=(9, 5))
plt.hist(data, bins=20, density=True, alpha=0.6, color='#10b981', edgecolor='#047857', label='Observed Scores')

# Generate fitted PDF line
x = np.linspace(data.min(), data.max(), 300)
pdf = stats.norm.pdf(x, mu, sigma)
plt.plot(x, pdf, color='#b91c1c', linewidth=2.5, label=f'Fitted Normal PDF (μ={mu:.2f}, σ={sigma:.2f})')

plt.xlabel("Examination Score")
plt.ylabel("Probability Density")
plt.title("Normal Distribution: Observed Data & Fitted PDF")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Estimated Mean (μ)              : {mu:.4f} (True: 70)")
print(f"Estimated Standard Deviation (σ): {sigma:.4f} (True: 10)")


# --- [Question 2] Poisson Distribution: Customer Support Requests per Minute ---
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Generate 500 Poisson samples with lambda = 4
data = np.random.poisson(lam=4, size=500)

# Estimate parameter lambda (sample mean)
lambda_hat = np.mean(data)

# Calculate observed probabilities
values, counts = np.unique(data, return_counts=True)
observed_prob = counts / len(data)

# Compute fitted Poisson PMF at observed values
fitted_prob = stats.poisson.pmf(values, lambda_hat)

# Plotting Observed vs Fitted
plt.figure(figsize=(9, 5))
plt.bar(values, observed_prob, alpha=0.6, color='#38bdf8', edgecolor='#0284c7', label='Observed Frequency')
plt.plot(values, fitted_prob, 'o-', color='#dc2626', linewidth=2, label=f'Fitted Poisson (λ={lambda_hat:.3f})')

plt.xlabel("Number of Requests per Minute")
plt.ylabel("Probability")
plt.title("Poisson Distribution: Observed vs. Fitted PMF")
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()

print(f"Estimated Lambda (λ): {lambda_hat:.4f} (True λ = 4)")


# --- [Question 3] Exponential Distribution: Customer Waiting Time ---
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Generate 500 exponential waiting times with average scale = 5 mins
data = np.random.exponential(scale=5, size=500)

# Fit exponential distribution fixing loc=0
loc, scale = stats.expon.fit(data, floc=0)

# Plot density histogram
plt.figure(figsize=(9, 5))
plt.hist(data, bins=25, density=True, alpha=0.6, color='#f97316', edgecolor='#c2410c', label='Observed Wait Times')

# Overlay fitted exponential PDF
x = np.linspace(0, data.max(), 300)
pdf = stats.expon.pdf(x, loc=loc, scale=scale)
plt.plot(x, pdf, color='#1e3a8a', linewidth=2.5, label=f'Fitted Expon PDF (Scale={scale:.2f} mins)')

plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Probability Density")
plt.title("Exponential Distribution: Customer Waiting Time")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Estimated Scale Parameter (Mean Wait Time): {scale:.4f} minutes (True: 5.0)")


# --- [Question 4] Sensor Noise Modeling with Gaussian Distribution ---
import numpy as np
import matplotlib.pyplot as plt

# Original clean sensor readings
data = np.array([50, 52, 48, 51, 49, 53, 50, 47, 52, 51])

np.random.seed(42)
# Gaussian noise with mean 0 and standard deviation 2 (variance 4)
noise = np.random.normal(loc=0, scale=2, size=len(data))

# Noisy observed data
noisy_data = data + noise

print("Original Sensor Readings :", data)
print("Generated Gaussian Noise :", np.round(noise, 3))
print("Noisy Sensor Readings    :", np.round(noisy_data, 3))

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', linewidth=2, color='#2563eb', label='True Signal (Original)')
plt.plot(noisy_data, marker='s', linestyle='--', linewidth=2, color='#ef4444', label='Noisy Sensor Measurement (Signal + Noise)')
plt.xlabel("Observation Index")
plt.ylabel("Measurement Value")
plt.title("Impact of Gaussian Noise on Sensor Measurements")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

