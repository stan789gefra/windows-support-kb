"""
Practical 4: Practical 4
Description: Markov Chains & Customer Churn Modeling
Original File: Prac4.ipynb
"""

import numpy as np
import pandas as pd
states = ["New","Active","Churned"]
matrix_1=np.array([[0.50,0.40,0.10],[0.10,0.70,0.20],[0.00,0.00,1.00]]) # it always goes from row to column
transition_matrix=pd.DataFrame(matrix_1,columns=states,index=states)
print(transition_matrix)

print("\n Row Sum:- ")
print(matrix_1.sum(axis=1))


initial_distribution = np.array([1,0,0])
distribution_1 = initial_distribution @ matrix_1
print("Distribution after 1 period:- ")
for state, probability in zip(states, distribution_1):
    print(f"{state}: {probability:.2f}")



# ------------------------------------------------------------
# Q3) Prdict the customer-state distribution after 5 period
# ------------------------------------------------------------

distribution = initial_distribution.copy()
for _ in range(5):
    distribution = distribution @ matrix_1
print("Distribution after 5 periods:- ")
for state, probability in zip(states, distribution):
    print(f"{state}: {probability:.2f}")


np.random.seed(42)
current_state = 0
customer_history = [states[current_state]]
for _ in range(10):
  current_state = np.random.choice(len(states),p=matrix_1[current_state])
  customer_history.append(states[current_state])
print("Customer State History:- ")
print(customer_history)


np.random.seed(42)
n_customer =1000
n_period = 10

customers= np.zeros(n_customer, dtype=int)
results=[]
for _ in range(n_period+1):
  counts = np.bincount(customers,minlength=3)
  proportions = counts / n_customer

  results.append([_,proportions[0],proportions[1],proportions[2]])
  new_customers = np.array([np.random.choice(3,p=matrix_1[state]) for state in customers])
  customers = new_customers
  results_df=pd.DataFrame(results,columns=["Period","New","Active","Churned"])
print(results_df)


import matplotlib.pyplot as plt

plt.figure(figsize=(15,5))
plt.plot(results_df["Period"],results_df["New"],marker='o',label="New")
plt.plot(results_df["Period"],results_df["Active"],marker='o',label="Active")
plt.plot(results_df["Period"],results_df["Churned"],marker='o',label="Churned")
plt.xlabel("Period")
plt.ylabel("Proportion of customers")
plt.title("Markov Chain Simulation of Customer Behavior")
plt.legend()
plt.grid(True)
plt.show()


max_chrun_period= results_df.loc[results_df['Churned'].idxmax()]
print("Maximum Churn Period:- ")
print(max_chrun_period)

