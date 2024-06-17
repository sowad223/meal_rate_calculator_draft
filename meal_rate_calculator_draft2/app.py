from flask import Flask, render_template, request, jsonify
from meal_rate_calculator import MealRateCalculator


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input_persons', methods=['POST'])
def input_persons():
    num_persons = int(request.form.get('num_persons'))
    return render_template('input_persons.html', num_persons=num_persons)


@app.route('/calculate', methods=['POST'])
def calculate():
    num_persons = len([key for key in request.form.keys() if key.startswith('name_')])
    calculator = MealRateCalculator()

    try:
        for i in range(num_persons):
            name = request.form.get(f'name_{i}')
            meal_count = request.form.get(f'meal_count_{i}')
            given_money = request.form.get(f'given_money_{i}')

            if not meal_count or not given_money or not name:
                return f"Missing input for person {i + 1}", 400

            meal_count = float(meal_count)
            given_money = float(given_money)

            calculator.add_person(name, meal_count, given_money)

        left_amount = request.form.get('left_money')
        if not left_amount:
            return "Missing input for left money", 400

        left_amount = float(left_amount)
        meal_rate, results = calculator.calculate(left_amount)

        return render_template('results.html', meal_rate=meal_rate, results=results)
    except ValueError as e:
        return str(e), 400


@app.route('/chat')
def chat():
    return render_template('chatbot.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("user_input")
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
