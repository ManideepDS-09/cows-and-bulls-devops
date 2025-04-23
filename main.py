"""
main.py

This is the entry point for running the Cows and Bulls game in standalone mode.
It takes user input for number of digits and sessions, and evaluates the AI's performance.

This file imports logic from the cows_and_bulls.game_logic module.
"""

from cows_and_bulls.game_logic import evaluate_learning_rate

if __name__ == "__main__":
    num_digits = int(input("No. of Digits: "))
    num_sessions = int(input("No. of Sessions: "))
    evaluate_learning_rate(num_digits, num_sessions)