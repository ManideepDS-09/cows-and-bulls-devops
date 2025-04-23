"""
game_logic.py

This module contains the core game logic for the "Cows and Bulls" game.
It includes:
- Feedback calculation (cows and bulls logic)
- AI guessing strategy (Knuth-style algorithm)
- Main game loop
- Learning evaluation with confidence intervals and visual plot

This module is meant to be imported and run from main.py or integrated into a web/API service later.
"""

import random
from itertools import permutations

def get_feedback(guess, secret):
    cows = sum(1 for g, s in zip(guess, secret) if g == s)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def ai_guess(possibilities, previous_guesses, num_digits):
    if not previous_guesses:
        return random.sample(range(0, 10), num_digits)  # Initial guess
    elif possibilities:
        guess = possibilities[0]  # Simplified Knuth-like selection
        return guess
    else:
        print("No possible numbers left that match the given feedback.")
        return []

def game(num_digits):
    sample_list = list(range(0, 10))
    secret = random.sample(sample_list, num_digits)
    all_possible_numbers = list(permutations(sample_list, num_digits))
    possibilities = all_possible_numbers.copy()
    previous_guesses = []

    count = 0
    guess_counts = []

    while True:
        count += 1
        guess = ai_guess(possibilities, previous_guesses, num_digits)
        previous_guesses.append(guess)
        print(f"AI guesses: {''.join(map(str, guess))}")

        try:
            cows = int(input("Enter number of cows: "))
            bulls = int(input("Enter number of bulls: "))
        except ValueError:
            print("Invalid input. Please enter integer values for cows and bulls.")
            continue

        if cows == num_digits:
            print(f"AI guessed the correct number {''.join(map(str, guess))} in {count} tries!")
            guess_counts.append(count)
            break

        print(f"cows:-> {cows} Bulls:-> {bulls}")
        possibilities = [num for num in possibilities if get_feedback(num, guess) == (cows, bulls)]

    return guess_counts

def evaluate_learning_rate(num_digits, num_sessions):
    import matplotlib.pyplot as plt
    import numpy as np

    all_guess_counts = []
    for session in range(num_sessions):
        print(f"\n--- Session {session + 1} ---")
        guess_counts = game(num_digits)
        all_guess_counts.extend(guess_counts)
        print(f"Session {session + 1}: AI guessed the number in {guess_counts} tries.")

    # Learning Curve
    session_numbers = range(1, num_sessions + 1)
    plt.plot(session_numbers, [np.mean(all_guess_counts[:i]) for i in range(1, num_sessions + 1)], marker='o')
    plt.xlabel('Session Number')
    plt.ylabel('Average Number of Guesses')
    plt.title('AI Learning Curve')
    plt.show()

    # Confidence Intervals
    bootstrap_means = []
    num_bootstraps = 1000
    for _ in range(num_bootstraps):
        bootstrap_sample = np.random.choice(all_guess_counts, size=len(all_guess_counts), replace=True)
        bootstrap_mean = np.mean(bootstrap_sample)
        bootstrap_means.append(bootstrap_mean)

    lower_ci = np.percentile(bootstrap_means, 2.5)
    upper_ci = np.percentile(bootstrap_means, 97.5)
    mean_guesses = np.mean(all_guess_counts)

    print(f"\nAverage number of guesses over {num_sessions} sessions: {mean_guesses}")
    print(f"95% Confidence Interval: [{lower_ci}, {upper_ci}]")

    return mean_guesses, (lower_ci, upper_ci)
