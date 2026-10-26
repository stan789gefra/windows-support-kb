"""
Practical 2: Practical 2
Description: Probability Distributions & Parameter Estimation (Normal, Poisson, Exponential, Noise Analysis)
Original File: prac2.ipynb
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



# ------------------------------------------------------------
# Q1) A data analyst wants to model the distribution of examination scores.
# 
# 1. Generate 500 normally distributed observations with mean 70 and standard deviation 10.
# 2. Plot a histogram of the observations.
# 3. Fit a Normal distribution to the data.
# 4. Overlay the fitted Normal PDF on the histogram.
# 5. Report the estimated mean and standard deviation.
# ------------------------------------------------------------

np.random.seed(42)
data = np.random.normal(loc=70, scale=10,size=500)

#fit normal distribution
mu, sigma = stats.norm.fit(data)

#histogram
plt.hist(data, bins=20, density=True, alpha=0.6, color='g')

#fitted pdf
x = np.linspace(data.min(), data.max(), 300)
pdf = stats.norm.pdf(x, mu, sigma)
plt.plot(x, pdf, linewidth=2)
plt.xlabel("Examination Score")
plt.ylabel("Probability Density")
plt.title("Normal Distribution: Observed Data and Fitted PDF")
plt.show()

print("Estimated Mean:", mu)
print("Estimated Standard Deviation:",sigma)



# ------------------------------------------------------------
# Q2) A website receives a certain number of customer support requests per minute. Assume that the number of requests can be modelled using a Poisson distribution.
# 
# 1. Generate 500 observations assuming an average of 4 requests per minute.
# 2. Plot the frequency distribution.
# 3. Estimate the Poisson parameter λ
# 4. Overlay the fitted Poisson probabilities.
# 5. Compare the observed and fitted distributions.
# ------------------------------------------------------------

np.random.seed(42)
data=np.random.poisson(lam=4, size=500)

#estimated lambda
lambda_hat = np.mean(data)

#observed values
values, counts = np.unique(data, return_counts=True)
observed_prob = counts/ len(data)

#fitted poisson probabilities
fitted_prob = stats.poisson.pmf(values, lambda_hat)

#plot
plt.bar(values, observed_prob, alpha=0.6, label="Observed")
plt.plot(values, fitted_prob,'o-',linewidth=2, alpha=0.6, label="Fitted")

plt.xlabel("Number of Requests per Minute")
plt.ylabel("Probability")
plt.title("Poisson Distribution: Observed vs. Fitted")
plt.legend()
plt.show()

print("Estimated Lambda:", lambda_hat)



# ------------------------------------------------------------
# Q3) An online service records the waiting time, in minutes, between successive customer requests.
# 
# 1. Generate 500 observations from an Exponential distribution assuming an average waiting time of 5 minutes.
# 2. Plot a histogram.
# 3. Fit an Exponential distribution.
# 4. Overlay the fitted PDF.
# ------------------------------------------------------------

np.random.seed(42)
data= np.random.exponential(scale=5, size=500)

# fit exponential distribution
loc, scale = stats.expon.fit(data,floc=0)

#histogram
plt.hist(data, bins=20, density=True, alpha=0.6, color=(255/255, 87/255, 51/255))

#fitted pdf
x = np.linspace(0, data.max(), 300)
pdf = stats.expon.pdf(x, loc=loc, scale=scale)

plt.plot(x, pdf, linewidth=2)

plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Probability Density")
plt.title("Exponential Distribution: Observed Data and Fitted PDF")
plt.show()

print("Estimated Scale:", scale)
print("Estimated mean Waiting Time:",scale)



# ------------------------------------------------------------
# # Gaussian distribution = Normal Distribution
# ------------------------------------------------------------


# ------------------------------------------------------------
# Noise/Error()
# 
# ---
# 
# 
# noise= Actual-predicted
# ------------------------------------------------------------


# ------------------------------------------------------------
# Q4) Suppose we have measurements of a sensor:
# 
# X=[50,52,48,51,49,53,50,47,52,51]
# 
# In real-world applications, measurements may contain random noise. Assume the noise follows a Gaussian distribution:
# 
#   # ϵ∼N(0,4)
# 
# 1. Generate the Gaussian noise.
# 2. Obtain the noisy observations.
# 3. Compare the original and noisy data.
# 4. Visualize the effect of Gaussian noise.
# 5. Report the estimated scale parameter.
# ------------------------------------------------------------

data= np.array([50,52,48,51,49,53,50,47,52,51])
print("Original data: ")
print(data)


np.random.seed(42)
noise = np.random.normal(loc=0, scale=2, size=len(data))
print("Noisy data: ")
print(noise)


nosiy_data=data+noise

print("Original data: ")
print(data)
print("Noisy data: ")
print(nosiy_data)


plt.figure(figsize=(10,6))
plt.plot(data,marker='o',label="origianal data")
plt.plot(nosiy_data,marker="o",label="Data with Gaussian Noise")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.title("Effect of Gaussian Noise")
plt.legend()
plt.show()

