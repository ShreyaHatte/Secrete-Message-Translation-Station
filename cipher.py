class Cipher:

    def __init__(self, key):
        self.key = key

    def encode_message(self, message):

        encoded = ""

        for char in message:

            if char.isalpha():

                shift = ord(char) + self.key

                if char.islower() and shift > ord('z'):
                    shift -= 26

                elif char.isupper() and shift > ord('Z'):
                    shift -= 26

                encoded += chr(shift)

            else:
                encoded += char

        return encoded

    def decode_message(self, message):

        decoded = ""

        for char in message:

            if char.isalpha():

                shift = ord(char) - self.key

                if char.islower() and shift < ord('a'):
                    shift += 26

                elif char.isupper() and shift < ord('A'):
                    shift += 26

                decoded += chr(shift)

            else:
                decoded += char

        return decoded