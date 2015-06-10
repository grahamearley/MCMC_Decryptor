__author__ = 'grahamearley'

from CharacterFrequencyCalibrator import CharacterFrequencyCalibrator

c = CharacterFrequencyCalibrator("test.txt")
text_for_decoding = c.clean_text

def calculate_score(swap_dictionary):
    text = text_for_decoding

    for char in text:
        if char in swap_dictionary:
            text = str.replace(text, char, swap_dictionary[char].capitalize())

    # Bring it back to lowercase now
    text = text.lower()

    print(text)

    score = 1
    i = 0
    while i < len(text)-1:
        code_char_pair = text[i] + text[i+1]

        if code_char_pair in c.frequencies_dict:
            score *= c.frequencies_dict[code_char_pair]
        else:
            score *= 1
            # Even though this means it has a frequency of zero,
            # we'll just leave it the same.

        i += 1

    return score

# def acceptance_function(from_letter, to_letter):

swap_map = {}

print(calculate_score(swap_map))