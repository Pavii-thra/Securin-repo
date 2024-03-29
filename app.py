from flask import Flask, render_template, redirect, url_for
from question2 import display_combinations
from question3 import calculate_probabilities
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Page 1
@app.route('/total_combinations')
def page1():
    return render_template('total_combinations.html')

# Page 2
@app.route('/possible_combinations')
def page2():
    combinations = display_combinations()
    return render_template('possible_combinations.html', combinations=combinations)

# Page 3
@app.route('/probability')
def page3():
    output = calculate_probabilities()
    return render_template('probability.html', output=output)
# Page 4
@app.route('/loki_challenge')
def page4():
    return render_template('loki_challenge.html')

if __name__ == '__main__':
    app.run(debug=True)
