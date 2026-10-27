#====================================================================
# Practical 4: Practical 4: Discrete-Time Markov Chains (DTMC)
#====================================================================

# --- [Question 1 & 2] Transition Matrix Setup & 1-Period Customer State Distribution ---
import numpy as np
import pandas as pd

states = ["New", "Active", "Churned"]

# Transition Probability Matrix (Row to Column)
matrix_1 = np.array([
    [0.50, 0.40, 0.10],   # New
    [0.10, 0.70, 0.20],   # Active
    [0.00, 0.00, 1.00]    # Churned (Absorbing State)
])

# Create readable DataFrame
transition_matrix = pd.DataFrame(matrix_1, columns=states, index=states)
print("--- Transition Matrix P ---")
print(transition_matrix)

# Verify stochastic matrix property: each row sum must equal 1.0
print("\nRow Sums:", matrix_1.sum(axis=1))

# Initial state: 100% New customers
initial_distribution = np.array([1.0, 0.0, 0.0])

# Distribution after 1 period: v_1 = v_0 @ P
distribution_1 = initial_distribution @ matrix_1

print("\n--- State Distribution after 1 Period ---")
for state, prob in zip(states, distribution_1):
    print(f"{state:<8}: {prob:.4f}")


# --- [Question 3] Predict Customer State Distribution After 5 Periods ---
import numpy as np

states = ["New", "Active", "Churned"]
matrix_1 = np.array([
    [0.50, 0.40, 0.10],
    [0.10, 0.70, 0.20],
    [0.00, 0.00, 1.00]
])

initial_distribution = np.array([1.0, 0.0, 0.0])
distribution = initial_distribution.copy()

# Multiply by transition matrix 5 times
for step in range(1, 6):
    distribution = distribution @ matrix_1

print("--- Distribution after 5 Periods (v_5 = v_0 @ P^5) ---")
for state, prob in zip(states, distribution):
    print(f"{state:<8}: {prob:.4f}")


# --- [Question 4] Simulate Cohort of 1,000 Customers over 10 Periods ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n_customers = 1000
n_periods = 10

# All 1000 customers start at state 0 ('New')
customers = np.zeros(n_customers, dtype=int)
results = []

states = ["New", "Active", "Churned"]
matrix_1 = np.array([
    [0.50, 0.40, 0.10],
    [0.10, 0.70, 0.20],
    [0.00, 0.00, 1.00]
])

for period in range(n_periods + 1):
    counts = np.bincount(customers, minlength=3)
    proportions = counts / n_customers
    results.append([period, proportions[0], proportions[1], proportions[2]])
    
    # Transition each customer according to current state row probabilities
    customers = np.array([np.random.choice(3, p=matrix_1[s]) for s in customers])

results_df = pd.DataFrame(results, columns=["Period", "New", "Active", "Churned"])
print("--- Cohort Simulation Proportions Over 10 Periods ---")
print(results_df.to_string(index=False))

# Maximum churn period
max_churn_period = results_df.loc[results_df['Churned'].idxmax()]
print(f"\nMaximum Churn Occurred at Period: {int(max_churn_period['Period'])} (Churned = {max_churn_period['Churned']*100:.1f}%)")

# Plot trajectories
plt.figure(figsize=(10, 5))
plt.plot(results_df["Period"], results_df["New"], marker='o', color='#38bdf8', label="New")
plt.plot(results_df["Period"], results_df["Active"], marker='s', color='#10b981', label="Active")
plt.plot(results_df["Period"], results_df["Churned"], marker='^', color='#ef4444', label="Churned")
plt.xlabel("Period")
plt.ylabel("Proportion of Customers")
plt.title("Markov Chain Cohort Simulation of Customer Lifecycle")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

