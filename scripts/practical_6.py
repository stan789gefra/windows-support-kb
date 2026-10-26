"""
Practical 6: Practical 6
Description: Monte Carlo Simulation & Financial Risk Analysis (Value at Risk - VaR)
Original File: Prac6.ipynb
"""


# ------------------------------------------------------------
# Q1)
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

#portfolio informaion
initial_value = 1000000  # 10,00,000
mean_return = 0.0005  # 0.05%
sd_return = 0.015     # 1.5%
n_simulation = 10000

#monte Carlo simulation
returns = np.random.normal(
    loc=mean_return,
    scale=sd_return,
    size= n_simulation,
)

#simulated portfolio values
portfolio_values = initial_value * ( 1 + returns)

#simulated porfit/Loss
profit_loss = portfolio_values - initial_value

#calculate the probability of loss
probability_loss = np.mean(profit_loss < 0)

print("Probability of porfolio loss: ", probability_loss)
print("percentage of porfolio loss: ", probability_loss * 100)

#plot
plt.hist(returns, bins=50, edgecolor='darkblue', color='lightblue')
plt.title("Monte Carlo Simulation of Portfolio Returns")
plt.xlabel("Daily Portfolio Returns")
plt.ylabel("Frequency")
plt.show()



# ------------------------------------------------------------
# Q2)
# ------------------------------------------------------------

#5th percentile of profit /loss
Var_95 = np.percentile(profit_loss, 5)

print("95% Value at Rik (VaR) : ", abs(Var_95))

#plot profit/ loss distribution
plt.hist(profit_loss, bins=50, edgecolor='darkblue', color='lightblue')
plt.axvline(x=Var_95, color='red', linestyle='dashed', linewidth=2, label=f"95% VaR = {abs(Var_95):,.0f}")
plt.title("Monte Carlo Simulation of Portfolio Risk")
plt.xlabel("Loss / Profit (rupees)")
plt.ylabel("Frequency")
plt.show()
plt

