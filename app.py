from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    Input1 = float(request.form['Input1'])
    Input2 = float(request.form['Input2'])
    result = Input1 + Input2
    operation = request.form['operation']
    if operation == 'addition':
        result = Input1 + Input2
    elif operation == 'subtraction':
            result = Input1 - Input2    
    elif operation == 'division':
        if Input2 != 0:
            result = Input1 / Input2
    elif operation == 'multiplication':
            result = Input1 * Input2           
        else:
            result = "Error: Division by zero"

    return render_template('result.html', result=result)






if __name__ == '__main__':
    app.run(debug=True)