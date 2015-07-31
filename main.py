__author__ = 'grahamearley'
import random

from CharacterFrequencyCalibrator import CharacterFrequencyCalibrator
c = CharacterFrequencyCalibrator("PrideAndPrejudice.txt")


def calculate_score(swap_dictionary, text):
    text = swap_text(swap_dictionary, text)
    score = 1
    i = 0
    while i < len(text)-2:
        code_char_pair = text[i] + text[i+1]

        if code_char_pair in c.frequencies_dict:
            score *= c.frequencies_dict[code_char_pair]

        i += 1

    return score


def swap_text(swap_dictionary, text):
    for char in text:
        if char in swap_dictionary:
            text = str.replace(text, char, swap_dictionary[char].capitalize())

    # Bring it back to lowercase now
    return text.lower()


def accept_proposal(current_swap_dictionary, proposed_swap_dictionary, text):
    proposed_score = calculate_score(proposed_swap_dictionary, text)
    current_score = calculate_score(current_swap_dictionary, text)

    ratio = proposed_score/current_score

    unif_rand = random.uniform(0, 1)

    return unif_rand <= ratio

encrypted_text = "Svool, gsrh rh zm zgyzhs xrksvi uli gvhgrmt lfg nb NXNX wvxibkgrlm zkkorxzgrlm dirggvm rm Kbgslm. Vmqlb!"

swap_dictionary = {}
for character in "qwertyuiopasdfghjklzxcvbnm":
    # Initialize the swap dictionary as the identity function
    swap_dictionary[character] = character

runtimes = 10000
for i in range(runtimes):
    swap_char1 = random.choice(list(swap_dictionary.keys()))
    swap_char2 = random.choice(list(swap_dictionary.keys()))

    proposal_dictionary = swap_dictionary.copy()

    proposal_dictionary[swap_char1], proposal_dictionary[swap_char2] = proposal_dictionary[swap_char2], proposal_dictionary[swap_char1]

    if accept_proposal(swap_dictionary, proposal_dictionary, encrypted_text):
        swap_dictionary = proposal_dictionary
        encrypted_text = swap_text(swap_dictionary, encrypted_text)
    i += 1

print(encrypted_text)
