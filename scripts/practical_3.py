"""
Practical 3: Practical 3
Description: Joint & Conditional Probability (Titanic & Palmer Penguins Datasets)
Original File: prac3.ipynb
"""


# ------------------------------------------------------------
# # A. Titanic Dataset
# ------------------------------------------------------------

import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()



# ------------------------------------------------------------
# Q2) Create a contingency table showing the number of passengers according to their sex and survival status
# ------------------------------------------------------------

table=pd.crosstab(df.sex,df.survived)
print(table)



# ------------------------------------------------------------
# Q3) Estimated the joint probability that a randomly selected passenger was female and survived.
# ------------------------------------------------------------

female_and_survived=((df.sex == 'female') & (df.survived == 1)).sum() # total no of female survived

total =len(df) # total no of rows

p_female_and_survived=female_and_survived/total # defination of the probability

print("probaility of female and servived",p_female_and_survived)



# ------------------------------------------------------------
# Q4) Estimated the conditional probility that a passenger survived, given that the passenger was female
# ------------------------------------------------------------

female = (df.sex == 'female').sum()
female_and_survived = ((df.sex == 'female') & (df.survived == 1)).sum()
p_survived_given_female = female_and_survived / female

print("Conditional probability:- P(survived | female)",p_survived_given_female)



# ------------------------------------------------------------
# Q5) Estimate the conditional probability that a passenger survived, given that the passenger was male. Compare i twith the probability obtained in Q4
# ------------------------------------------------------------

male=(df.sex=='male').sum()
male_and_survived=((df.sex=='male') & (df.survived==1)).sum()
p_survived_given_male=male_and_survived/male

print("conditional probablilty:- P(Survived | Male)",p_survived_given_male)
print("Conditional probability:- P(survived | female)",p_survived_given_female)



# ------------------------------------------------------------
# Q6) Estimate the probability of survival conditional on passenger class
# ------------------------------------------------------------

survival_by_class=df.groupby('class')['survived'].mean()
print(survival_by_class)



# ------------------------------------------------------------
# # B. Penguin Dataset
# ------------------------------------------------------------


# ------------------------------------------------------------
# Q1) Load the palmer Penguins dataset and display the first five observatios. Also find the number of observation and variables
# ------------------------------------------------------------

import seaborn as sns
df=sns.load_dataset('penguins')
print(df.head(),"\n")
print("no of obervations",df.shape) # output(obervation, variable)



# ------------------------------------------------------------
# Q2) Find the Frequency Distribution of species, island, and sex
# ------------------------------------------------------------

df[['species','island','sex']].value_counts()



# ------------------------------------------------------------
# Q3) Construct a contingency table showing the number of penguins belonging to each species on each island
# ------------------------------------------------------------

contingency_table = pd.crosstab(df.species, df.island)
print(contingency_table)



# ------------------------------------------------------------
# Q4) Find the joint probability that a randomly selected penguin is an Adelie penguin AND is found on Dream island
# ------------------------------------------------------------

penguin_adelie_and_dream_island = ((df.species == 'Adelie') & (df.island == 'Dream')).sum()
total=len(df)
joint_probability = penguin_adelie_and_dream_island / total
print(joint_probability)



# ------------------------------------------------------------
# Q5) Find the joint probability that a randomly selected penguin is an Gentoo penguin AND is found on Biscoe island
# ------------------------------------------------------------

penguin_gentoo_and_biscoe_island = ((df.species == 'Gentoo') & (df.island == 'Biscoe')).sum()
total=len(df)
joint_probability = penguin_gentoo_and_biscoe_island / total
print(joint_probability)



# ------------------------------------------------------------
# Q6) Calculate the conditional probability that a penguin is an Adelie penguin given that it is found on Dream island
# ------------------------------------------------------------

Dream = (df.island == 'Dream').sum()
Adelie_and_Dream = ((df.species == 'Adelie') & (df.island == 'Dream')).sum()
p_Adelie_given_Dream = Adelie_and_Dream / Dream

print("Conditional probability:- P(Adelie | Dream)",p_Adelie_given_Dream)



# ------------------------------------------------------------
# Q7) Calculate the conditional probability that a penguin is an male given that it belong to the gentoo species
# ------------------------------------------------------------

Gentoo = (df.species == 'Gentoo').sum()
Male_and_Gentoo = ((df.sex == 'Male') & (df.species == 'Gentoo')).sum()
p_Male_given_Gentoo  = Male_and_Gentoo / Gentoo

print("Conditional probability:- P(Male | Gentoo)",p_Male_given_Gentoo)



# ------------------------------------------------------------
# Q8. Construct a contingency table for species and sex. Then calculate the probability that a randomly selected penguin is female and belongs to the Chinstrap species.
# ------------------------------------------------------------

contingency_table = pd.crosstab(df.species, df.sex)
print(contingency_table)

df.sex == 'Female'
df.species == 'Chinstrap'
total=len(df)
probability_sex_species = ((df.sex == 'Female') & (df.species == 'Chinstrap')).sum() / total
print("Probability that a randomly selected penguin is female and belongs to the Chinstrap species:", probability_sex_species)



# ------------------------------------------------------------
# Q9. Calculate the probability of a penguin being male for each species. Use groupby().
# ------------------------------------------------------------

probability_male_by_species = df.groupby('species')['sex'].apply(lambda x: (x == 'Male').mean())
print(probability_male_by_species)



# ------------------------------------------------------------
# Q10. Test whether species and island can be considered independent using :    P(A∩B)=P(A)P(B)Take:
# A : Penguin is Gentoo
# B : Penguin is found on Biscoe Island
# ------------------------------------------------------------

Gentoo_count = (df.species == 'Gentoo').sum()
Biscoe_count = (df.island == 'Biscoe').sum()
Gentoo_and_Biscoe_count = ((df.species == 'Gentoo') & (df.island == 'Biscoe')).sum()
total = len(df)

p_Gentoo_and_Biscoe = Gentoo_and_Biscoe_count / total
p_Gentoo = Gentoo_count / total
p_Biscoe = Biscoe_count / total

P_A_times_P_B = p_Gentoo * p_Biscoe

print("P(Gentoo and Biscoe):", p_Gentoo_and_Biscoe)
print("P(Gentoo) * P(Biscoe):", P_A_times_P_B)
print("Are A and B independent :",p_Gentoo_and_Biscoe == P_A_times_P_B )


p_Gentoo = (df.species == 'Gentoo').mean()
p_Biscoe = (df.island == 'Biscoe').mean()
p_Gentoo_and_Biscoe = ((df.species == 'Gentoo') & (df.island == 'Biscoe')).mean()

P_A_times_P_B = p_Gentoo * p_Biscoe

print("P(Gentoo and Biscoe):", p_Gentoo_and_Biscoe)
print("P(Gentoo) * P(Biscoe):", P_A_times_P_B)
print("Are A and B independent :",p_Gentoo_and_Biscoe == P_A_times_P_B )

