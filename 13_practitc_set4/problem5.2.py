import requests # pip install requsts

a = requests.get("https://api.github.com/")

print(a.json())
