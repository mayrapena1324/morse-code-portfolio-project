import requests


class Morse:
    def create_morse(self, message):
        parameters = {
            "text": message,
        }

        response = requests.get("https://api.funtranslations.com/translate/morse/", params=parameters).json()
        ciphered_text = response["contents"]["translated"]
    #     ciphered_text = ""
    #     for letter in message:
    #         if letter == " ":
    #             ciphered_letter = " / "
    #         else:
    #             ciphered_letter = MORSE_CODE_DICT[letter]
    #         ciphered_text += ciphered_letter + " "
        return ciphered_text
