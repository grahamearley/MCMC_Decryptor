__author__ = 'grahamearley'


class CharacterFrequencyCalibrator:
    """
    A class for storing the frequencies of character pairings,
    calibrated to a specific text file (like a text from
    Project Gutenberg).
    """

    def __init__(self, input_file_location):
        self.input_text_file = open(input_file_location, 'r')
        self.frequencies_dict = self.count_character_appearances()

    def calibrate_characters(self):
        non_punctuation_chars = []
        text = self.input_text_file.read().lower()  # (Make all text lower case)

        for char in text:
            if char == "\n":
                # Set line breaks as spaces.
                non_punctuation_chars.append(" ")
            elif char not in "`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/?1234567890":
                # Store it if it's not punctuation, etc.
                non_punctuation_chars.append(char)

        self.input_text_file.close()
        non_punctuation_text = "".join(non_punctuation_chars)

        return non_punctuation_text

    def count_character_appearances(self):
        clean_text = self.calibrate_characters()

        frequencies_dict = {}
        text_length = len(clean_text)-1

        i = 0
        while i < text_length:
            char_pair = clean_text[i] + clean_text[i+1]

            if char_pair in frequencies_dict:
                frequencies_dict[char_pair] += 1
            else:
                frequencies_dict[char_pair] = 1

            i += 1

        return frequencies_dict


