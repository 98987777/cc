Steps: -
1. Open Microsoft Visual Studio 2019.
2, Create a new project – ASP .NET Core Web Application / App (MVC)
In Controllers folder create a new Controller Empty named HelloController and add the below code:
----------------------------------------------------------------------------------------

#Code:

helloController.cs

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace WebApplication2.Controllers
{
    public class helloController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet("{name}")]
        public string GetHello(string name)
        {
            return $"Hello, {name} from .NET";
        }
    }
}

#Run Code:
    link mai / dalke add ur name (eg. https://localhost:44380/Ash)


#In Command Prompt:
python -m pip install requests

#Now Open Python IDE and create a file and write the below code:
Code:
import requests

url = "https://localhost:44344/Riddhi"
response = requests.get(url, verify=False)
print(response.text)


==============================================================================================
#Q2. Temperature Conversion Web Service (.NET + Python)** exactly in your format 👇


1. Open Microsoft Visual Studio 2019.
2. Create a new project – **ASP .NET Core Web Application / App (MVC)**
3. In **Controllers folder** create a new Controller → **Empty** → named
   👉 `TempController`

and add the below code:

# Code:

### tempController.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace WebApplication2.Controllers
{
    public class tempController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        // Celsius to Fahrenheit
        [HttpGet("c2f/{c}")]
        public string CelsiusToFahrenheit(double c)
        {
            double f = (c * 9 / 5) + 32;
            return $"Celsius {c} = Fahrenheit {f}";
        }

        // Fahrenheit to Celsius
        [HttpGet("f2c/{f}")]
        public string FahrenheitToCelsius(double f)
        {
            double c = (f - 32) * 5 / 9;
            return $"Fahrenheit {f} = Celsius {c}";
        }
    }
}

# Example:

👉 Celsius to Fahrenheit
https://localhost:44380/c2f/25

👉 Fahrenheit to Celsius
https://localhost:44380/f2c/77

# In Command Prompt:
python -m pip install requests

# Now Open Python IDE and create a file and write the below code:

## Code:
import requests

# Change port if needed
url = "https://localhost:44380/c2f/30"
response = requests.get(url, verify=False)
print(response.text)







For Viva-
# Practical Viva Questions  
## ASP.NET Core MVC Web Service with Python Client  

---

## 1. Web Service and API Concepts  

**Q1. What is a Web Service?**  
A web service is a system that enables communication between different applications over a network using HTTP.  

**Q2. What is a REST API?**  
A REST API is a web service that follows REST principles and uses HTTP methods to perform operations.  

**Q3. What is an endpoint?**  
An endpoint is a specific URL where a web service can be accessed.  

---

## 2. ASP.NET Core MVC Concepts  

**Q1. What is ASP.NET Core?**  
ASP.NET Core is a cross-platform web development framework by :contentReference[oaicite:0]{index=0} used to build modern web applications and APIs.  

**Q2. What is MVC architecture?**  
MVC stands for Model, View, Controller. It separates application logic into three components.  

**Q3. What is the role of Controller in MVC?**  
The controller handles incoming requests, processes them, and returns responses.  

---

## 3. Routing Concepts  

**Q1. What is routing in ASP.NET Core?**  
Routing maps URLs to specific controller actions.  

**Q2. What is attribute routing?**  
Routing defined using attributes like [HttpGet("route")].  

**Q3. What is dynamic routing?**  
Passing values through URL (e.g., /hello/Ash).  

---

## 4. Controller and Action Methods  

**Q1. What is an action method?**  
A method inside a controller that handles HTTP requests.  

**Q2. What does IActionResult represent?**  
It represents the result returned by a controller action (view, data, etc.).  

**Q3. What is the purpose of [HttpGet]?**  
It specifies that the method handles HTTP GET requests.  

---

## 5. Client-Server Communication  

**Q1. What is client-server architecture?**  
The client sends requests and the server processes and returns responses.  

**Q2. What acts as client and server in this practical?**  
Python script / browser → Client  
ASP.NET Core app → Server  

**Q3. How does Python communicate with .NET service?**  
Using HTTP requests through the requests library.  

---

## 6. Python Requests Library  

**Q1. What is requests library in Python?**  
A library used to send HTTP requests to web services.  

**Q2. What does requests.get() do?**  
It sends a GET request to the specified URL.  

**Q3. Why is verify=False used?**  
To bypass SSL certificate verification for local testing.  

---

## 7. Data Processing Concepts  

**Q1. How is temperature conversion handled?**  
Using mathematical formulas inside controller methods.  

**Q2. Formula for Celsius to Fahrenheit**  
F = (C × 9/5) + 32  

**Q3. Formula for Fahrenheit to Celsius**  
C = (F − 32) × 5/9  

---

## 8. URL and Parameter Passing  

**Q1. How are parameters passed in this API?**  
Through URL path (route parameters).  

**Q2. Example of route parameter**  
/c2f/25 → 25 is passed as input  

**Q3. What is RESTful URL design?**  
Using meaningful URLs to represent resources and operations.  

---

## 9. Advantages and Applications  

**Q1. Advantages of ASP.NET Core APIs**  
High performance, cross-platform, scalable  

**Q2. Advantages of using Python as client**  
Simple, flexible, easy integration  

**Q3. Where is this used in real life?**  
Microservices, web APIs, mobile app backends  

---

## 10. Comparison-Based Questions  

**Q1. Difference between ASP.NET Core and ASP.NET Framework**  
Core → Cross-platform, modern  
Framework → Windows-only, older  

**Q2. Difference between REST API and Web Application**  
REST API → Returns data  
Web App → Returns UI  

---

## 11. Error Handling and Security  

**Q1. Why is HTTPS used?**  
To secure communication between client and server.  

**Q2. What happens if wrong URL is entered?**  
Server returns error (e.g., 404 Not Found).  

---

## 12. Final Conceptual Question  

**Q. Explain how this practical demonstrates web services.**  
In this practical, ASP.NET Core MVC is used to create REST endpoints for greeting and temperature conversion. A Python client sends HTTP requests to these endpoints and receives responses, demonstrating client-server communication and interoperability between different technologies.  

---


