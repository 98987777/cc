#1. Fibonacci Series
Steps:
    Create ASP.NET Web Application (.NET Framework) → Web Forms
    Add WebForm1.aspx
    Add controls:
    Label → “Enter Number”
    TextBox → num
    Button → fib (Text: Generate Fibonacci)
    Label → result
    Double-click button to create event
    Add WebService1.asmx
    Write Fibonacci logic
    Call service in button click
    Build and Run
    
#WebForm1.aspx.cs
using System;
namespace WebServices
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void fib_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            result.Text = t.Fibonacci(int.Parse(num.Text));
        }
    }
}

#WebService1.asmx.cs
using System.Web.Services;

namespace WebServices
{
    public class WebService1 : WebService
    {
        [WebMethod]
        public string Fibonacci(int n)
        {
            int a = 0, b = 1;
            string series = "";

            for (int i = 0; i < n; i++)
            {
                series += a + " ";
                int temp = a + b;
                a = b;
                b = temp;
            }

            return series;
        }
    }
}
=================================================================
#2. Odd / Even
Steps:

(Same steps as above, only change button text → “Check Odd/Even”)

#WebForm1.aspx.cs
using System;
namespace WebServices
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void oddeven_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            result.Text = t.CheckOddEven(int.Parse(num.Text));
        }
    }
}

#WebService1.asmx.cs
[WebMethod]
public string CheckOddEven(int num)
{
    if (num % 2 == 0)
        return "Even";
    else
        return "Odd";
}
========================================================================
#3. Multiplication Table
✅ Steps:

(Same steps, button text → “Generate Table”)

#WebForm1.aspx.cs
using System;
namespace WebServices
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void table_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            result.Text = t.Table(int.Parse(num.Text));
        }
    }
}

#WebService1.asmx.cs
[WebMethod]
public string Table(int num)
{
    string result = "";

    for (int i = 1; i <= 10; i++)
    {
        result += num + " x " + i + " = " + (num * i) + "<br/>";
    }

    return result;
}
=================================================================
#4. Prime Number
Steps:

(Same steps, button text → “Check Prime”)

#WebForm1.aspx.cs
using System;
namespace WebServices
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void prime_Click(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();
            result.Text = t.CheckPrime(int.Parse(num.Text));
        }
    }
}

#WebService1.asmx.cs
[WebMethod]
public string CheckPrime(int num)
{
    if (num <= 1)
        return "Not Prime";

    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
            return "Not Prime";
    }

    return "Prime";
}






for viva- 

# Practical Viva Questions  
## ASP.NET Web Services – Basic Programs (Fibonacci, Odd/Even, Table, Prime)  

---

## 1. Web Service Concepts  

**Q1. What is a Web Service?**  
A web service is a software component that allows applications to communicate over a network.  

**Q2. What is ASMX Web Service?**  
ASMX is a framework in ASP.NET used to create SOAP-based web services.  

**Q3. What is a WebMethod?**  
A method marked with [WebMethod] that can be accessed by clients over the web.  

---

## 2. ASP.NET and Architecture  

**Q1. What is ASP.NET?**  
ASP.NET is a web development framework by :contentReference[oaicite:0]{index=0} used to build web applications and services.  

**Q2. What is client-server architecture in this practical?**  
The Web Form acts as a client and the Web Service acts as a server.  

**Q3. How does the Web Form communicate with the Web Service?**  
By calling methods of the web service through object creation.  

---

## 3. Programming Logic Concepts  

**Q1. What is an algorithm?**  
A step-by-step procedure to solve a problem.  

**Q2. Why are loops used in this practical?**  
To perform repeated operations like generating series or tables.  

**Q3. What is conditional statement?**  
A decision-making statement like if-else used to control program flow.  

---

## 4. Fibonacci Series  

**Q1. What is Fibonacci series?**  
A sequence where each number is the sum of the previous two numbers.  

**Q2. What is the starting sequence of Fibonacci?**  
0, 1, 1, 2, 3, 5...  

**Q3. Where is Fibonacci used?**  
Mathematics, algorithms, data structures, and nature patterns.  

---

## 5. Odd and Even Concept  

**Q1. How do you check if a number is even?**  
If number % 2 == 0, it is even.  

**Q2. How do you check if a number is odd?**  
If number % 2 != 0, it is odd.  

**Q3. What is modulus operator (%)?**  
It returns the remainder of a division.  

---

## 6. Multiplication Table  

**Q1. What is a multiplication table?**  
A list showing multiples of a number.  

**Q2. Why use loops for table generation?**  
To repeat multiplication from 1 to 10 automatically.  

**Q3. What is string concatenation?**  
Combining multiple strings into one output.  

---

## 7. Prime Number Concept  

**Q1. What is a prime number?**  
A number divisible only by 1 and itself.  

**Q2. Why is 1 not a prime number?**  
Because it has only one factor.  

**Q3. How do you check a prime number?**  
By checking divisibility from 2 to n-1.  

---

## 8. Data Handling and Validation  

**Q1. Why use int.Parse()?**  
To convert string input into integer.  

**Q2. What happens if invalid input is entered?**  
It causes a runtime error.  

**Q3. How can input validation be improved?**  
Using try-catch or validation controls.  

---

## 9. Advantages and Applications  

**Q1. Advantages of using Web Services**  
Reusability, platform independence, modular design  

**Q2. Where can such services be used?**  
Online calculators, educational apps, APIs  

**Q3. Why separate logic into Web Service?**  
To reuse logic across multiple clients  

---

## 10. Final Conceptual Question  

**Q. Explain how this practical demonstrates web services.**  
In this practical, different logic operations like Fibonacci, prime checking, and table generation are implemented in a web service. The web form sends input to the service, which processes it and returns the result, demonstrating client-server communication and reusable services.  

---
