from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from morse import Morse

#  c) template inheritance?

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'  #


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
    morse = Morse()
    message = form.text.data.upper()
    morsed_message = morse.create_morse(message)
    return render_template("morse_text.html", message=morsed_message)


if __name__ == '__main__':
    app.run(debug=True)
