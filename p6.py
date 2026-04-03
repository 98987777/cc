
Creating and Running a Python Web Service using Flask
Steps: -
1. Create a file name prac6.py and write the code given below.
2. Save the file.
3. Open Command Prompt (Terminal) and change the directory to the python file.
4. In CMD type – python prac6.py
5. Now open the Link given below –
http://127.0.0.1:5000
http://127.0.0.1:5000/hello
6. To run add method:
http://127.0.0.1:5000/add?a=5&b=3
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





For Viva- 
# Practical Viva Questions  
## Python Web Service using Flask  

---

## 1. Web Service Concepts  

**Q1. What is a Web Service?**  
A web service is a software system that allows communication between applications over a network using standard protocols like HTTP.  

**Q2. What type of web service is Flask used for?**  
Flask is commonly used to create RESTful web services.  

**Q3. What is REST API?**  
REST (Representational State Transfer) is an architectural style used to build lightweight and scalable web services.  

---

## 2. Flask Framework  

**Q1. What is Flask?**  
Flask is a lightweight web framework in Python used to build web applications and APIs.  

**Q2. Why is Flask called a micro-framework?**  
Because it provides only essential features and does not include heavy built-in components.  

**Q3. What are the advantages of Flask?**  
Lightweight, easy to learn, flexible, and suitable for small to medium applications.  

---

## 3. Routing and Endpoints  

**Q1. What is routing in Flask?**  
Routing maps a URL to a specific function in the application.  

**Q2. What is an endpoint?**  
An endpoint is a URL where a web service can be accessed.  

**Q3. What does @app.route() do?**  
It defines the URL path and connects it to a function.  

---

## 4. HTTP Methods  

**Q1. What are HTTP methods?**  
They define the type of request sent to the server (GET, POST, etc.).  

**Q2. Difference between GET and POST**  
GET → Used to retrieve data  
POST → Used to send data to the server  

**Q3. Which method is used in browser URL testing?**  
GET method  

---

## 5. Request and Response Handling  

**Q1. What is request.args?**  
It is used to get query parameters from the URL in GET requests.  

**Q2. What is request.get_json()?**  
It is used to read JSON data sent in a POST request.  

**Q3. What is jsonify()?**  
It converts Python data into JSON format for response.  

---

## 6. JSON Concepts  

**Q1. What is JSON?**  
JSON (JavaScript Object Notation) is a lightweight data format used for data exchange.  

**Q2. Why is JSON used in web services?**  
Because it is easy to read, lightweight, and widely supported.  

---

## 7. Programming Logic Concepts  

**Q1. What is the logic behind Fibonacci series?**  
Each number is the sum of the previous two numbers.  

**Q2. How is odd/even determined?**  
Using modulus operator (num % 2).  

**Q3. How do you check prime number?**  
By checking divisibility from 2 to n-1.  

**Q4. How is the largest of three numbers found?**  
Using comparison or built-in max() function.  

---

## 8. Client-Server Interaction  

**Q1. What is client-server architecture?**  
The client sends requests and the server processes and responds.  

**Q2. What acts as client and server in this practical?**  
Browser/Postman → Client  
Flask application → Server  

**Q3. How does the browser communicate with Flask?**  
Through HTTP requests using URLs.  

---

## 9. Debugging and Execution  

**Q1. What does debug=True do?**  
It enables automatic reload and shows error messages for debugging.  

**Q2. What is localhost (127.0.0.1)?**  
It refers to the local machine where the server is running.  

---

## 10. Advantages and Limitations  

**Q1. Advantages of Flask Web Services**  
Simple, lightweight, flexible, fast development  

**Q2. Limitations of Flask**  
Not suitable for very large applications without extensions  

---

## 11. Comparison-Based Questions  

**Q1. Difference between Flask and ASP.NET Web Service**  
Flask → Python-based, REST  
ASP.NET → .NET-based, supports SOAP and Web API  

**Q2. Difference between REST and SOAP**  
REST → Lightweight, uses JSON  
SOAP → Heavy, uses XML  

---

## 12. Final Conceptual Question  

**Q. Explain how this practical demonstrates a web service.**  
In this practical, Flask is used to create REST APIs that perform operations like Fibonacci, prime check, and addition. The client sends requests through URLs, and the server processes them and returns JSON responses, demonstrating web service communication.  

---
