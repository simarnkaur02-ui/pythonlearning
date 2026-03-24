#Two type of modules in python:
#- Build in Modules 
#   - External Modules
    
#  list of all the built in modules: https://docs.python.org/3/py-modindex.html

import math
import os 
import mymodules
import requests

print(math.sqrt(16))

mymodules.hello()

r = requests.get("https://www.google.com")
print('testttttttttttttttttttttttttttttttttttttt',r.text)