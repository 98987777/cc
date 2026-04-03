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




