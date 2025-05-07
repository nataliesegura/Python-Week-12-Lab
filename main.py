import operator

from flask import Flask, render_template, request, url_for

app = Flask(__name__)
print("poo")
@app.route("/", methods=['POST', 'GET'])

def home():
    userInput = ""
    rezult = None

    if request.method == 'POST':
        user_input = request.form.get('expression', '').strip() # Get input, default to empty, strip whitespace
        rezult = rpn(user_input)

    return render_template('index.html', rezult=rezult)

def rpn(userInput):
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '%': operator.mod }

    stack = []
    tokens = userInput.split()

    listy = []
    for token in tokens:
        if token.lstrip('-').replace('.', '', 1).isdigit():
            listy.append(float(token))
        elif token in operators:
            listy.append(token)
        else:
            raise ValueError(f"Invalid token found: {token}")

    for element in listy:
        if isinstance(element, (int, float)):
            stack.append(element)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            op = operators.get(element)
            stack.append((int(operators[element](num1, num2)))) # int just makes it be a whole number instead of a long decimal
            print (operators[element](num1, num2))

    return stack


if __name__ == '__main__':
    app.run(debug=True) # debug=True is helpful for development