import os
from os import rename
import sys
import unittest

import requests

from OpenSSL import SSL

print("   ")
print("   ")
print("==========Shift+Ctrl+P ==> command pallett ==========================")
print("====================================")
print("====================================")
print(SSL._CERTIFICATE_PATH_LOCATIONS)

print(sys.version)
print(sys.executable)

print("==========use 'Run Python file in Terminal' ==========================")
print("==== because 'Run Code Runner' is read-only and cannot accept an input =======")

name = input("Your Name?")
print("Hello, ", name)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

print(greet("World"))
print(greet("Corey"))

r = requests.get("https://www.google.com")
print(r.status_code)
print(r.ok)
