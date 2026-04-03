
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

