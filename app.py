from flask import Flask, request, render_template, redirect, url_for
#Creating Flask instance
app = Flask(__name__)

#Defining a route for our home page ('/')
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

    @app.route('/result/', methods=['POST'])
def result():
    return render_template('index.html')

         Input1 = float(request.form['Input1'])
         Input2 = float(request.form['Input2'])
         result = Input1 + Input2
         operation = request.form['operation']

#Calculating the result based on selected operation
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
        result = "Invalid operation"
        operation = "Invalid operation"

     return render_template(
        'index.html',
        Input1=Input1,
        Input2=Input2,
        operation=operation,
        result=result 
     )
    

#Run the flask application

if __name__ == '__main__':
    app.debug = True
    app.run()
    