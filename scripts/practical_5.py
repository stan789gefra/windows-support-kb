"""
Practical 5: Practical 5
Description: Hidden Markov Models (HMM) - Part-of-Speech Tagging
Original File: Prac5.ipynb
"""

import numpy as np
import pandas as pd

#hidden state
states = ['Noun','Verb']

#observation
observation = ['dogs','barks','loudly']

#initial state probabilities
initial_prob = np.array([0.6,0.4])

# Transition Probabilities Matrix
transition_prob = np.array([[0.3,0.7],[0.6,0.4]])

#Emission Probability Matrix
emission_prob = np.array([[0.7,0.2,0.1],[0.1,0.6,0.3]])

#Display initial probabilities
print("Initial Probabilities")
print(pd.Series(initial_prob,index=states))

# Display transition matrix
print("Transition Probabilities Matrix")
print(pd.DataFrame(transition_prob,index=states,columns=states))

# Display emission matrix
print("Emission Probabilities matrix")
print(pd.DataFrame(emission_prob,columns=observation,index=states))


# check the initial probabilities
print("sum of initial probabilities: ",initial_prob.sum())

# check the transition probabilities
print("sum of transition probabilities: ",transition_prob.sum(axis=1))

# check the emission probabilities
print("sum of emission probabilities: ",emission_prob.sum(axis=1))


#Index of the observation "Dogs"
dogs_index= observation.index("dogs")
#                      P(Noun)          P(dogs | Noun)
p_dogs_given_noun = initial_prob[0] * emission_prob[0,dogs_index]
#                      P(Verb)          P(dogs | Verb)
p_dogs_given_verb = initial_prob[1] * emission_prob[1,dogs_index]

print("P(Noun) x P(dogs | Noun)= ",p_dogs_given_noun)
print("P(Verb) x P(dogs | Verb)= ",p_dogs_given_verb)

#p(dogs) = P(Noun).P(dogs | Noun) +P(Verb) x P(dogs | Verb)
print(("\n P(dogs)= ", p_dogs_given_noun + p_dogs_given_verb))


# same code as above
dogs_index= observation.index("dogs")
#P(Noun, dogs)
p_noun_dogs = initial_prob[0] * emission_prob[0,dogs_index]

#P(Verb, dogs)
p_verb_dogs = initial_prob[1] * emission_prob[1,dogs_index]

print("P(Noun) x P(dogs | Noun)= ",p_noun_dogs)
print("P(Verb) x P(dogs | Verb)= ",p_verb_dogs)


#current state
current_state = "Noun"

#find the row corresponding to Noun
current_index = states.index(current_state)

#get transition probabilities
next_state_probabilities= transition_prob[current_index]
print("Current state: ",current_state)
for state, probability in zip(states, next_state_probabilities):
    print(f"P({current_state}|{state}) = {probability}")

most_likely_index = np.argmax(next_state_probabilities)
most_likely_state = states[most_likely_index]

print("\n Most probable next state: ", most_likely_state)


print("mostly next probable verb is bark")



# ------------------------------------------------------------
# Q7. Calculate the Probability of a Hidden-State and Observation Sequence
# Consider the following hidden-state sequence:
# Noun → Verb
# and the observed sequence:
# dogs → bark
# Calculate the joint probability of this state-observation sequence using:
# 
# P(Noun)×P(dogs|Noun)×P(Verb|Noun)×P(bark|Verb)
# 
# Write Python code to calculate the probability.
# ------------------------------------------------------------

# Hidden-state sequence
state_1 = "Noun"
state_2 = "Verb"

# Observation sequence
observation_1 = "dogs"
observation_2 = "barks"

# Convert names to indices
state_1_index = states.index(state_1)
state_2_index = states.index(state_2)

observation_1_index = observation.index(observation_1)
observation_2_index = observation.index(observation_2)

# Calculate each component
p1 = initial_prob[state_1_index]

p2 = emission_prob[
    state_1_index,
    observation_1_index
]

p3 = transition_prob[
    state_1_index,
    state_2_index
]

p4 = emission_prob[
    state_2_index,
    observation_2_index
]

# Joint probability
sequence_probability = p1 * p2 * p3 * p4

print("P(Noun) =", p1)
print("P(dogs | Noun) =", p2)
print("P(Verb | Noun) =", p3)
print("P(bark | Verb) =", p4)

