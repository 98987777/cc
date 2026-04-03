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
