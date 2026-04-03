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
