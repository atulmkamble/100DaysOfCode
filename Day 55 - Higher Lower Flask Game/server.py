from flask import Flask
from random import randint

app = Flask(__name__)

guess = randint(0, 9)


@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/guess/<int:number>')
def user_guess(number):
    print(f'<h1>The guess is: {guess}</h1>')
    if number < guess:
        return '<h1 style="color: purple">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > guess:
        return '<h1 style="color: red">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
