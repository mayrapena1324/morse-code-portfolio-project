from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from morse import Morse
import pyperclip

# have morse copied to clip board
# a nice css animation for a card that says Morse and underneath has two buttons. morsify, demorsify. buttons will route
# to correct html form
#  c) add decrypt capabilities
#  d) bootstrap
#  h) add users and save their morse searches with postgreSQL database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
Bootstrap(app)


class TextToEncrypt(FlaskForm):
    text = StringField("Text", validators=[DataRequired()])
    submit = SubmitField("Translate")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/morse", methods=["GET", "POST"])
def morse_text():
    form = TextToEncrypt()
    return render_template("encrypt.html", form=form)


@app.route("/translate", methods=["GET", "POST"])
def show_results():
    form = TextToEncrypt()
    text = form.text.data
    morse = Morse()
    message = morse.create_morse(text)
    return render_template("morse_text.html", message=message)


@app.route("/english", methods=["GET", "POST"])
def to_english():
    form = TextToEncrypt()
    return render_template("decrypt.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
