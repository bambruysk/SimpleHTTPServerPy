import requests 
import unittest

response = requests.get(r'http://127.0.0.1:8000')

print(response)