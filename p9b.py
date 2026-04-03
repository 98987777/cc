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



