#https://play.picoctf.org/practice/challenge/427

import base64

encoded_value = "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9"

decoded_value = base64.b64decode(encoded_value).decode("utf-8")
print("Decoded value:", decoded_value)