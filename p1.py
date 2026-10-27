#====================================================================
# Practical 1: Practical 1: Probability Simulations & Law of Large Numbers
#====================================================================

# --- [Question 1] Simulate 100 Coin Tosses & Compare with Theoretical Probability ---
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Simulate 100 coin tosses ('Head' or 'Tail')
tosses = np.random.choice(['Head', 'Tail'], size=100)

# Count frequencies
heads = np.sum(tosses == 'Head')
tails = np.sum(tosses == 'Tail')

# Calculate empirical probabilities
prob_heads = heads / len(tosses)
prob_tails = tails / len(tosses)

# Display results
print(f"Heads Count: {heads}")
print(f"Tails Count: {tails}")
print(f"Empirical P(Head): {prob_heads:.4f} | Theoretical P(Head): 0.5000")
print(f"Empirical P(Tail): {prob_tails:.4f} | Theoretical P(Tail): 0.5000")


# --- [Question 2] Demonstrate the Law of Large Numbers (Sample Sizes 10 to 100,000) ---
import numpy as np
import matplotlib.pyplot as plt

sample_sizes = [10, 100, 1000, 10000, 100000]
probabilities = []

np.random.seed(42)
print("--- Law of Large Numbers Convergence ---")
for n in sample_sizes:
    tosses = np.random.choice(['Head', 'Tail'], size=n)
    heads = np.sum(tosses == 'Head')
    prob = heads / n
    probabilities.append(prob)
    print(f"Tosses (n = {n:>6}): Heads = {heads:>5} | Empirical P(Head) = {prob:.5f}")

# Plotting the convergence graph
plt.figure(figsize=(10, 5))
plt.plot(sample_sizes, probabilities, marker='o', color='#0284c7', linewidth=2, label='Empirical P(Head)')
plt.axhline(y=0.5, color='#ef4444', linestyle='--', linewidth=2, label='Theoretical P(Head) = 0.5')
plt.xscale('log')
plt.xlabel("Number of Tosses (Log Scale)")
plt.ylabel("Empirical Probability of Heads")
plt.title("Law of Large Numbers: Convergence of Empirical Probability")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# --- [Question 3] Dice Roll Simulation (10,000 Rolls of a Fair 6-Sided Die) ---
import numpy as np

np.random.seed(42)

# Simulate 10,000 dice rolls (integers from 1 to 6)
rolls = np.random.randint(1, 7, size=10000)

# Calculate empirical probabilities
p_6 = np.mean(rolls == 6)
p_even = np.mean(rolls % 2 == 0)
p_greater_4 = np.mean(rolls > 4)
p_less_equal_3 = np.mean(rolls <= 3)

# Theoretical probabilities
theo_6 = 1 / 6
theo_even = 3 / 6
theo_greater_4 = 2 / 6
theo_less_equal_3 = 3 / 6

print(f"P(X = 6)     : Empirical = {p_6:.4f} | Theoretical = {theo_6:.4f}")
print(f"P(X is even) : Empirical = {p_even:.4f} | Theoretical = {theo_even:.4f}")
print(f"P(X > 4)     : Empirical = {p_greater_4:.4f} | Theoretical = {theo_greater_4:.4f}")
print(f"P(X <= 3)    : Empirical = {p_less_equal_3:.4f} | Theoretical = {theo_less_equal_3:.4f}")


# --- [Question 4] Frequency Distribution & Probability Bar Plot of a Die ---
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
rolls = np.random.randint(1, 7, size=10000)

# Calculate unique values, counts and empirical probabilities
values, counts = np.unique(rolls, return_counts=True)
probabilities = counts / len(rolls)

print("Face\tFrequency\tEmpirical Probability")
print("-" * 42)
for val, count, prob in zip(values, counts, probabilities):
    print(f"{val}\t{count}\t\t{prob:.4f}")

# Plot bar graph
plt.figure(figsize=(8, 4.5))
plt.bar(values, probabilities, color='#38bdf8', edgecolor='#0369a1', alpha=0.85, label='Empirical Probability')
plt.axhline(y=1/6, color='#ef4444', linestyle='--', label='Theoretical (1/6 ≈ 0.1667)')
plt.xlabel("Dice Outcome Face")
plt.ylabel("Empirical Probability")
plt.title("Empirical Probability Distribution of a Fair Die")
plt.xticks(values)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()


# --- [Question 5] Sum of Two Dice Simulation (10,000 Rolls) ---
import numpy as np

n = 10000
np.random.seed(42)

# Simulate rolling two dice
die1 = np.random.randint(1, 7, size=n)
die2 = np.random.randint(1, 7, size=n)
total = die1 + die2

# Calculate empirical probabilities
p_sum_2 = np.mean(total == 2)
p_sum_7 = np.mean(total == 7)
p_sum_12 = np.mean(total == 12)
p_greater_9 = np.mean(total > 9)

print(f"P(S = 2)  : Empirical = {p_sum_2:.4f} | Theoretical = 1/36 ≈ {1/36:.4f}")
print(f"P(S = 7)  : Empirical = {p_sum_7:.4f} | Theoretical = 6/36 ≈ {6/36:.4f}")
print(f"P(S = 12) : Empirical = {p_sum_12:.4f} | Theoretical = 1/36 ≈ {1/36:.4f}")
print(f"P(S > 9)  : Empirical = {p_greater_9:.4f} | Theoretical = 6/36 ≈ {6/36:.4f}")


# --- [Question 6] Complete Probability Distribution for Sum of Two Dice (100,000 Rolls) ---
import numpy as np
import matplotlib.pyplot as plt

n = 100000
np.random.seed(42)

# Roll two dice 100,000 times
die1 = np.random.randint(1, 7, size=n)
die2 = np.random.randint(1, 7, size=n)
total = die1 + die2

# Frequencies and empirical probabilities
sums, counts = np.unique(total, return_counts=True)
probabilities = counts / len(total)

print("Sum\tFrequency\tEmpirical Probability")
print("-" * 42)
for s, count, prob in zip(sums, counts, probabilities):
    print(f"{s:>2}\t{count:>7}\t\t{prob:.4f}")

# Plot bar distribution
plt.figure(figsize=(10, 5))
plt.bar(sums, probabilities, color='#818cf8', edgecolor='#4338ca', width=0.7)
plt.xlabel("Sum of Two Dice (S)")
plt.ylabel("Empirical Probability")
plt.title("Empirical Probability Distribution of the Sum of Two Dice (Triangular Distribution)")
plt.xticks(range(2, 13))
plt.grid(axis='y', alpha=0.3)
plt.show()

