#====================================================================
# Practical 7: Practical 7: Bayesian Parameter Estimation
#====================================================================

# --- [Question 1] Estimate Female Survival Rate θ on Titanic via Bayesian Grid Updating ---
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Data
df = sns.load_dataset('titanic')
female = df[df['sex'] == 'female']['survived'].dropna()

n = len(female)
s = int(female.sum())
nonsurv = n - s

print(f"Total Female Passengers (n) : {n}")
print(f"Survived (s)                : {s}")
print(f"Not Survived (n - s)        : {nonsurv}")

# 2. Grid Discretization of theta from 0.1 to 0.9
theta_values = np.arange(0.1, 1.0, 0.1)

# 3. Uniform Prior: P(theta) = 1/9
prior = np.ones(len(theta_values)) / len(theta_values)

# 4. Binomial Log-Likelihood to prevent underflow: ln(L) = s*ln(θ) + (n-s)*ln(1-θ)
log_likelihood = s * np.log(theta_values) + nonsurv * np.log(1 - theta_values)

# Rescale log-likelihood before exponentiating to prevent numerical underflow
log_likelihood_scaled = log_likelihood - np.max(log_likelihood)
likelihood = np.exp(log_likelihood_scaled)

# 5. Compute Normalized Posterior: P(θ | D) ∝ Prior * Likelihood
unnormalized_posterior = prior * likelihood
posterior = unnormalized_posterior / unnormalized_posterior.sum()

# 6. Tabulate Results
results = pd.DataFrame({
    'Theta (θ)': np.round(theta_values, 1),
    'Prior': np.round(prior, 4),
    'Posterior': posterior
})
print("\n--- Bayesian Updating Table ---")
print(results.to_string(index=False))

# 7. MAP Estimate and Posterior Mean
map_index = np.argmax(posterior)
best_theta = theta_values[map_index]
posterior_mean = np.sum(theta_values * posterior)

print(f"\nMaximum A Posteriori (MAP) Estimate : θ* = {best_theta:.1f} (Posterior = {posterior[map_index]*100:.2f}%)")
print(f"Posterior Mean E[θ | Data]          : {posterior_mean:.4f}")

# 8. Visualization
plt.figure(figsize=(9, 5))
plt.plot(theta_values, prior, marker='o', linestyle='--', color='#ef4444', linewidth=2, label='Uniform Prior P(θ)')
plt.plot(theta_values, posterior, marker='s', linestyle='-', color='#2563eb', linewidth=2.5, label='Posterior P(θ | Data)')
plt.axvline(x=best_theta, color='#10b981', linestyle=':', label=f'MAP Estimate θ={best_theta}')
plt.xlabel('Possible Survival Probability (θ)')
plt.ylabel('Probability')
plt.title('Bayesian Parameter Estimation: Female Survival Probability on Titanic')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

