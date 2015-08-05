"""
Graham Earley, 2015.

Read more about the algorithm here:
https://en.wikipedia.org/wiki/Metropolis–Hastings_algorithm
"""
import random

from CharacterFrequencyCalibrator import CharacterFrequencyCalibrator


def calculate_score(text, calibrator):
    score = 1
    i = 0
    while i < len(text) - 2:
        code_char_pair = text[i] + text[i + 1]

        if code_char_pair in calibrator.frequencies_dict:
            score *= calibrator.frequencies_dict[code_char_pair]

        i += 1

    return score


def swap_chars_in_text(text, swap_char1, swap_char2):
    # Build up the swapped text:
    swapped_text = ""

    for char in text:
        if char == swap_char1:
            swapped_text += swap_char2
        elif char == swap_char2:
            swapped_text += swap_char1
        else:
            swapped_text += char

    return swapped_text


calibrator = CharacterFrequencyCalibrator("PrideAndPrejudice.txt")
encrypted_text = open('encrypted.txt', 'r').read().lower()

letters = "qwertyuiopasdfghjklzxcvbnm"
runtimes = 10000
for run in range(runtimes):
    # Pick two characters to swap (uniformly, at random)
    swap_char1 = random.choice(letters)
    swap_char2 = random.choice(letters)

    # Determine whether to accept the proposal by comparing scores:
    swapped_text = swap_chars_in_text(encrypted_text, swap_char1, swap_char2)
    proposed_score = calculate_score(swapped_text, calibrator)
    current_score = calculate_score(encrypted_text, calibrator)
    acceptance_ratio = proposed_score / current_score

    unif_rand = random.uniform(0, 1)

    # If
    if unif_rand <= acceptance_ratio:
        encrypted_text = swapped_text

print(encrypted_text)
