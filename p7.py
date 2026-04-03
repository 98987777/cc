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








For Viva -
# Practical Viva Questions  
## Python Flask Web Service (Student API + GET/POST Operations)  

---

## 1. Web Service and API Concepts  

**Q1. What is a Web Service?**  
A web service is a system that enables communication between applications over a network using HTTP.  

**Q2. What is an API?**  
API (Application Programming Interface) allows different software systems to communicate and exchange data.  

**Q3. What is a REST API?**  
A REST API is a web service that follows REST principles and uses HTTP methods for communication.  

---

## 2. Flask Framework  

**Q1. What is Flask?**  
Flask is a lightweight Python web framework used to build web applications and REST APIs.  

**Q2. Why is Flask suitable for web services?**  
Because it is simple, flexible, and allows quick API development.  

**Q3. What is the role of Flask in this practical?**  
It acts as the server that handles requests and sends responses.  

---

## 3. HTTP Methods (Very Important)  

**Q1. What are HTTP methods?**  
They define actions performed on resources (GET, POST, etc.).  

**Q2. Difference between GET and POST**  
GET → Used to retrieve data  
POST → Used to send and add data  

**Q3. Which method is more secure?**  
POST is more secure than GET as data is not visible in the URL.  

---

## 4. Routing and Endpoints  

**Q1. What is routing?**  
Mapping URLs to functions in Flask.  

**Q2. What is an endpoint?**  
A URL where a specific service can be accessed.  

**Q3. What is dynamic routing?**  
Using variables in URL (e.g., /students/<id>) to access specific data.  

---

## 5. Data Handling  

**Q1. What is request.args?**  
Used to get data from URL parameters (GET request).  

**Q2. What is request.get_json()?**  
Used to get data from request body (POST request).  

**Q3. What is jsonify()?**  
Converts Python data into JSON format for response.  

---

## 6. JSON and Data Storage  

**Q1. What is JSON?**  
A lightweight format for data exchange between client and server.  

**Q2. Why is JSON used in APIs?**  
It is easy to read, lightweight, and language-independent.  

**Q3. What data structure is used in this practical?**  
Dictionary is used to store student data.  

---

## 7. CRUD Operations  

**Q1. What is CRUD?**  
Create, Read, Update, Delete operations on data.  

**Q2. Which operations are implemented here?**  
Create (add student), Read (get students).  

**Q3. Which HTTP methods correspond to CRUD?**  
Create → POST  
Read → GET  
Update → PUT  
Delete → DELETE  

---

## 8. Error Handling  

**Q1. What is HTTP status code 404?**  
Resource not found.  

**Q2. What is HTTP status code 201?**  
Resource created successfully.  

**Q3. Why is error handling important?**  
To provide proper responses when something goes wrong.  

---

## 9. Programming Logic Concepts  

**Q1. How is multiplication table generated?**  
Using a loop from 1 to 10.  

**Q2. How is Fibonacci series generated?**  
By adding previous two numbers repeatedly.  

**Q3. How is prime number checked?**  
By checking divisibility from 2 to n-1.  

**Q4. How is largest number found?**  
Using comparison or max() function.  

---

## 10. Client-Server Interaction  

**Q1. What acts as client and server here?**  
Browser/Postman → Client  
Flask app → Server  

**Q2. How does client communicate with server?**  
Through HTTP requests using URLs.  

**Q3. What is localhost (127.0.0.1)?**  
It refers to the local machine where the server runs.  

---

## 11. Debugging and Execution  

**Q1. What does debug=True do?**  
Enables debugging and auto-reload during development.  

**Q2. Why change port number?**  
If default port (5000) is busy or not responding.  

---

## 12. Advantages and Limitations  

**Q1. Advantages of Flask APIs**  
Lightweight, fast, easy to develop, flexible  

**Q2. Limitations**  
Not ideal for very large applications without extensions  

---

## 13. Comparison-Based Questions  

**Q1. Difference between Flask API and ASP.NET Web Service**  
Flask → Python-based, REST  
ASP.NET → .NET-based, supports SOAP and REST  

**Q2. Difference between REST and SOAP**  
REST → Lightweight, uses JSON  
SOAP → Heavy, uses XML  

---

## 14. Final Conceptual Question  

**Q. Explain how this practical demonstrates a web service.**  
In this practical, Flask is used to build REST APIs for managing student data and performing operations like Fibonacci, prime check, and addition. The client sends HTTP requests, and the server processes them and returns JSON responses, demonstrating web service communication and CRUD operations.  

---
