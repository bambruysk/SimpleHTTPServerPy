import requests 
import unittest

response = requests.post(r'http://127.0.0.1:8000/test')

print(response)