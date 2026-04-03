import requests
import pyperclip

url = "https://raw.github.com/98987777/cc/refs/heads/main/p3.py"

code = requests.get(url)

print(code.text)
pyperclip.copy(code.text)


