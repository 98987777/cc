python -m pip install flask
or
pip intall flask

Steps: -
1. Create a file named prac7.py and write the code given below.
2. Save the file.
3. Open Command Prompt (Terminal) and change the directory to the folder where the
Python file is saved.
Example: cd C:\Users\Admin\Desktop\ASH
4. In CMD type: Python prac7.py
5. Now open the links given below in the browser:
Home Page: http://127.0.0.1:5000/
Get All Students: http://127.0.0.1:5000/students
Get Student by ID: http://127.0.0.1:5000/students/1
Add Student: http://127.0.0.1:5000/addstudents?id=5&name=riddhi&marks=92


from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data (dictionary)
students = {
    1: {"name": "Alice", "marks": 85},
    2: {"name": "Bob", "marks": 90},
    3: {"name": "Charlie", "marks": 78}
}

# Home Route
@app.route("/")
def home():
    return "Student Marks Web Service Running!"

# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# Get a student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    if id in students:
        return jsonify(students[id])
    return jsonify({"error": "Student not found"}), 404

# Add a student (POST)
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    sid = data.get("id")
    name = data.get("name")
    marks = data.get("marks")
    students[sid] = {"name": name, "marks": marks}
    return jsonify({"message": "Student added successfully!"}), 201

# Add student using GET
@app.route("/addstudents", methods=["GET"])
def add_students_get():
    sid = request.args.get("id", type=int)
    name = request.args.get("name")
    marks = request.args.get("marks", type=int)

    if not sid or not name or not marks:
        return jsonify({"error": "Missing required parameters"}), 400

    students[sid] = {"name": name, "marks": marks}
    return jsonify({"message": "Student added successfully!"}), 201

# Run Server
if __name__ == "__main__":
    app.run(debug=True)

agar sirf load ho rha hai pura time then write
app.run(port=5000) any 5000 se kitna bhi
----------------------------------------------------------------------------------------

#1. Multiplication Table (GET + POST)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Multiplication Table Service Running!"

@app.route("/table", methods=["GET", "POST"])
def table():
    if request.method == "POST":
        data = request.get_json()
        num = data.get("num")
    else:
        num = int(request.args.get("num"))

    result = []
    for i in range(1, 11):
        result.append(f"{num} x {i} = {num*i}")

    return jsonify({"table": result})

if __name__ == "__main__":
    app.run(debug=True)

👉 Test:
http://127.0.0.1:5000/table?num=5
--------------------------------------------------------------------

#🔹 2. Fibonacci Series (GET + POST)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/fibonacci", methods=["GET", "POST"])
def fibonacci():
    if request.method == "POST":
        data = request.get_json()
        n = data.get("n")
    else:
        n = int(request.args.get("n"))

    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return jsonify({"fibonacci": series})

if __name__ == "__main__":
    app.run(debug=True)

--------------------------------------------------------------------

#3. Odd / Even (GET + POST)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/oddeven", methods=["GET", "POST"])
def odd_even():
    if request.method == "POST":
        data = request.get_json()
        num = data.get("num")
    else:
        num = int(request.args.get("num"))

    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    return jsonify({"number": num, "result": result})

if __name__ == "__main__":
    app.run(debug=True)

--------------------------------------------------------------------

#4. Prime Number (GET + POST)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/prime", methods=["GET", "POST"])
def prime():
    if request.method == "POST":
        data = request.get_json()
        num = data.get("num")
    else:
        num = int(request.args.get("num"))

    if num <= 1:
        return jsonify({"number": num, "result": "Not Prime"})

    for i in range(2, num):
        if num % i == 0:
            return jsonify({"number": num, "result": "Not Prime"})

    return jsonify({"number": num, "result": "Prime"})

if __name__ == "__main__":
    app.run(debug=True)
🔹 5. Largest of 3 Numbers (GET + POST)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/largest", methods=["GET", "POST"])
def largest():
    if request.method == "POST":
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")
        c = data.get("c")
    else:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        c = int(request.args.get("c"))

    largest_num = max(a, b, c)

    return jsonify({"largest": largest_num})

if __name__ == "__main__":
    app.run(debug=True)
