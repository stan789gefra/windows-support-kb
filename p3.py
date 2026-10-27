#====================================================================
# Practical 3: Practical 3: Joint, Marginal & Conditional Probability on Real Datasets
#====================================================================

# --- [Titanic Part A] Titanic: Contingency Table & Survival by Gender ---
import pandas as pd
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

print(f"\nJoint Probability P(Female ∩ Survived)     : {p_female_and_survived:.4f}")
print(f"Conditional Probability P(Survived | Female) : {p_survived_given_female:.4f}")
print(f"Conditional Probability P(Survived | Male)   : {p_survived_given_male:.4f}")


# --- [Titanic Part B] Titanic: Probability of Survival Conditional on Passenger Class ---
import seaborn as sns

df = sns.load_dataset('titanic')

# Survival rate grouped by Passenger Class
survival_by_class = df.groupby('class', observed=False)['survived'].mean()

print("--- Conditional Probability: P(Survived | Pclass) ---")
for pclass, rate in survival_by_class.items():
    print(f"P(Survived | {pclass:<6} Class) : {rate:.4f} ({rate*100:.1f}%)")


# --- [Penguins Part A] Palmer Penguins: Contingency Table & Joint Probabilities ---
import pandas as pd
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

print(f"\nP(Adelie ∩ Dream Island) : {p_adelie_dream:.4f}")
print(f"P(Gentoo ∩ Biscoe Island): {p_gentoo_biscoe:.4f}")


# --- [Penguins Part B] Palmer Penguins: Conditional Probabilities ---
import seaborn as sns

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
print(f"P(Male | Gentoo Species) : {p_male_given_gentoo:.4f} (61 / 124)")


# --- [Penguins Part C] Statistical Independence Test: P(A ∩ B) vs P(A) · P(B) ---
import seaborn as sns

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
print(f"Are Species and Island independent? {abs(p_A_and_B - product) < 1e-5}")

