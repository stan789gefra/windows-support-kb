#====================================================================
# Practical 6: Practical 6: Monte Carlo Simulation & Financial Risk (VaR)
#====================================================================

# --- [Question 1] Simulate Portfolio Daily Returns & Probability of Loss ---
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Portfolio setup
initial_value = 1000000   # ₹10,00,000
mean_return = 0.0005     # 0.05% expected daily return
sd_return = 0.015        # 1.5% daily volatility
n_simulations = 10000

# Monte Carlo simulation of daily returns
returns = np.random.normal(loc=mean_return, scale=sd_return, size=n_simulations)

# Simulated portfolio end values & profit/loss
portfolio_values = initial_value * (1 + returns)
profit_loss = portfolio_values - initial_value

# Probability of loss (Profit/Loss < 0)
prob_loss = np.mean(profit_loss < 0)

print(f"Probability of Portfolio Loss : {prob_loss:.4f} ({prob_loss * 100:.2f}%)")
print(f"Mean Simulated Profit/Loss    : ₹{np.mean(profit_loss):,.2f}")
print(f"Worst Simulated Loss          : ₹{np.min(profit_loss):,.2f}")
print(f"Best Simulated Gain           : ₹{np.max(profit_loss):,.2f}")

# Plotting Return Distribution
plt.figure(figsize=(9, 4.5))
plt.hist(returns, bins=50, edgecolor='#1e3a8a', color='#93c5fd', alpha=0.85)
plt.axvline(x=0, color='#ef4444', linestyle='--', label='Break-even (Return = 0)')
plt.title("Monte Carlo Simulation of Daily Portfolio Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# --- [Question 2] Calculate and Visualize 95% Value at Risk (VaR) ---
import numpy as np
import matplotlib.pyplot as plt

# 5th percentile of profit/loss corresponds to 95% confidence VaR
var_95 = np.percentile(profit_loss, 5)

print(f"95% Value at Risk (VaR): ₹{abs(var_95):,.2f}")
print(f"Interpretation: With 95% confidence, daily loss will NOT exceed ₹{abs(var_95):,.2f}.")

# Plot profit/loss distribution with VaR threshold
plt.figure(figsize=(10, 5))
plt.hist(profit_loss, bins=50, edgecolor='#0f172a', color='#38bdf8', alpha=0.7)
plt.axvline(x=var_95, color='#dc2626', linestyle='dashed', linewidth=2.5, 
            label=f"95% VaR = ₹{abs(var_95):,.0f}")
plt.axvline(x=0, color='#64748b', linestyle=':', label="Zero Profit/Loss")

plt.title("Portfolio Profit / Loss Distribution with 95% Value at Risk (VaR)")
plt.xlabel("Profit / Loss (₹)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

