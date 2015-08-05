class SwapEncryptor:
    """
    A SwapEncryptor will encrypt text based on a
    given alphabet map.
    """

    def __init__(self, encrypted_alphabet):
        # encrypted_alphabet should be a string whose
        # characters correspond to an alphabet character.
        #       e.g. "abcd" -> "wdsy" would map 'a' to 'w', 'b'
        #             to 'd', etc.
        self.encrypted_alphabet = self.verify_encrypted_alphabet(encrypted_alphabet)

    def encrypt(self, text):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted_text = text.lower()
        for char in alphabet:
            char_index = alphabet.index(char)
            encrypted_char = self.encrypted_alphabet[char_index]

            encrypted_text = encrypted_text.replace(char, encrypted_char)

        return encrypted_text

    @staticmethod
    def verify_encrypted_alphabet(encrypted_alphabet):
        """
        Checks if the given encrypted_alphabet is valid by making sure
            * it has 26 characters
            * it only has alphabet letters
            * no letters are repeated

        If valid, return the encrypted_alphabet.
        """
        if len(encrypted_alphabet) != 26:
            raise "The encrypted alphabet you provided doesn't have exactly 26 characters."

        for char in encrypted_alphabet:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                raise "Your encrypted alphabet contained an illegal character: " + char
            if encrypted_alphabet.count(char) > 1:
                raise "Your encrypted alphabet contained more than one of the following character: " + char

        return encrypted_alphabet
