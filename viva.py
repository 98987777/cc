
#Synchronous programming executes tasks sequentially, blocking further execution until the current task completes, making it simple but potentially slow.
#Asynchronous programming enables non-blocking,concurrent execution, allowing multiple tasks to run without waiting, significantly improving responsivenessand efficiency
==================================================================================================================================================
🔥 Final Viva Questions (Practical 1, 2, 3)
Cloud Computing & Web Services (Refined for Viva)
☁️ 1. Cloud Computing & IaaS
✅ Q1. What is Cloud Computing?

👉 Delivery of computing services (servers, storage, databases, networking) over the internet.

✅ Q2. What is IaaS?

👉 IaaS (Infrastructure as a Service) provides virtual machines, storage, and networking on demand.

✅ Q3. Examples of IaaS

👉 AWS EC2, Microsoft Azure VM, Google Compute Engine

✅ Q4. What is Virtualization?

👉 Technology that creates virtual versions of hardware resources.

✅ Q5. What is Hypervisor?

👉 Software that creates and manages virtual machines.

✅ Q6. Types of Hypervisors

👉

Type 1 → Bare metal (runs directly on hardware)
Type 2 → Hosted (runs on OS)
🖥️ 2. VMware, Xen Server, Hyper-V
✅ Q7. What is VMware ESXi?

👉 A Type 1 hypervisor used for enterprise virtualization.

✅ Q8. What is Xen Server?

👉 A hypervisor developed by Citrix for managing virtual machines.

✅ Q9. What is Hyper-V?

👉 A Microsoft hypervisor used for virtualization.

✅ Q10. Difference between ESXi, Xen Server, Hyper-V

👉 All are hypervisors from different vendors used for virtualization.

✅ Q11. What is Nested Virtualization?

👉 Running a virtual machine inside another virtual machine.

🌐 3. Web Services Basics
✅ Q12. What is a Web Service?

👉 A software system that enables communication between applications over a network.

✅ Q13. Types of Web Services

👉 SOAP and REST

✅ Q14. What is API?

👉 API (Application Programming Interface) allows communication between software systems.

✅ Q15. What is Endpoint?

👉 The URL where a web service is accessed.

🔗 4. REST API Concepts
✅ Q16. What is REST?

👉 REST (Representational State Transfer) is an architectural style using HTTP methods.

✅ Q17. HTTP Methods

👉

GET → Retrieve
POST → Create
PUT → Update
DELETE → Remove
✅ Q18. Difference between GET and POST

👉

GET → retrieve data
POST → send data
✅ Q19. What is JSON?

👉 JSON (JavaScript Object Notation) is a lightweight data format.

🧩 5. ASP.NET & Web Services
✅ Q20. What is ASP.NET?

👉 A web development framework developed by Microsoft.

✅ Q21. What is ASMX Web Service?

👉 A SOAP-based web service in ASP.NET.

✅ Q22. What is MVC Architecture?

👉

Model → data
View → UI
Controller → logic
✅ Q23. What is Controller?

👉 Handles incoming requests and returns responses.

🐍 6. Python Flask & FastAPI
✅ Q24. What is Flask?

👉 A lightweight Python web framework.

✅ Q25. What is FastAPI?

👉 A high-performance Python framework for building APIs.

✅ Q26. Difference between Flask and FastAPI

👉

Flask → simple, synchronous
FastAPI → faster, asynchronous
✅ Q27. What is Routing?

👉 Mapping URL to a function.

🔄 7. Client-Server Communication
✅ Q28. What is Client-Server Architecture?

👉 Client sends request, server processes and responds.

✅ Q29. Example in Practicals

👉

Client → Browser / Python / .NET
Server → Flask / FastAPI / Java / ASP.NET
✅ Q30. What is localhost?

👉 Local machine (127.0.0.1)

⚙️ 8. .NET Integration
✅ Q31. What is HttpClient?

👉 Used to send HTTP requests in .NET.

✅ Q32. What is async/await?

👉 Used for non-blocking asynchronous execution.

✅ Q33. Why integrate Python with .NET?

👉 For cross-platform communication.

🧾 9. SOAP Web Services (Java)
✅ Q34. What is SOAP?

👉 SOAP (Simple Object Access Protocol) is used for communication using XML.

✅ Q35. What is WSDL?

👉 WSDL (Web Services Description Language) describes web service structure.

✅ Q36. What is JAX-WS?

👉 Java API for creating SOAP web services.

✅ Q37. What is Apache Tomcat?

👉 Server to run Java web applications.

✅ Q38. What is Maven?

👉 Tool for project build and dependency management.

🔢 10. Data Handling & Logic
✅ Q39. What is Parsing?

👉 Converting one data type to another.

✅ Q40. What is Validation?

👉 Checking correctness of input.

✅ Q41. What is Algorithm?

👉 Step-by-step solution to a problem.

🔄 11. CRUD Operations
✅ Q42. What is CRUD?

👉

Create
Read
Update
Delete
✅ Q43. Mapping with HTTP

👉

POST → Create
GET → Read
PUT → Update
DELETE → Delete
⚠️ 12. Error Handling
✅ Q44. What is HTTP 404?

👉 Not Found

✅ Q45. What is HTTP 201?

👉 Created

✅ Q46. Why Error Handling is Important?

👉 To handle invalid inputs and avoid crashes.

🚀 13. Advantages & Applications
✅ Q47. Advantages of Web Services

👉 Reusable, scalable, platform independent

✅ Q48. Advantages of IaaS

👉 Cost-effective, flexible, scalable

✅ Q49. Real-world Applications

👉 Cloud computing, APIs, mobile apps
==================================================================================================================================================
#Practical 5 Viva Questions (ASP.NET ASMX Web Service)

1. What is ASMX?
👉 ASMX is a framework in ASP.NET used to create SOAP-based web service
ASMX = Active Server Method eXtension

2. What is a Web Service?
👉 A web service allows communication between applications over a network using HTTP.

3. What is SOAP?
👉 SOAP (Simple Object Access Protocol) is a protocol used to exchange data using XML.

4. What is Web Forms?
👉 ASP.NET Web Forms is a framework used to build UI using server controls.

5. What is [WebMethod]?
👉 It is used to expose a method as a web service.

6. Why do we create WebService1 object?
WebService1 t = new WebService1();
👉 To call web service methods inside WebForm.

7. What is Double.Parse()?
👉 Converts string input into double data type.

8. What is Namespace?
👉 A namespace is used to organize classes and avoid naming conflicts.

9. What is tempuri.org?
👉 Default namespace used for testing web services.

10. What is Code Behind?
👉 The .aspx.cs file where backend logic is written.

11. What is Label control?
👉 Used to display output.

12. What is TextBox?
👉 Used to take user input.

13. What is Button Click Event?
👉 Event triggered when button is clicked.

#IMPORTANT TRICKY QUESTIONS
What happens if [WebMethod] is not used? Method will NOT be accessible as web service
What protocol does ASMX use? SOAP
What format is used in ASMX? XML
Can ASMX use JSON? No (it is SOAP-based → uses XML)
What is difference between Web Form and Web Service? Web Form → UI and Web Service → logic / backend

#MOST ASKED (VERY HIGH CHANCE)
⭐ What is difference between SOAP and REST? SOAP → XML, protocol, REST → JSON, lightweight
⭐ What is WSDL? WSDL (Web Services Description Language) describes web service.

#HOW TO ANSWER (important)
👉 “ASMX is used to create SOAP web services in ASP.NET.”
👉 “WebMethod exposes functions as web services.”
👉 “We use WebService1 object to call methods.”
==================================================================================================================================================

#Practical 6 & 7 Viva Questions (Flask)
1. What is Flask?
👉 Flask is a micro web framework written in Python used to build web applications and APIs.

2. What is a Web Framework?
👉 A web framework is a tool that helps developers build web applications easily by providing predefined functions and structure.

3. What is an API?
👉 API (Application Programming Interface) allows communication between different software systems.

4. What is a Web Service?
👉 A web service is an API that works over the internet using HTTP protocol.

5. What is HTTP?
👉 HTTP (HyperText Transfer Protocol) is used for communication between client and server.

6. What is GET method?
👉 GET is used to retrieve data from the server.

7. What is POST method?
👉 POST is used to send data to server securely.

8. What is @app.route()?
👉 It is a decorator used to define URL routes in Flask.

✅ 10. What is a decorator?
👉 A decorator is a function that modifies another function’s behavior.

✅ 11. What is jsonify()?
👉 Converts Python dictionary into JSON format.

📌 Full form:
JSON = JavaScript Object Notation

✅ 12. What is request object?
👉 Used to get data sent by client (GET or POST).
==================================================================================================================================================
#Practical 8 Viva Questions

1. What is Client-Server Architecture?
👉A model where: Client sends request and Server processes request and sends response

2. Who is Client and Server in this practical?
👉Python script → Client
  ASP.NET application → Server
  
3. What is ASP.NET? (Active Server Pages)
👉 ASP.NET is a web framework developed by Microsoft to build web applications.

4. What is MVC?
👉 MVC (Model View Controller) is a design pattern:
    Model → Data
    View → UI
    Controller → Logic
    
5. What is a Controller?
👉 A controller handles incoming requests and returns responses.

6. What is IActionResult?
👉 It is a return type used in ASP.NET to return different types of responses.

7. What is HttpGet attribute?
👉 Used to specify that a method handles GET requests.

8. What is URL parameter?
👉 Data passed in URL.

Example:
/hello?name=Riddhi

9. What is Python requests library?
👉 A library used to send HTTP requests in Python.

10. What is requests.get()?
👉 Used to send a GET request to a server.

11. What is response object?
👉 Stores server response.

12. What is response.text?
👉 Contains the response content as string.

13. What is verify=False?
👉 Disables SSL certificate verification.

14. What is HTTPS?
👉 HTTPS = HyperText Transfer Protocol Secure
👉 Secure version of HTTP.

15. What is localhost?
👉 Refers to your own machine (local server)
==================================================================================================================================================
#Practical 9 Viva Questions

1. What is FastAPI?
👉 FastAPI is a modern Python web framework used to build APIs quickly and efficiently.

2. Why is FastAPI called “fast”?
👉 Because it supports asynchronous programming and is built on high-performance libraries.

3. What is API?
👉 API (Application Programming Interface) allows communication between different systems.

4. What is Cross-platform communication?
👉 Communication between applications built using different technologies.
👉 Example: Python (FastAPI) ↔ .NET

5. What is Uvicorn?
👉 Uvicorn is an ASGI server used to run FastAPI applications.

6. What is ASGI (Asynchronous Server Gateway Interface)?
👉 ASGI is a standard interface between web server and Python applications (supports async).

7. Difference between WSGI and ASGI?
Feature	                    WSGI	                                ASGI
Full form	    Web Server Gateway Interface	Asynchronous Server Gateway Interface
Type	                Synchronous	                            Asynchronous
Used in	                    Flask	                                FastAPI

8. What is @app.get()?
👉 It defines a GET API endpoint in FastAPI.

9. What is query parameter?
👉 Data passed in URL.
    Example:
    /hello?name=Riddhi
    
10. What is JSON?
👉 JSON (JavaScript Object Notation) is used for data exchange.

11. What is HttpClient in .NET?
👉 A class used to send HTTP requests and receive responses.

12. What is async and await?
👉 Used for asynchronous programming to improve performance.

13. What is port 8000?
👉 Default port used by FastAPI server.

#IMPORTANT TRICKY QUESTIONS
1. Difference between Flask and FastAPI?

        Flask → simple, synchronous
        FastAPI → faster, asynchronous

    Can FastAPI handle multiple requests at same time? Yes (due to async support)

    Why use async? Improves performance and handles multiple users efficiently.

    What happens if port is already used? Server will not start (error occurs)

    What protocol is used? HTTP

    What is cross-platform? Different technologies communicating together.

==================================================================================================================================================
#Practical 10 Viva Questions (SOAP Web Service – Java)

1. What is SOAP?
👉 SOAP (Simple Object Access Protocol) is a protocol used to exchange data between applications using XML format.

2. What is a Web Service?
👉 A web service is a software system that allows communication between applications over a network using HTTP.

3. What is WSDL?
👉 WSDL (Web Services Description Language) is an XML file that describes:
    Available methods
    Input/output
    Service location
    
4. What is JAX-WS?
👉 JAX-WS (Java API for XML Web Services) is used to create SOAP web services in Java.

5. What is Maven?
👉 Maven is a build automation tool used to manage dependencies and project structure.

6. What is Tomcat?
👉 Apache Tomcat is a web server used to deploy and run Java web applications.

7. What is WAR file?
👉 WAR (Web Application Archive) is a packaged file used to deploy web applications.

8. Why do we use <packaging>war</packaging>?
👉 To package the project as a deployable web application.

9. What is @WebService?
👉 Annotation used to define a class as a web service.

10. What is @WebMethod?
👉 Annotation used to expose a method as a web service operation.

11. What is web.xml?
👉 Deployment descriptor that configures servlet and URL mapping.

12. What is sun-jaxws.xml?
👉 Configuration file that maps Java class to web service endpoint.

13. What is endpoint?
👉 URL where web service is available.
    Example:
    /HelloService

14. What is XML?
👉 XML (eXtensible Markup Language) is used for data exchange in SOAP.

15. What is SOAP UI?
👉 Tool used to test SOAP web services.


Difference between SOAP and REST?
                        SOAP	            REST
                        Protocol	Architecture
                        Uses XML	Uses JSON
                        Heavy	        Lightweight
                        More secure	  Faster

Can SOAP use JSON? No, SOAP uses only XML

=> Why do we need Tomcat?
👉 To host and run Java web applications


#MOST ASKED (VERY HIGH PROBABILITY)
⭐ What is difference between WSDL and SOAP? SOAP → protocol, WSDL → description of service
⭐ What is endpoint URL? URL where service is available
⭐ What is dependency in pom.xml? External libraries required for project
⭐ Why XML is used in SOAP? Standard format for structured data exchange
