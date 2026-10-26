"""
Practical 7: Practical 7
Description: Bayesian Inference & Parameter Estimation (Titanic Survival Rate)
Original File: Prac7.ipynb
"""


# ------------------------------------------------------------
# Q1)
# ------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset('titanic')
print(df.head())


female = df[df['sex'] == 'female']['survived'].dropna()

n=len(female)
s = female.sum()
nonsurv = n-s
print("total female passenger : ",n)
print("total female survived : ",s)
print("total female not survived : ",nonsurv)


theta_values = np.arange(0.1,1.0,0.1)
print(theta_values)


prior = np.ones(len(theta_values)) / len(theta_values)
print(prior)


log_likelihood = (
    s * np.log(theta_values) +
    nonsurv * np.log(1 - theta_values)
)
likelihood = np.exp(log_likelihood)
print(likelihood)


unnormalized_posterior = prior * likelihood
posterior = unnormalized_posterior / unnormalized_posterior.sum()
print(posterior)


results = pd.DataFrame({
    'theta_value': theta_values,
    'prior': prior,
    'likelihood': likelihood,
    'unnormalized_posterior': unnormalized_posterior,
    'posterior': posterior
})
print(results)



# ------------------------------------------------------------
# THE BEST VALUE OF THETA IS (0.7) AS THE POSTERIOR VALUE OF THETA (0.7) IS MAXIMUM
# ------------------------------------------------------------

posterior_mean = np.sum(theta_values * posterior)
print("Posterior mean: ",posterior_mean)


plt.figure(figsize=(8,5))

plt.plot(
    theta_values,
    prior,
    marker='o',
    linestyle='-',
    color='r',
    label='Prior'
)
plt.plot(
    theta_values,
    posterior,
    marker='o',
    linestyle='-',
    color='b',
    label='Posterior'
)
plt.xlabel('Possible Theta Value')
plt.ylabel('Probability')
plt.title('Bayesian Updating of Female Survival Probability')
plt.legend()
plt.grid(True)
plt.show()

