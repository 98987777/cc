#Develop a simple Employee Details Web Service in Python and consume it in .NET
#Part A: Create Python FastAPI Web Service
1.Open Command Prompt and install required packages:
pip install fastapi uvicorn

2.Open Python IDE (VS Code / IDLE).
    #Create a file named emp_api.py.
    #Write the following code:
from fastapi import FastAPI
app = FastAPI()

# Sample Employee Data
employees = {
    1: {"name": "Ravi", "department": "HR", "salary": 40000},
    2: {"name": "Priya", "department": "IT", "salary": 55000}
}

# Home Route
@app.get("/")
def home():
    return {"message": "Employee API Running"}

# Get all employees
@app.get("/employees")
def get_employees():
    return employees

# Get employee by ID
@app.get("/employees/{id}")
def get_employee(id: int):
    if id in employees:
        return employees[id]
    return {"error": "Employee not found"}

#Part B: Run Python Server
Open Command Prompt and navigate to file location. (cd...........)
#Run the server:
    python -m uvicorn emp_api:app --reload --port 8000
#Open browser and check:
    http://localhost:8000/employees

#👉 You should see employee data in JSON format.

#Part C: Create .NET Console Application
Open Microsoft Visual Studio 2019.
Create a new project → Console App (.NET Core).
Open Program.cs file.

#Part D: Write .NET Code to Consume API
Replace code with:
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();

        var response = await client.GetAsync("http://localhost:8000/employees");
        var content = await response.Content.ReadAsStringAsync();

        Console.WriteLine("Employee Data from Python API:");
        Console.WriteLine(content);
    }
}
#Part E: Run Application
#Keep Python server running.
#Run the .NET Console Application.
Output: -
Employee Data from Python API:
{"1":{"name":"Ravi","department":"HR","salary":40000},...}

====================================================

OR ELSE

#Develop a simple Employee Details Web Service in Python and consume it in .NET

#Part 1: Python Flask Web Service (Employee API)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Employee Data
employees = {
    1: {"name": "Ravi", "salary": 50000},
    2: {"name": "Priya", "salary": 60000}
}

# Get all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Add employee
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    eid = data.get("id")
    name = data.get("name")
    salary = data.get("salary")

    employees[eid] = {"name": name, "salary": salary}

    return jsonify({"message": "Employee added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)

# => Run this first: URL: http://127.0.0.1:5000/employees

#🔹 Part 2: Consume in .NET (ASP.NET Controller)
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace WebApplication2.Controllers
{
    public class EmployeeController : Controller
    {
        public async Task<string> GetEmployees()
        {
            HttpClient client = new HttpClient();

            var response = await client.GetStringAsync("http://127.0.0.1:5000/employees");

            return response;
        }
    }
}

#Output
When you run:
https://localhost:xxxx/Employee/GetEmployees










For Viva - 
# Practical Viva Questions  
## Employee Details Web Service using Python (FastAPI/Flask) and .NET  

---

## 1. Web Service and API Concepts  

**Q1. What is a Web API?**  
A Web API is a service that allows communication between applications using HTTP requests and responses.  

**Q2. What is REST API?**  
REST API is an architectural style that uses HTTP methods to perform operations on resources.  

**Q3. What is a resource in REST?**  
A resource is an entity such as an employee that can be accessed via a URL.  

---

## 2. Python API Frameworks  

**Q1. What is FastAPI?**  
FastAPI is a high-performance Python framework used to build REST APIs quickly.  

**Q2. What is Flask?**  
Flask is a lightweight Python web framework used to create web applications and APIs.  

**Q3. Difference between FastAPI and Flask**  
FastAPI → Faster, async support, automatic validation  
Flask → Simple, lightweight, more manual configuration  

---

## 3. Routing and Endpoints  

**Q1. What is routing?**  
Mapping URLs to functions that handle requests.  

**Q2. What is dynamic routing?**  
Using variables in URL (e.g., /employees/{id}).  

**Q3. What is an endpoint?**  
A specific URL where the API can be accessed.  

---

## 4. HTTP Methods and CRUD  

**Q1. What are HTTP methods?**  
They define actions performed on resources (GET, POST, etc.).  

**Q2. Which methods are used in this practical?**  
GET → Retrieve employee data  
POST → Add employee data  

**Q3. What is CRUD?**  
Create, Read, Update, Delete operations on data.  

---

## 5. JSON and Data Handling  

**Q1. What is JSON?**  
A lightweight data format used for data exchange between client and server.  

**Q2. Why is JSON used in APIs?**  
It is easy to read, lightweight, and language-independent.  

**Q3. What data structure is used to store employees?**  
Dictionary (key-value pairs).  

---

## 6. Client-Server Communication  

**Q1. What is client-server architecture?**  
Client sends request → Server processes → Server sends response.  

**Q2. What acts as client and server here?**  
.NET application → Client  
Python API → Server  

**Q3. How does .NET communicate with Python API?**  
Using HTTP requests via HttpClient.  

---

## 7. .NET HttpClient  

**Q1. What is HttpClient?**  
A class in .NET used to send HTTP requests and receive responses.  

**Q2. What does GetAsync() or GetStringAsync() do?**  
It sends a request to the API and retrieves response data.  

**Q3. Why is async/await used?**  
To perform non-blocking operations and improve performance.  

---

## 8. Error Handling  

**Q1. What happens if employee ID is not found?**  
API returns an error message.  

**Q2. What is HTTP status code 404?**  
Resource not found.  

**Q3. What is HTTP status code 201?**  
Resource created successfully.  

---

## 9. Advantages and Applications  

**Q1. Advantages of Web APIs**  
Platform independent, reusable, scalable  

**Q2. Why use Python with .NET together?**  
To enable interoperability between different technologies  

**Q3. Where is this used?**  
Microservices, enterprise applications, system integration  

---

## 10. Comparison-Based Questions  

**Q1. Difference between Web API and Web Application**  
Web API → Returns data (JSON)  
Web App → Returns UI (HTML)  

**Q2. Difference between REST and SOAP**  
REST → Lightweight, JSON  
SOAP → Heavy, XML  

---

## 11. Final Conceptual Question  

**Q. Explain how this practical demonstrates web services.**  
In this practical, a Python-based API provides employee data as JSON. A .NET application sends HTTP requests to this API and receives the response, demonstrating client-server communication and integration between different technologies.  

---

