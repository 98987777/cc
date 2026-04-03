
Steps: -
#In Command Prompt:
    pip install fastapi uvicorn
    Open Microsoft Visual Studio 2019.
    Create a new project – Console App (.NET Core) / Console App
    Now open Python IDE and create a file (e.g., practical9.py)
    #write the below code:
        
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello {name} from Python API!"}

#To run the file, go to CMD and navigate to the Python file location and run:
python -m uvicorn practical9:app --reload --port 8000

#In Microsoft Visual Studio – open Program.cs and write the below code and run (keep Python server running):
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();

        var response = await client.GetAsync("http://localhost:8000/hello?name=ASH");
        var content = await response.Content.ReadAsStringAsync();

        Console.WriteLine("Response from Python API:");
        Console.WriteLine(content);
    }
}
Output: -

Open:

http://localhost:8000/hello?name=ASH



👉 Output:

{"message":"Hello ASH from Python API!"}






for viva -
# Practical Viva Questions  
## Python FastAPI Web Service with .NET Client  

---

## 1. Web Service and API Concepts  

**Q1. What is a Web API?**  
A Web API is a service that allows communication between applications using HTTP requests and responses.  

**Q2. What is REST API?**  
REST API is an architectural style that uses HTTP methods to perform operations on resources.  

**Q3. What is an endpoint?**  
An endpoint is a URL where a specific API service is accessed.  

---

## 2. FastAPI Framework  

**Q1. What is FastAPI?**  
FastAPI is a modern, high-performance Python framework used to build APIs quickly and efficiently.  

**Q2. Why is FastAPI popular?**  
Because it is fast, easy to use, and supports automatic documentation.  

**Q3. What type of API does FastAPI create?**  
RESTful APIs.  

---

## 3. Routing and Parameters  

**Q1. What is routing in FastAPI?**  
Mapping URLs to specific Python functions.  

**Q2. What is query parameter?**  
A value passed in the URL (e.g., ?name=ASH).  

**Q3. How are parameters handled in FastAPI?**  
Using function arguments with type annotations.  

---

## 4. HTTP Methods  

**Q1. What is GET method?**  
Used to retrieve data from the server.  

**Q2. Which HTTP method is used in this practical?**  
GET method.  

**Q3. Can FastAPI support other methods?**  
Yes, POST, PUT, DELETE, etc.  

---

## 5. JSON and Response  

**Q1. What format does FastAPI return data in?**  
JSON format.  

**Q2. What is JSON?**  
A lightweight data format used for communication between client and server.  

---

## 6. Client-Server Communication  

**Q1. What is client-server architecture?**  
Client sends request → Server processes → Server sends response.  

**Q2. What acts as client and server here?**  
.NET Console App → Client  
FastAPI application → Server  

**Q3. How does the client communicate with FastAPI?**  
Using HTTP requests via URL.  

---

## 7. .NET HttpClient  

**Q1. What is HttpClient?**  
A class in .NET used to send HTTP requests and receive responses.  

**Q2. What does GetAsync() do?**  
It sends a GET request to a specified URL.  

**Q3. What is ReadAsStringAsync()?**  
It reads the response content as a string.  

---

## 8. Asynchronous Programming  

**Q1. What is async/await?**  
It allows non-blocking execution of tasks.  

**Q2. Why use async in HTTP requests?**  
To improve performance and avoid blocking the application.  

---

## 9. Server Execution Concepts  

**Q1. What is Uvicorn?**  
A server used to run FastAPI applications.  

**Q2. What does --reload do?**  
Automatically reloads the server when code changes.  

**Q3. What is localhost?**  
Refers to the local machine where the server runs.  

---

## 10. Advantages and Applications  

**Q1. Advantages of FastAPI**  
High performance, automatic documentation, easy to develop  

**Q2. Advantages of cross-language communication**  
Different technologies can interact easily (Python ↔ .NET)  

**Q3. Where is this used?**  
Microservices, backend APIs, system integration  

---

## 11. Comparison-Based Questions  

**Q1. Difference between FastAPI and Flask**  
FastAPI → Faster, built-in validation, async support  
Flask → Lightweight, simpler, fewer built-in features  

**Q2. Difference between REST API and Web Application**  
REST API → Returns data (JSON)  
Web App → Returns UI (HTML)  

---

## 12. Final Conceptual Question  

**Q. Explain how this practical demonstrates web services.**  
In this practical, a FastAPI application provides an API endpoint that returns a greeting message. A .NET client sends an HTTP request to this API and receives a JSON response, demonstrating communication between different technologies using web services.  

---
