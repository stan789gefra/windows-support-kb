#====================================================================
# Practical 5: Practical 5: Hidden Markov Models (HMM) & NLP Inference
#====================================================================

# --- [Question 1] HMM Model Setup & Matrix Probability Verification ---
import numpy as np
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

print("\n--- Transition Probability Matrix (A) ---")
print(pd.DataFrame(transition_prob, index=states, columns=states))

print("\n--- Emission Probability Matrix (B) ---")
print(pd.DataFrame(emission_prob, index=states, columns=observation))

# Sanity Check
print("\nSum of initial probabilities   :", initial_prob.sum())
print("Sum of transition probabilities :", transition_prob.sum(axis=1))
print("Sum of emission probabilities   :", emission_prob.sum(axis=1))


# --- [Question 2] Calculate Marginal Probability of Observation P('dogs') ---
# Index of observation 'dogs'
dogs_idx = observation.index("dogs")

# P(Noun ∩ dogs) = P(Noun) * P(dogs | Noun)
p_noun_dogs = initial_prob[0] * emission_prob[0, dogs_idx]

# P(Verb ∩ dogs) = P(Verb) * P(dogs | Verb)
p_verb_dogs = initial_prob[1] * emission_prob[1, dogs_idx]

# Total Marginal Probability P(dogs)
p_dogs_total = p_noun_dogs + p_verb_dogs

print(f"P(Noun) * P(dogs | Noun) = {initial_prob[0]:.2f} * {emission_prob[0, dogs_idx]:.2f} = {p_noun_dogs:.4f}")
print(f"P(Verb) * P(dogs | Verb) = {initial_prob[1]:.2f} * {emission_prob[1, dogs_idx]:.2f} = {p_verb_dogs:.4f}")
print(f"\nTotal P('dogs') = {p_noun_dogs:.4f} + {p_verb_dogs:.4f} = {p_dogs_total:.4f}")


# --- [Question 3] Calculate Joint Probability of Sequence: 'Noun -> Verb' & 'dogs -> barks' ---
# Sequence definition
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
print(f"Joint Sequence Probability P(S, O) = {joint_seq_prob:.6f} ({joint_seq_prob*100:.2f}%)")

