from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#
#  a) Get /morse route to work
#  b) create morse code class
#  c) template inheritance?

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'  #


# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


class TextToEncrypt(FlaskForm):
    text = StringField("Text", validators=[DataRequired()])
    submit = SubmitField("Encrypt")


def create_morse(message):
    ciphered_text = ""
    for letter in message:
        if letter == " ":
            ciphered_letter = " / "
        else:
            ciphered_letter = MORSE_CODE_DICT[letter]
        ciphered_text += ciphered_letter + " "
    return ciphered_text


@app.route("/", methods=["GET", "POST"])
def home():
    form = TextToEncrypt()
    return render_template("index.html", form=form)


@app.route("/morse", methods=["GET", "POST"])
def morse_text():
    text = input("What would you like to translate to morse code? Type your text here: ").upper()
    encrypted_text = create_morse(text)
    return render_template("morse_text.html", message=encrypted_text)


if __name__ == '__main__':
    app.run(debug=True)
