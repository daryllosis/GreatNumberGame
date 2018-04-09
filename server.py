from flask import Flask, render_template, session, redirect, request

import random

app = Flask(__name__)
app.secret_key = 'denvernuggets'

@app.route('/')
def index():
    session['randomnumber'] = random.randrange(0, 101)
    print(session['randomnumber'])
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guessNumber():
    display = "block"
    resetbutton = "none"
    guess = int(request.form['number'])
    if guess > session['randomnumber']:
        color = "red"
        message = "Too High!"
    elif guess < session['randomnumber']:
        message = "Too Low"
        color = "red"
    elif guess == session['randomnumber']:
        resetbutton = "block"
        message = str(session['randomnumber']) + " was the number!"
        color = "green"

    return render_template('index.html', message = message, color = color, display = display, resetbutton = resetbutton)

if __name__ == "__main__":
    app.run(debug=True)