
Steps: -
1. Create a file name prac6.py and write the code given below.
2. Save the file.
3. Open Command Prompt (Terminal) and change the directory to the python file.
4. In CMD type – python prac6.py
5. Now open the Link given below –
http://127.0.0.1:5000
http://127.0.0.1:5000/hello
6. To run add method:
http://127.0.0.1:5000/add?a=5&amp;b=3
------------------------------------------------------------------------------

#1. Fibonacci Series
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/fibonacci", methods=["GET"])
def fibonacci():
    n = int(request.args.get("n"))
    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return jsonify({"fibonacci": series})

if __name__ == "__main__":
    app.run(debug=True)

👉 Test:
http://127.0.0.1:5000/fibonacci?n=5
--------------------------------------------------------------------
#2. Odd / Even Check
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/oddeven", methods=["GET"])
def odd_even():
    num = int(request.args.get("num"))

    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    return jsonify({"number": num, "result": result})

if __name__ == "__main__":
    app.run(debug=True)

👉 Test:
http://127.0.0.1:5000/oddeven?num=7
--------------------------------------------------------------------

#3. Prime Number Check
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/prime", methods=["GET"])
def prime():
    num = int(request.args.get("num"))

    if num <= 1:
        return jsonify({"number": num, "result": "Not Prime"})

    for i in range(2, num):
        if num % i == 0:
            return jsonify({"number": num, "result": "Not Prime"})

    return jsonify({"number": num, "result": "Prime"})

if __name__ == "__main__":
    app.run(debug=True)

👉 Test:
http://127.0.0.1:5000/prime?num=7
--------------------------------------------------------------------

#4. Largest of 3 Numbers
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/largest", methods=["GET"])
def largest():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    c = int(request.args.get("c"))

    largest_num = max(a, b, c)

    return jsonify({"largest": largest_num})

if __name__ == "__main__":
    app.run(debug=True)

👉 Test:
http://127.0.0.1:5000/largest?a=5&b=10&c=7
--------------------------------------------------------------------
#5. addition

from flask import Flask, jsonify, request

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "Python Web Service is running!"

# Simple GET WEB Service
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python Web Service"})

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")
    else:  # GET request from browser
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))

    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True)




