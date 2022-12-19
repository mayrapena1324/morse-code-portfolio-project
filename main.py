from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from morse import Morse

#  a) Find api that plays morse code text
#  b) create morse code class
#  c) add decrypt capabilities
#  d) bootstrap
#  e) host
#  f) ensure all symbols are included in dict or find api that has letters
#  h) add users and save their morse searches with postgreSQL database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


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


@app.route("/", methods=["GET", "POST"])
def home():
    form = TextToEncrypt()
    return render_template("index.html", form=form)


@app.route("/morse", methods=["GET", "POST"])
def morse_text():
    form = TextToEncrypt()
    text = form.text.data
    morse = Morse()
    message = morse.create_morse(text.upper())
    return render_template("morse_text.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
