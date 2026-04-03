#convert temperature from Celsius to Fahrenheit and Fahrenheit to Celsius.

#Steps: -
1. Open Visual Studio 2019.
2. Click on Create a new project.
3. Select ASP.NET Web Application (.NET Framework) and click Next.
4. Enter the project details:
    Project Name: WebServices
    Location: As per requirement
    Click Create.
5. Select Web Forms as the project template.
6. Set Authentication to No Authentication and click Create.
7. After the project is created, right-click on the project name in Solution Explorer.
8. Select Add → New Item.
9. Choose Web Form, name it WebForm1.aspx, and click Add.
10. Open WebForm1.aspx and switch to Design View.
11. From the Toolbox, drag and drop the following controls:
        o Label → “Enter temperature in Celsius”
        o TextBox → ID: celbox
        o Button → Text: “Convert to Fahrenheit”, ID: ctof
        o Label → ID: fah
        o Label → “Enter temperature in Fahrenheit”
        o TextBox → ID: fahbox
        o Button → Text: “Convert to Celsius”, ID: ctoc
        o Label → ID: cel
12. Double-click both buttons to generate click event handlers in WebForm1.aspx.cs.
13. Right-click on the project name again.
14. Select Add → New Item.
15. Choose Web Service (ASMX), name it WebService1.asmx, and click Add.
16. Open WebService1.asmx.cs and define WebMethods for Celsius to Fahrenheit and
Fahrenheit to Celsius conversion.
17. Open WebForm1.aspx.cs and create an object of WebService1.
18. Call the Web Service methods inside the button click events and display the result in
the respective labels.
19. Save all the files.
20. Click on Build → Rebuild Solution.
21. Run the application by clicking Start (▶).
22. Enter temperature values in the text boxes and observe the converted output.

UI: -

#WebForm1.aspx.cs: -

using System;
namespace WebServices
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        // Celsius to Fahrenheit
        protected void ctof_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            fah.Text = t.CelsiusToFarenheit(
                Double.Parse(celbox.Text)
            ).ToString();
        }
        // Fahrenheit to Celsius
        protected void ctoc_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            cel.Text = t.FarenheitToCelsius(
                Double.Parse(fahbox.Text)
            ).ToString();
        }
    }
}

#WebService1.asmx.cs: -

using System.Web.Services;
namespace WebServices
{
    [WebService(Namespace = &quot;http://tempuri.org/&quot;)]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    public class WebService1 : WebService

    {
        [WebMethod]
        public double CelsiusToFarenheit(double cel)
        {
            return (cel * 9 / 5) + 32;
        }
        [WebMethod]
        public double FarenheitToCelsius(double fahr)
        {
            return (fahr - 32) * 5 / 9;
        }
    }
}
==============================================================================================





For Viva-
# Practical Viva Questions  
## Temperature Conversion Web Service using ASP.NET (.NET Framework)  

---

## 1. Web Service Concepts  

**Q1. What is a Web Service?**  
A web service is a software component that allows communication between applications over a network using standard protocols.  

**Q2. What is an ASMX Web Service?**  
ASMX is a web service framework in ASP.NET used to create SOAP-based web services.  

**Q3. What is SOAP?**  
SOAP (Simple Object Access Protocol) is a protocol used for exchanging structured information in web services.  

**Q4. What is the purpose of a WebMethod?**  
It exposes a method so that it can be accessed by clients over the web.  

---

## 2. ASP.NET Concepts  

**Q1. What is ASP.NET?**  
ASP.NET is a web development framework by :contentReference[oaicite:0]{index=0} used to build dynamic web applications and services.  

**Q2. What is a Web Form in ASP.NET?**  
A Web Form is a page used to create user interfaces with controls like buttons, labels, and textboxes.  

**Q3. What is code-behind in ASP.NET?**  
It is the backend C# file where logic and event handling are written.  

---

## 3. Client-Server Interaction  

**Q1. How does the Web Form interact with the Web Service?**  
The Web Form calls methods of the web service to process data and display results.  

**Q2. What is client-server architecture?**  
A model where the client requests services and the server processes and responds.  

**Q3. What happens when a button is clicked in Web Form?**  
An event is triggered, and the corresponding method is executed in the code-behind file.  

---

## 4. Data Handling Concepts  

**Q1. Why is Double.Parse used?**  
To convert input from string (textbox) into numeric (double) format.  

**Q2. What will happen if invalid input is entered?**  
It will cause a runtime error (format exception).  

**Q3. How can input validation be improved?**  
By using try-catch blocks or validation controls.  

---

## 5. Temperature Conversion Logic  

**Q1. Formula to convert Celsius to Fahrenheit**  
F = (C × 9/5) + 32  

**Q2. Formula to convert Fahrenheit to Celsius**  
C = (F − 32) × 5/9  

**Q3. Why are these formulas used?**  
They convert temperature values between two standard measurement scales.  

---

## 6. Application Logic  

**Q1. What is the role of WebService1 class?**  
It contains methods for temperature conversion.  

**Q2. Why create an object of WebService1 in WebForm?**  
To access and call its methods.  

**Q3. What is the flow of execution in this application?**  
User input → Button click → Web service method call → Result displayed  

---

## 7. Advantages and Limitations  

**Q1. Advantages of using Web Services**  
Platform independent, reusable, supports distributed systems  

**Q2. Limitations of ASMX Web Services**  
Uses SOAP (heavy), less flexible compared to modern APIs  

**Q3. What is a modern alternative to ASMX?**  
RESTful Web Services or Web API  

---

## 8. Comparison-Based Questions  

**Q1. Difference between Web Service and Web Application**  
Web Service → Provides data/services  
Web Application → Provides user interface  

**Q2. Difference between SOAP and REST**  
SOAP → Protocol, XML-based, heavier  
REST → Architectural style, lightweight, uses JSON  

---

## 9. Error Handling and Improvements  

**Q1. How can you handle errors in this application?**  
Using try-catch blocks and validation controls  

**Q2. How can this application be improved?**  
Add input validation, use Web API, improve UI  

---

## 10. Final Conceptual Question  

**Q. Explain how this practical demonstrates a web service.**  
In this practical, a web service is created to perform temperature conversion. The web form acts as a client that sends input to the service, which processes the data and returns the result, demonstrating client-server communication using web services.  

---
