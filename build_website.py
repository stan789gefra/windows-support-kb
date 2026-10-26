# -*- coding: utf-8 -*-
"""
PSP MasterLab - Static Website Generator
Compiles all 8 Practicals into a single, highly polished, responsive index.html
with copyable code snippets, theory cards, and outputs.
"""

import html

practicals = [
    {
        "id": "prac1",
        "title": "Practical 1: Probability Simulations & Law of Large Numbers",
        "badge": "Prac 01",
        "filename": "pRAC_1.ipynb",
        "theory_title": "Core Theory: Classical vs. Empirical Probability & Law of Large Numbers (LLN)",
        "theory_desc": "Empirical probability estimates the likelihood of an event based on real observations (P(E) = n(E) / N). The Law of Large Numbers states that as the number of independent trials N approaches infinity, the empirical probability converges to the theoretical probability.",
        "questions": [
            {
                "qid": "p1_q1",
                "badge": "Question 1",
                "title": "Simulate 100 Coin Tosses & Compare with Theoretical Probability",
                "desc": "A fair coin is tossed 100 times. Simulate 100 coin tosses using NumPy. Count the number of Heads and Tails. Calculate the empirical probability of obtaining Head and Tail and compare them with the theoretical probabilities P(H) = 0.5, P(T) = 0.5.",
                "code": """import numpy as np

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
print(f"Empirical P(Tail): {prob_tails:.4f} | Theoretical P(Tail): 0.5000")""",
                "output": """Heads Count: 44
Tails Count: 56
Empirical P(Head): 0.4400 | Theoretical P(Head): 0.5000
Empirical P(Tail): 0.5600 | Theoretical P(Tail): 0.5000""",
                "viva": "Why doesn't the empirical probability exactly equal 0.5 for 100 tosses? Because 100 is a relatively small sample size subject to random sample variance. As N increases, random fluctuations average out."
            },
            {
                "qid": "p1_q2",
                "badge": "Question 2",
                "title": "Demonstrate the Law of Large Numbers (Sample Sizes 10 to 100,000)",
                "desc": "Repeat the coin-toss experiment for sample sizes n = 10, 100, 1,000, 10,000, and 100,000. Calculate the empirical probability of Heads for each sample size and plot the convergence curve against the theoretical probability line (y = 0.5).",
                "code": """import numpy as np
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
plt.show()""",
                "output": """--- Law of Large Numbers Convergence ---
Tosses (n =     10): Heads =     7 | Empirical P(Head) = 0.70000
Tosses (n =    100): Heads =    47 | Empirical P(Head) = 0.47000
Tosses (n =   1000): Heads =   493 | Empirical P(Head) = 0.49300
Tosses (n =  10000): Heads =  5076 | Empirical P(Head) = 0.50760
Tosses (n = 100000): Heads = 49937 | Empirical P(Head) = 0.49937""",
                "viva": "Notice how at n=10, P(Head)=0.70 (30% error), but by n=100,000, P(Head)=0.49937 (under 0.1% error). This proves the Law of Large Numbers."
            },
            {
                "qid": "p1_q3",
                "badge": "Question 3",
                "title": "Dice Roll Simulation (10,000 Rolls of a Fair 6-Sided Die)",
                "desc": "Simulate 10,000 rolls of a fair six-sided die where X denotes the outcome. Estimate: 1) P(X=6), 2) P(X is even), 3) P(X > 4), 4) P(X <= 3). Compare with theoretical values.",
                "code": """import numpy as np

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
print(f"P(X <= 3)    : Empirical = {p_less_equal_3:.4f} | Theoretical = {theo_less_equal_3:.4f}")""",
                "output": """P(X = 6)     : Empirical = 0.1657 | Theoretical = 0.1667
P(X is even) : Empirical = 0.5021 | Theoretical = 0.5000
P(X > 4)     : Empirical = 0.3346 | Theoretical = 0.3333
P(X <= 3)    : Empirical = 0.4982 | Theoretical = 0.5000""",
                "viva": "Why use np.mean(condition)? In Python, a boolean array evaluates True as 1 and False as 0. The mean of booleans equals the proportion of True values, directly computing empirical probability."
            },
            {
                "qid": "p1_q4",
                "badge": "Question 4",
                "title": "Frequency Distribution & Probability Bar Plot of a Die",
                "desc": "Calculate the frequency and empirical probability of each outcome {1, 2, 3, 4, 5, 6} across 10,000 rolls. Display as a table and plot the empirical probability distribution using a bar graph.",
                "code": """import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
rolls = np.random.randint(1, 7, size=10000)

# Calculate unique values, counts and empirical probabilities
values, counts = np.unique(rolls, return_counts=True)
probabilities = counts / len(rolls)

print("Face\\tFrequency\\tEmpirical Probability")
print("-" * 42)
for val, count, prob in zip(values, counts, probabilities):
    print(f"{val}\\t{count}\\t\\t{prob:.4f}")

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
plt.show()""",
                "output": """Face\tFrequency\tEmpirical Probability
------------------------------------------
1\t1665\t\t0.1665
2\t1692\t\t0.1692
3\t1625\t\t0.1625
4\t1672\t\t0.1672
5\t1689\t\t0.1689
6\t1657\t\t0.1657""",
                "viva": "Are all six outcomes approximately equally likely? Yes, each face lands roughly 16.6% of the time, aligning with the discrete uniform distribution."
            },
            {
                "qid": "p1_q5",
                "badge": "Question 5",
                "title": "Sum of Two Dice Simulation (10,000 Rolls)",
                "desc": "Two fair dice are rolled simultaneously 10,000 times. Let S = X1 + X2 be the sum of the two dice. Calculate empirical probabilities: P(S=2), P(S=7), P(S=12), and P(S > 9). Compare P(S=7) with theoretical probability (6/36 = 1/6).",
                "code": """import numpy as np

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
print(f"P(S > 9)  : Empirical = {p_greater_9:.4f} | Theoretical = 6/36 ≈ {6/36:.4f}")""",
                "output": """P(S = 2)  : Empirical = 0.0273 | Theoretical = 1/36 ≈ 0.0278
P(S = 7)  : Empirical = 0.1616 | Theoretical = 6/36 ≈ 0.1667
P(S = 12) : Empirical = 0.0275 | Theoretical = 1/36 ≈ 0.0278
P(S > 9)  : Empirical = 0.1689 | Theoretical = 6/36 ≈ 0.1667""",
                "viva": "Why is P(S=7) higher than P(S=2)? There are 6 combinations to sum to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). But only 1 combination makes 2: (1,1)."
            },
            {
                "qid": "p1_q6",
                "badge": "Question 6",
                "title": "Complete Probability Distribution for Sum of Two Dice (100,000 Rolls)",
                "desc": "Simulate 100,000 rolls of two dice. Calculate frequency and probability for every possible sum from 2 to 12. Plot the resulting triangular distribution.",
                "code": """import numpy as np
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

print("Sum\\tFrequency\\tEmpirical Probability")
print("-" * 42)
for s, count, prob in zip(sums, counts, probabilities):
    print(f"{s:>2}\\t{count:>7}\\t\\t{prob:.4f}")

# Plot bar distribution
plt.figure(figsize=(10, 5))
plt.bar(sums, probabilities, color='#818cf8', edgecolor='#4338ca', width=0.7)
plt.xlabel("Sum of Two Dice (S)")
plt.ylabel("Empirical Probability")
plt.title("Empirical Probability Distribution of the Sum of Two Dice (Triangular Distribution)")
plt.xticks(range(2, 13))
plt.grid(axis='y', alpha=0.3)
plt.show()""",
                "output": """Sum\tFrequency\tEmpirical Probability
------------------------------------------
 2\t   2798\t\t0.0280
 3\t   5501\t\t0.0550
 4\t   8328\t\t0.0833
 5\t  11041\t\t0.1104
 6\t  13924\t\t0.1392
 7\t  16569\t\t0.1657
 8\t  14172\t\t0.1417
 9\t  11032\t\t0.1103
10\t   8299\t\t0.0830
11\t   5602\t\t0.0560
12\t   2734\t\t0.0273""",
                "viva": "Does the simulated distribution resemble the theoretical distribution? Yes, it forms a symmetric triangular distribution peaking at S=7 with minimum probabilities at S=2 and S=12."
            }
        ]
    },
    {
        "id": "prac2",
        "title": "Practical 2: Continuous & Discrete Probability Distributions",
        "badge": "Prac 02",
        "filename": "prac2.ipynb",
        "theory_title": "Core Theory: Parametric Distribution Fitting via Maximum Likelihood Estimation (MLE)",
        "theory_desc": "Fitting a probability distribution involves finding parameter estimates (e.g., mean μ and variance σ² for Normal, rate λ for Poisson, scale β = 1/λ for Exponential) that maximize the likelihood of observing the empirical sample data.",
        "questions": [
            {
                "qid": "p2_q1",
                "badge": "Question 1",
                "title": "Normal Distribution: Modeling & Fitting Examination Scores",
                "desc": "1. Generate 500 normally distributed scores with mean 70 and standard deviation 10. 2. Plot a density histogram. 3. Fit a Normal distribution using stats.norm.fit. 4. Overlay the fitted PDF on the histogram. 5. Report estimated mean and std dev.",
                "code": """import numpy as np
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
print(f"Estimated Standard Deviation (σ): {sigma:.4f} (True: 10)")""",
                "output": """Estimated Mean (μ)              : 70.0684 (True: 70)
Estimated Standard Deviation (σ): 9.8027 (True: 10)""",
                "viva": "Why must density=True in plt.hist? Because the PDF represents probability density, where the total area under the curve equals 1. Setting density=True normalizes histogram bin heights so area sums to 1."
            },
            {
                "qid": "p2_q2",
                "badge": "Question 2",
                "title": "Poisson Distribution: Customer Support Requests per Minute",
                "desc": "1. Generate 500 observations assuming an average of 4 requests per minute (Poisson with λ=4). 2. Plot frequency distribution. 3. Estimate Poisson parameter λ. 4. Overlay fitted Poisson PMF probabilities.",
                "code": """import numpy as np
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

print(f"Estimated Lambda (λ): {lambda_hat:.4f} (True λ = 4)")""",
                "output": """Estimated Lambda (λ): 3.9320 (True λ = 4)""",
                "viva": "What is the key property of the Poisson distribution? In a theoretical Poisson distribution, the mean and variance are equal: E[X] = Var(X) = λ."
            },
            {
                "qid": "p2_q3",
                "badge": "Question 3",
                "title": "Exponential Distribution: Customer Waiting Time",
                "desc": "1. Generate 500 observations from an Exponential distribution assuming an average waiting time of 5 minutes (scale=5). 2. Plot histogram. 3. Fit Exponential distribution. 4. Overlay fitted PDF.",
                "code": """import numpy as np
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

print(f"Estimated Scale Parameter (Mean Wait Time): {scale:.4f} minutes (True: 5.0)")""",
                "output": """Estimated Scale Parameter (Mean Wait Time): 5.0215 minutes (True: 5.0)""",
                "viva": "What is the memoryless property of the Exponential distribution? P(X > s + t | X > s) = P(X > t). The probability of waiting an additional t minutes is independent of how long you have already waited."
            },
            {
                "qid": "p2_q4",
                "badge": "Question 4",
                "title": "Sensor Noise Modeling with Gaussian Distribution",
                "desc": "Given true sensor measurements X = [50, 52, 48, 51, 49, 53, 50, 47, 52, 51], model measurement noise following Gaussian noise ϵ ~ N(0, σ²=4) (σ = 2). Compare original vs noisy data and visualize effect.",
                "code": """import numpy as np
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
plt.show()""",
                "output": """Original Sensor Readings : [50 52 48 51 49 53 50 47 52 51]
Generated Gaussian Noise : [ 0.993 -0.277  1.295  3.046 -0.468 -0.468  3.158  1.535 -0.939  1.085]
Noisy Sensor Readings    : [50.993 51.723 49.295 54.046 48.532 52.532 53.158 48.535 51.061 52.085]""",
                "viva": "Why is sensor noise modeled using a Gaussian distribution? According to the Central Limit Theorem, when many microscopic independent random perturbations combine, their sum approaches a Gaussian distribution."
            }
        ]
    },
    {
        "id": "prac3",
        "title": "Practical 3: Joint, Marginal & Conditional Probability on Real Datasets",
        "badge": "Prac 03",
        "filename": "prac3.ipynb",
        "theory_title": "Core Theory: Contingency Tables, Joint & Conditional Probability",
        "theory_desc": "Joint Probability P(A ∩ B) is the probability that both events occur. Conditional Probability P(A | B) = P(A ∩ B) / P(B) is the probability of A given that B has occurred. Two events are statistically independent if and only if P(A ∩ B) = P(A) · P(B).",
        "questions": [
            {
                "qid": "p3_q1",
                "badge": "Titanic Part A",
                "title": "Titanic: Contingency Table & Survival by Gender",
                "desc": "Load the Titanic dataset. Construct a contingency table for sex vs. survival, then estimate: 1) Joint probability P(Female ∩ Survived), 2) Conditional probability P(Survived | Female), 3) Conditional probability P(Survived | Male).",
                "code": """import pandas as pd
import seaborn as sns

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Contingency table (counts)
table = pd.crosstab(df['sex'], df['survived'], margins=True)
print("--- Contingency Table: Sex vs. Survived ---")
print(table)

total = len(df)
female_survived = ((df['sex'] == 'female') & (df['survived'] == 1)).sum()
total_female = (df['sex'] == 'female').sum()
total_male = (df['sex'] == 'male').sum()
male_survived = ((df['sex'] == 'male') & (df['survived'] == 1)).sum()

# 1. Joint Probability
p_female_and_survived = female_survived / total

# 2. Conditional Probability P(Survived | Female)
p_survived_given_female = female_survived / total_female

# 3. Conditional Probability P(Survived | Male)
p_survived_given_male = male_survived / total_male

print(f"\\nJoint Probability P(Female ∩ Survived)     : {p_female_and_survived:.4f}")
print(f"Conditional Probability P(Survived | Female) : {p_survived_given_female:.4f}")
print(f"Conditional Probability P(Survived | Male)   : {p_survived_given_male:.4f}")""",
                "output": """--- Contingency Table: Sex vs. Survived ---
survived    0    1  All
sex                    
female     81  233  314
male      468  109  577
All       549  342  891

Joint Probability P(Female ∩ Survived)     : 0.2615
Conditional Probability P(Survived | Female) : 0.7420
Conditional Probability P(Survived | Male)   : 0.1889""",
                "viva": "What does P(Survived | Female) = 74.2% vs P(Survived | Male) = 18.9% signify? It demonstrates strong statistical dependence between gender and survival due to the 'women and children first' evacuation policy."
            },
            {
                "qid": "p3_q2",
                "badge": "Titanic Part B",
                "title": "Titanic: Probability of Survival Conditional on Passenger Class",
                "desc": "Estimate the conditional probability of survival given passenger class (First, Second, Third) using groupby().",
                "code": """import seaborn as sns

df = sns.load_dataset('titanic')

# Survival rate grouped by Passenger Class
survival_by_class = df.groupby('class', observed=False)['survived'].mean()

print("--- Conditional Probability: P(Survived | Pclass) ---")
for pclass, rate in survival_by_class.items():
    print(f"P(Survived | {pclass:<6} Class) : {rate:.4f} ({rate*100:.1f}%)")""",
                "output": """--- Conditional Probability: P(Survived | Pclass) ---
P(Survived | First  Class) : 0.6296 (63.0%)
P(Survived | Second Class) : 0.4728 (47.3%)
P(Survived | Third  Class) : 0.2424 (24.2%)""",
                "viva": "Notice that First Class passengers had more than 2.5x higher survival probability than Third Class passengers, confirming socioeconomic privilege in emergency rescue."
            },
            {
                "qid": "p3_q3",
                "badge": "Penguins Part A",
                "title": "Palmer Penguins: Contingency Table & Joint Probabilities",
                "desc": "Load the Palmer Penguins dataset. Construct a contingency table for Species vs. Island. Compute: 1) P(Adelie ∩ Dream), 2) P(Gentoo ∩ Biscoe).",
                "code": """import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

# Contingency table
contingency_table = pd.crosstab(df['species'], df['island'], margins=True)
print("--- Contingency Table: Species vs. Island ---")
print(contingency_table)

total = len(df)
adelie_dream = ((df['species'] == 'Adelie') & (df['island'] == 'Dream')).sum()
gentoo_biscoe = ((df['species'] == 'Gentoo') & (df['island'] == 'Biscoe')).sum()

p_adelie_dream = adelie_dream / total
p_gentoo_biscoe = gentoo_biscoe / total

print(f"\\nP(Adelie ∩ Dream Island) : {p_adelie_dream:.4f}")
print(f"P(Gentoo ∩ Biscoe Island): {p_gentoo_biscoe:.4f}")""",
                "output": """--- Contingency Table: Species vs. Island ---
island     Biscoe  Dream  Torgersen  All
species                                 
Adelie         44     56         52  152
Chinstrap       0     68          0   68
Gentoo        124      0          0  124
All           168    124         52  344

P(Adelie ∩ Dream Island) : 0.1628
P(Gentoo ∩ Biscoe Island): 0.3605""",
                "viva": "Look closely at the table: All 124 Gentoo penguins live on Biscoe Island, and all 68 Chinstrap penguins live on Dream Island. Only Adelie penguins inhabit all three islands."
            },
            {
                "qid": "p3_q4",
                "badge": "Penguins Part B",
                "title": "Palmer Penguins: Conditional Probabilities",
                "desc": "Calculate: 1) P(Adelie | Dream Island), 2) P(Male | Gentoo Species).",
                "code": """import seaborn as sns

df = sns.load_dataset('penguins')

# 1. P(Adelie | Dream)
dream_count = (df['island'] == 'Dream').sum()
adelie_and_dream = ((df['species'] == 'Adelie') & (df['island'] == 'Dream')).sum()
p_adelie_given_dream = adelie_and_dream / dream_count

# 2. P(Male | Gentoo)
gentoo_count = (df['species'] == 'Gentoo').sum()
male_and_gentoo = ((df['sex'] == 'Male') & (df['species'] == 'Gentoo')).sum()
p_male_given_gentoo = male_and_gentoo / gentoo_count

print(f"P(Adelie | Dream Island) : {p_adelie_given_dream:.4f} (56 / 124)")
print(f"P(Male | Gentoo Species) : {p_male_given_gentoo:.4f} (61 / 124)")""",
                "output": """P(Adelie | Dream Island) : 0.4516 (56 / 124)
P(Male | Gentoo Species) : 0.4919 (61 / 124)""",
                "viva": "Why does P(Male | Gentoo) equal 49.19%? Because in nature, the sex ratio of penguins is approximately 1:1 (50% male, 50% female)."
            },
            {
                "qid": "p3_q5",
                "badge": "Penguins Part C",
                "title": "Statistical Independence Test: P(A ∩ B) vs P(A) · P(B)",
                "desc": "Test whether Species and Island are statistically independent using: P(A ∩ B) = P(A) · P(B). Let A = Penguin is Gentoo, B = Penguin is on Biscoe Island.",
                "code": """import seaborn as sns

df = sns.load_dataset('penguins')
total = len(df)

# Probabilities
p_A = (df['species'] == 'Gentoo').sum() / total
p_B = (df['island'] == 'Biscoe').sum() / total
p_A_and_B = ((df['species'] == 'Gentoo') & (df['island'] == 'Biscoe')).sum() / total

product = p_A * p_B

print(f"P(Gentoo)            : {p_A:.4f}")
print(f"P(Biscoe)            : {p_B:.4f}")
print(f"P(Gentoo ∩ Biscoe)   : {p_A_and_B:.4f}")
print(f"P(Gentoo) * P(Biscoe): {product:.4f}")
print(f"Are Species and Island independent? {abs(p_A_and_B - product) < 1e-5}")""",
                "output": """P(Gentoo)            : 0.3605
P(Biscoe)            : 0.4884
P(Gentoo ∩ Biscoe)   : 0.3605
P(Gentoo) * P(Biscoe): 0.1760
Are Species and Island independent? False""",
                "viva": "Why are they not independent? Because P(A ∩ B) = 0.3605 is vastly different from P(A) · P(B) = 0.1760. Knowing a penguin is Gentoo dramatically increases the probability that it is on Biscoe Island (to 100%)."
            }
        ]
    },
    {
        "id": "prac4",
        "title": "Practical 4: Discrete-Time Markov Chains (DTMC)",
        "badge": "Prac 04",
        "filename": "Prac4.ipynb",
        "theory_title": "Core Theory: Discrete-Time Markov Chains & State Transition Dynamics",
        "theory_desc": "A Markov chain satisfies the Markov property: the future state depends only on the current state. The transition matrix P defines P_ij = P(X_t+1 = j | X_t = i). The state probability vector after t periods is given by Chapman-Kolmogorov: v_t = v_0 · P^t.",
        "questions": [
            {
                "qid": "p4_q1",
                "badge": "Question 1 & 2",
                "title": "Transition Matrix Setup & 1-Period Customer State Distribution",
                "desc": "Define customer states S = ['New', 'Active', 'Churned']. Matrix: New -> [0.5, 0.4, 0.1], Active -> [0.1, 0.7, 0.2], Churned -> [0.0, 0.0, 1.0]. Check row sums. For initial customer vector v0 = [1, 0, 0], compute state distribution after 1 period.",
                "code": """import numpy as np
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
print("\\nRow Sums:", matrix_1.sum(axis=1))

# Initial state: 100% New customers
initial_distribution = np.array([1.0, 0.0, 0.0])

# Distribution after 1 period: v_1 = v_0 @ P
distribution_1 = initial_distribution @ matrix_1

print("\\n--- State Distribution after 1 Period ---")
for state, prob in zip(states, distribution_1):
    print(f"{state:<8}: {prob:.4f}")""",
                "output": """--- Transition Matrix P ---
         New  Active  Churned
New      0.5     0.4      0.1
Active   0.1     0.7      0.2
Churned  0.0     0.0      1.0

Row Sums: [1. 1. 1.]

--- State Distribution after 1 Period ---
New     : 0.5000
Active  : 0.4000
Churned : 0.1000""",
                "viva": "What is an absorbing state in a Markov chain? A state that once entered cannot be left. Here, row 3 is [0, 0, 1], meaning once a customer is 'Churned', they remain churned forever (P_33 = 1)."
            },
            {
                "qid": "p4_q2",
                "badge": "Question 3",
                "title": "Predict Customer State Distribution After 5 Periods",
                "desc": "Starting from initial distribution v0 = [1, 0, 0], compute the customer state distribution after 5 periods using matrix multiplication v5 = v0 · P^5.",
                "code": """import numpy as np

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
    print(f"{state:<8}: {prob:.4f}")""",
                "output": """--- Distribution after 5 Periods (v_5 = v_0 @ P^5) ---
New     : 0.1130
Active  : 0.3375
Churned : 0.5495""",
                "viva": "What trend do you see after 5 periods? The proportion of 'New' customers drops from 100% to 11.3%, while 'Churned' steadily climbs to 54.95% due to the absorbing barrier."
            },
            {
                "qid": "p4_q3",
                "badge": "Question 4",
                "title": "Simulate Cohort of 1,000 Customers over 10 Periods",
                "desc": "Simulate 1,000 individual customers over 10 periods. Track proportions of New, Active, Churned at each step, plot customer behavior trajectories, and find the maximum churn period.",
                "code": """import numpy as np
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
print(f"\\nMaximum Churn Occurred at Period: {int(max_churn_period['Period'])} (Churned = {max_churn_period['Churned']*100:.1f}%)")

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
plt.show()""",
                "output": """--- Cohort Simulation Proportions Over 10 Periods ---
 Period   New  Active  Churned
      0 1.000   0.000    0.000
      1 0.503   0.397    0.100
      2 0.284   0.491    0.225
      3 0.193   0.456    0.351
      4 0.145   0.389    0.466
      5 0.113   0.338    0.549
      6 0.084   0.275    0.641
      7 0.068   0.230    0.702
      8 0.069   0.191    0.740
      9 0.058   0.164    0.778
     10 0.046   0.136    0.818

Maximum Churn Occurred at Period: 10 (Churned = 81.8%)""",
                "viva": "Why does the churned proportion monotonically increase? Because Churned has probability 1.0 of remaining Churned. Eventually, as t -> ∞, the entire population will be absorbed into Churned (stationary distribution = [0, 0, 1])."
            }
        ]
    },
    {
        "id": "prac5",
        "title": "Practical 5: Hidden Markov Models (HMM) & NLP Inference",
        "badge": "Prac 05",
        "filename": "Prac5.ipynb",
        "theory_title": "Core Theory: Hidden Markov Models (HMM) & Sequence Likelihood",
        "theory_desc": "An HMM consists of hidden states S (e.g., parts of speech), observable symbols V (e.g., words), initial probabilities π, transition probabilities A, and emission probabilities B. The joint probability of state sequence S and observation O is: P(S, O) = π(s₁) B(o₁|s₁) ∏ A(s_t|s_t-1) B(o_t|s_t).",
        "questions": [
            {
                "qid": "p5_q1",
                "badge": "Question 1",
                "title": "HMM Model Setup & Matrix Probability Verification",
                "desc": "Hidden states: ['Noun', 'Verb']. Observations: ['dogs', 'barks', 'loudly']. Set up Initial probabilities π = [0.6, 0.4], Transition matrix A, and Emission matrix B. Verify row sums.",
                "code": """import numpy as np
import pandas as pd

# Hidden States (e.g., Part of Speech)
states = ['Noun', 'Verb']

# Observed Words
observation = ['dogs', 'barks', 'loudly']

# Initial State Probabilities π: P(Noun)=0.6, P(Verb)=0.4
initial_prob = np.array([0.6, 0.4])

# State Transition Matrix A (Rows = from_state, Columns = to_state)
transition_prob = np.array([
    [0.3, 0.7],   # Noun -> [Noun, Verb]
    [0.6, 0.4]    # Verb -> [Noun, Verb]
])

# Emission Probability Matrix B (Rows = hidden_state, Columns = observation)
emission_prob = np.array([
    [0.7, 0.2, 0.1],   # Noun -> ['dogs', 'barks', 'loudly']
    [0.1, 0.6, 0.3]    # Verb -> ['dogs', 'barks', 'loudly']
])

print("--- Initial Probabilities (π) ---")
print(pd.Series(initial_prob, index=states))

print("\\n--- Transition Probability Matrix (A) ---")
print(pd.DataFrame(transition_prob, index=states, columns=states))

print("\\n--- Emission Probability Matrix (B) ---")
print(pd.DataFrame(emission_prob, index=states, columns=observation))

# Sanity Check
print("\\nSum of initial probabilities   :", initial_prob.sum())
print("Sum of transition probabilities :", transition_prob.sum(axis=1))
print("Sum of emission probabilities   :", emission_prob.sum(axis=1))""",
                "output": """--- Initial Probabilities (π) ---
Noun    0.6
Verb    0.4
dtype: float64

--- Transition Probability Matrix (A) ---
      Noun  Verb
Noun   0.3   0.7
Verb   0.6   0.4

--- Emission Probability Matrix (B) ---
      dogs  barks  loudly
Noun   0.7    0.2     0.1
Verb   0.1    0.6     0.3

Sum of initial probabilities   : 1.0
Sum of transition probabilities : [1. 1.]
Sum of emission probabilities   : [1. 1.]""",
                "viva": "What is the difference between transition probability and emission probability? Transition probability P(s_t | s_t-1) is the chance of moving from one hidden state to another. Emission probability P(o_t | s_t) is the chance of observing a specific word given a hidden state."
            },
            {
                "qid": "p5_q2",
                "badge": "Question 2",
                "title": "Calculate Marginal Probability of Observation P('dogs')",
                "desc": "Using the Law of Total Probability, calculate the marginal probability of observing 'dogs': P(dogs) = P(Noun)·P(dogs|Noun) + P(Verb)·P(dogs|Verb).",
                "code": """# Index of observation 'dogs'
dogs_idx = observation.index("dogs")

# P(Noun ∩ dogs) = P(Noun) * P(dogs | Noun)
p_noun_dogs = initial_prob[0] * emission_prob[0, dogs_idx]

# P(Verb ∩ dogs) = P(Verb) * P(dogs | Verb)
p_verb_dogs = initial_prob[1] * emission_prob[1, dogs_idx]

# Total Marginal Probability P(dogs)
p_dogs_total = p_noun_dogs + p_verb_dogs

print(f"P(Noun) * P(dogs | Noun) = {initial_prob[0]:.2f} * {emission_prob[0, dogs_idx]:.2f} = {p_noun_dogs:.4f}")
print(f"P(Verb) * P(dogs | Verb) = {initial_prob[1]:.2f} * {emission_prob[1, dogs_idx]:.2f} = {p_verb_dogs:.4f}")
print(f"\\nTotal P('dogs') = {p_noun_dogs:.4f} + {p_verb_dogs:.4f} = {p_dogs_total:.4f}")""",
                "output": """P(Noun) * P(dogs | Noun) = 0.60 * 0.70 = 0.4200
P(Verb) * P(dogs | Verb) = 0.40 * 0.10 = 0.0400

Total P('dogs') = 0.4200 + 0.0400 = 0.4600""",
                "viva": "If you observe 'dogs', is it more likely a Noun or a Verb? P(Noun | dogs) = 0.42 / 0.46 ≈ 91.3%. It is overwhelmingly likely to be a Noun."
            },
            {
                "qid": "p5_q3",
                "badge": "Question 3",
                "title": "Calculate Joint Probability of Sequence: 'Noun -> Verb' & 'dogs -> barks'",
                "desc": "Calculate joint probability for hidden state sequence (Noun -> Verb) and observation sequence ('dogs' -> 'barks') using: P = P(Noun) · P(dogs|Noun) · P(Verb|Noun) · P(barks|Verb).",
                "code": """# Sequence definition
state_1, state_2 = "Noun", "Verb"
obs_1, obs_2 = "dogs", "barks"

s1_idx = states.index(state_1)
s2_idx = states.index(state_2)
o1_idx = observation.index(obs_1)
o2_idx = observation.index(obs_2)

# Compute individual probability factors
p_initial = initial_prob[s1_idx]                       # P(Noun)
p_emit_1 = emission_prob[s1_idx, o1_idx]               # P(dogs | Noun)
p_trans = transition_prob[s1_idx, s2_idx]              # P(Verb | Noun)
p_emit_2 = emission_prob[s2_idx, o2_idx]               # P(barks | Verb)

# Joint Sequence Probability
joint_seq_prob = p_initial * p_emit_1 * p_trans * p_emit_2

print(f"1. P(Noun)         = {p_initial:.4f}")
print(f"2. P(dogs | Noun)  = {p_emit_1:.4f}")
print(f"3. P(Verb | Noun)  = {p_trans:.4f}")
print(f"4. P(barks | Verb) = {p_emit_2:.4f}")
print("-" * 35)
print(f"Joint Sequence Probability P(S, O) = {joint_seq_prob:.6f} ({joint_seq_prob*100:.2f}%)")""",
                "output": """1. P(Noun)         = 0.6000
2. P(dogs | Noun)  = 0.7000
3. P(Verb | Noun)  = 0.7000
4. P(barks | Verb) = 0.6000
-----------------------------------
Joint Sequence Probability P(S, O) = 0.176400 (17.64%)""",
                "viva": "Why do HMM sequence probabilities become small quickly as sentence length increases? Because it is a product of probabilities in (0, 1). In production POS taggers (Viterbi algorithm), calculations are converted to log-space: log P = ∑ log(p)."
            }
        ]
    },
    {
        "id": "prac6",
        "title": "Practical 6: Monte Carlo Simulation & Financial Risk (VaR)",
        "badge": "Prac 06",
        "filename": "Prac6.ipynb",
        "theory_title": "Core Theory: Monte Carlo Methods & Value at Risk (VaR)",
        "theory_desc": "Monte Carlo simulation models uncertainty by generating thousands of random market trajectories. The 95% Value at Risk (VaR) identifies the 5th percentile of the profit/loss distribution: the maximum expected loss at a 95% confidence level over a given horizon.",
        "questions": [
            {
                "qid": "p6_q1",
                "badge": "Question 1",
                "title": "Simulate Portfolio Daily Returns & Probability of Loss",
                "desc": "A portfolio has an initial value of ₹10,00,000 ($1,000,000). Assume daily returns follow N(μ=0.0005, σ=0.015). Run 10,000 Monte Carlo simulations. Compute simulated portfolio values, profit/loss, and probability of suffering a loss.",
                "code": """import numpy as np
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
plt.show()""",
                "output": """Probability of Portfolio Loss : 0.4874 (48.74%)
Mean Simulated Profit/Loss    : ₹473.47
Worst Simulated Loss          : ₹-57,406.87
Best Simulated Gain           : ₹58,746.43""",
                "viva": "Why is the probability of loss 48.74% when the mean return is positive (+0.05%)? Because the standard deviation (1.5%) is 30 times larger than the mean return (0.05%), causing a substantial portion of the bell curve to fall below zero."
            },
            {
                "qid": "p6_q2",
                "badge": "Question 2",
                "title": "Calculate and Visualize 95% Value at Risk (VaR)",
                "desc": "Calculate the 95% Value at Risk (VaR) by finding the 5th percentile of the profit/loss distribution. Plot the profit/loss distribution and annotate the 95% VaR threshold line.",
                "code": """import numpy as np
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
plt.show()""",
                "output": """95% Value at Risk (VaR): ₹24,322.87
Interpretation: With 95% confidence, daily loss will NOT exceed ₹24,322.87.""",
                "viva": "What is the business value of VaR in risk management? Banks and hedge funds use VaR to set regulatory capital reserves, ensuring they hold enough liquid cash to survive severe market drawdowns."
            }
        ]
    },
    {
        "id": "prac7",
        "title": "Practical 7: Bayesian Parameter Estimation",
        "badge": "Prac 07",
        "filename": "Prac7.ipynb",
        "theory_title": "Core Theory: Bayesian Updating & Grid Approximation",
        "theory_desc": "Bayes' Theorem updates belief upon observing data D: P(θ | D) ∝ P(D | θ) · P(θ). When dealing with large binomial counts, log-likelihood ln L(θ) = s ln(θ) + (n-s) ln(1-θ) prevents arithmetic underflow. The Maximum A Posteriori (MAP) estimate maximizes P(θ | D).",
        "questions": [
            {
                "qid": "p7_q1",
                "badge": "Question 1",
                "title": "Estimate Female Survival Rate θ on Titanic via Bayesian Grid Updating",
                "desc": "Extract female passengers on Titanic (n=314, s=233 survived, 81 died). Discretize parameter θ in [0.1, 0.9]. Set a uniform prior P(θ) = 1/9. Compute Binomial log-likelihood, likelihood, unnormalized posterior, and normalized posterior. Report the MAP estimate and posterior mean.",
                "code": """import pandas as pd
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
print("\\n--- Bayesian Updating Table ---")
print(results.to_string(index=False))

# 7. MAP Estimate and Posterior Mean
map_index = np.argmax(posterior)
best_theta = theta_values[map_index]
posterior_mean = np.sum(theta_values * posterior)

print(f"\\nMaximum A Posteriori (MAP) Estimate : θ* = {best_theta:.1f} (Posterior = {posterior[map_index]*100:.2f}%)")
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
plt.show()""",
                "output": """Total Female Passengers (n) : 314
Survived (s)                : 233
Not Survived (n - s)        : 81

--- Bayesian Updating Table ---
 Theta (θ)  Prior  Posterior
       0.1 0.1111   0.000000
       0.2 0.1111   0.000000
       0.3 0.1111   0.000000
       0.4 0.1111   0.000000
       0.5 0.1111   0.000000
       0.6 0.1111   0.000003
       0.7 0.1111   0.849392
       0.8 0.1111   0.150605
       0.9 0.1111   0.000000

Maximum A Posteriori (MAP) Estimate : θ* = 0.7 (Posterior = 84.94%)
Posterior Mean E[θ | Data]          : 0.7151""",
                "viva": "Why was θ = 0.7 selected as best? Because the sample survival rate is 233/314 ≈ 74.2%. On our discrete grid [0.1 ... 0.9], 0.7 has the highest posterior probability (84.94%), closely followed by 0.8 (15.06%)."
            }
        ]
    },
    {
        "id": "prac8",
        "title": "Practical 8: PageRank Algorithm & Random Walk on Graphs",
        "badge": "Prac 08",
        "filename": "Prac8.ipynb",
        "theory_title": "Core Theory: PageRank, Markov Chains & The Random Surfer Model",
        "theory_desc": "PageRank treats the web as a directed graph where hyperlinks are votes of authority. It models a random surfer who clicks outgoing links with probability d (damping factor, typically 0.85) or jumps to a random page with probability (1 - d). The steady-state visit probability is the principal eigenvector.",
        "questions": [
            {
                "qid": "p8_q1",
                "badge": "Network 1",
                "title": "Simulate Random Walk & Compute PageRank on 4-Node Web Graph",
                "desc": "Construct directed graph G with edges: (A,B), (A,C), (B,C), (B,D), (C,A), (C,D), (D,A), (D,C). 1. Visualize network. 2. Simulate 20-step random walk from 'A'. 3. Count node visits. 4. Compute exact PageRank with nx.pagerank.",
                "code": """import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

# Set random seed
random.seed(42)

# Create directed graph
G1 = nx.DiGraph()
edges_1 = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "A"), ("C", "D"),
    ("D", "A"), ("D", "C")
]
G1.add_edges_from(edges_1)

# Visualize Graph
plt.figure(figsize=(7, 5))
pos = nx.spring_layout(G1, seed=42)
nx.draw(G1, pos, with_labels=True, node_color='#38bdf8', node_size=2000, 
        font_size=14, font_weight='bold', arrows=True, arrowsize=20, edge_color='#64748b')
plt.title("Network 1: Directed Webpage Network")
plt.show()

# 2. Simulate Random Walk of 20 steps starting at page 'A'
current = 'A'
walk = [current]
for _ in range(20):
    neighbours = list(G1.successors(current))
    current = random.choice(neighbours)
    walk.append(current)

print("Random Walk Sequence (20 steps):", walk)

# 3. Count visits
visit_counts = Counter(walk)
print("\\nVisit Counts during Random Walk:")
for page in sorted(G1.nodes()):
    print(f"Page {page}: {visit_counts[page]} visits")

# 4. Compute PageRank
pagerank_1 = nx.pagerank(G1, alpha=0.85)
print("\\n--- Stationary PageRank Scores ---")
for page, score in sorted(pagerank_1.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {page}: {score:.4f} ({score*100:.2f}%)")""",
                "output": """Random Walk Sequence (20 steps): ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'A', 'B', 'D', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'C', 'A', 'C', 'D']

Visit Counts during Random Walk:
Page A: 7 visits
Page B: 5 visits
Page C: 6 visits
Page D: 3 visits

--- Stationary PageRank Scores ---
Page C: 0.3246 (32.46%)
Page A: 0.2781 (27.81%)
Page D: 0.2416 (24.16%)
Page B: 0.1557 (15.57%)""",
                "viva": "Why does Page C have the highest PageRank? Because Page C receives incoming links from both A and B, plus D. Since important pages point to C, C acquires the highest stationary authority."
            },
            {
                "qid": "p8_q2",
                "badge": "Network 2",
                "title": "PageRank on Alternative Web Topology (25-Step Walk from 'B')",
                "desc": "Construct directed graph G2 with edges: (A,B), (A,D), (B,C), (B,D), (C,A), (C,D), (D,B). Simulate 25-step random walk starting at 'B'. Compare visit counts and PageRank.",
                "code": """import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

random.seed(42)

# Create second directed graph topology
G2 = nx.DiGraph()
edges_2 = [
    ("A", "B"), ("A", "D"),
    ("B", "C"), ("B", "D"),
    ("C", "A"), ("C", "D"),
    ("D", "B")
]
G2.add_edges_from(edges_2)

# Simulate 25-step random walk starting at 'B'
current = 'B'
walk_2 = [current]
for _ in range(25):
    neighbours = list(G2.successors(current))
    current = random.choice(neighbours)
    walk_2.append(current)

print("Random Walk Sequence (25 steps):", walk_2)

# Count visits
visit_counts_2 = Counter(walk_2)
print("\\nVisit Counts during Random Walk:")
for page in sorted(G2.nodes()):
    print(f"Page {page}: {visit_counts_2[page]} visits")

# Compute PageRank
pagerank_2 = nx.pagerank(G2, alpha=0.85)
print("\\n--- Stationary PageRank Scores ---")
for page, score in sorted(pagerank_2.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {page}: {score:.4f} ({score*100:.2f}%)")""",
                "output": """Random Walk Sequence (25 steps): ['B', 'C', 'A', 'D', 'B', 'C', 'A', 'B', 'C', 'D', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'D', 'B', 'D', 'B', 'C', 'A', 'D', 'B', 'D']

Visit Counts during Random Walk:
Page A: 5 visits
Page B: 9 visits
Page C: 6 visits
Page D: 6 visits

--- Stationary PageRank Scores ---
Page B: 0.3640 (36.40%)
Page D: 0.3246 (32.46%)
Page C: 0.1922 (19.22%)
Page A: 0.1192 (11.92%)""",
                "viva": "Why does Page B rank highest in Network 2? Notice edge (D, B): Node D has only ONE outgoing link, which points directly to B! So 100% of D's high incoming traffic funnels straight into B, driving B to the top rank."
            }
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Microsoft Support: Windows &amp; PC Help</title>
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon.png">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='1' y='1' width='10.5' height='10.5' fill='%23f25022'/%3E%3Crect x='12.5' y='1' width='10.5' height='10.5' fill='%237fba00'/%3E%3Crect x='1' y='12.5' width='10.5' height='10.5' fill='%2300a4ef'/%3E%3Crect x='12.5' y='12.5' width='10.5' height='10.5' fill='%23ffb900'/%3E%3C/svg%3E">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <div class="logo-area">
      <button class="btn-icon menu-toggle-btn" id="menuToggle" title="Toggle Navigation Menu">&#9776;</button>
      <div class="logo-icon-wrapper" title="Microsoft Support">
        <svg class="ms-logo-svg" width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="1" y="1" width="10.5" height="10.5" fill="#f25022"/>
          <rect x="12.5" y="1" width="10.5" height="10.5" fill="#7fba00"/>
          <rect x="1" y="12.5" width="10.5" height="10.5" fill="#00a4ef"/>
          <rect x="12.5" y="12.5" width="10.5" height="10.5" fill="#ffb900"/>
        </svg>
      </div>
      <div class="logo-text">
        <h1>Microsoft Support</h1>
      </div>
      <span class="logo-badge">PC Help &amp; Diagnostics</span>
    </div>

    <div class="header-controls">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" placeholder="Search questions, codes...">
        <span class="search-count-badge" id="searchCount">0</span>
        <span class="search-shortcut">Ctrl+K</span>
      </div>
      <button class="btn-icon" id="themeToggle" title="Toggle Theme">☀️</button>
    </div>
  </header>

  <!-- App Body Layout -->
  <div class="app-container">
    
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-heading">Navigation / Lab Practicals</div>
      {nav_items}
    </aside>

    <!-- Main Content Stream -->
    <main class="main-content">
      
      <!-- Hero Banner -->
      <section class="hero-banner">
        <h2 class="hero-title">Probability & Stochastic Processes Hub</h2>
        <p class="hero-desc">
          Interactive practical repository containing verified Python implementations, mathematical formulations, complete outputs, and viva explanations for Practicals 1 through 8.
        </p>
        <div class="hero-stats">
          <div class="stat-pill"><span class="stat-num">8</span> Total Practicals</div>
          <div class="stat-pill"><span class="stat-num">25+</span> Problem Solutions</div>
          <div class="stat-pill"><span class="stat-num">100%</span> Copyable Clean Code</div>
          <div class="stat-pill"><span class="stat-num">NumPy / SciPy</span> Verified</div>
        </div>
      </section>

      <!-- Practicals Sections -->
      {sections_html}

    </main>
  </div>

  <!-- Scroll to Top Button -->
  <button class="scroll-top-btn" id="scrollTopBtn" title="Back to Top">&#8593;</button>

  <script src="app.js"></script>
</body>
</html>
"""

# Build Navigation HTML
nav_items_list = []
sections_list = []

disguise_kb_map = {
    "prac1": "support-information-repair-kb30214",
    "prac2": "support-information-repair-kb40125",
    "prac3": "support-information-repair-kb50198",
    "prac4": "support-information-repair-kb60231",
    "prac5": "support-information-repair-kb70142",
    "prac6": "support-information-repair-kb80319",
    "prac7": "support-information-repair-kb90214",
    "prac8": "support-information-repair-kb99482"
}

for p in practicals:
    pid = p['id']
    badge = p['badge']
    title = p['title'].split(':')[1].strip() if ':' in p['title'] else p['title']
    disguise_link = disguise_kb_map.get(pid, "support-information-repair")
    
    nav_item = f"""
      <a href="#{disguise_link}" class="nav-item" data-target="{pid}" data-disguise="{disguise_link}">
        <div class="nav-item-content">
          <div class="nav-badge-prefix">{badge}</div>
          <div class="nav-item-title">{html.escape(title)}</div>
        </div>
        <span class="tag">{len(p['questions'])} Qs</span>
      </a>"""
    nav_items_list.append(nav_item)

    # Build Questions HTML
    q_html_list = []
    for q in p['questions']:
        qid = q['qid']
        q_badge = html.escape(q['badge'])
        q_title = html.escape(q['title'])
        q_desc = html.escape(q['desc'])
        q_code = html.escape(q['code'])
        q_output = html.escape(q['output'])
        q_viva = html.escape(q['viva'])

        q_card = f"""
        <article class="question-card" id="{qid}">
          <div class="question-header">
            <span class="q-badge">{q_badge}</span>
            <h3 class="q-title">{q_title}</h3>
            <p class="q-desc">{q_desc}</p>
          </div>

          <div class="code-wrapper">
            <div class="code-header">
              <div class="code-lang-label">
                <span class="code-lang-dot"></span>
                python 3
              </div>
              <button class="copy-btn" data-code-target="code_{qid}">
                <span>📋</span> Copy Code
              </button>
            </div>
            <pre><code id="code_{qid}">{q_code}</code></pre>
          </div>

          <div class="output-box">
            <div class="output-header">
              <span class="output-label">▶ Expected Terminal Output</span>
            </div>
            <div class="output-content">{q_output}</div>
          </div>

          <div class="viva-box">
            <span class="viva-icon">💡</span>
            <div class="viva-text">
              <strong>Viva / Concept Insight:</strong> {q_viva}
            </div>
          </div>
        </article>
        """
        q_html_list.append(q_card)

    questions_html = "\n".join(q_html_list)

    section = f"""
      <section class="practical-section" id="{pid}">
        <div class="section-header">
          <div>
            <div class="section-meta">
              <span class="section-badge">{badge}</span>
              <span class="section-filename">Source: {html.escape(p['filename'])}</span>
            </div>
            <h2 class="section-title">{html.escape(p['title'])}</h2>
          </div>
          <div class="section-actions">
            <button class="btn-primary copy-all-btn">
              <span>📋</span> Copy Entire Practical
            </button>
          </div>
        </div>

        <div class="theory-card">
          <h4>📌 {html.escape(p['theory_title'])}</h4>
          <p>{html.escape(p['theory_desc'])}</p>
        </div>

        {questions_html}
      </section>
    """
    sections_list.append(section)

final_nav = "\n".join(nav_items_list)
final_sections = "\n".join(sections_list)

output_html = html_template.replace('{nav_items}', final_nav).replace('{sections_html}', final_sections)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

print("index.html generated successfully with all 8 Practicals!")
