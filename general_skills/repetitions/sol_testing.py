#VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
#RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
#MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
#VkpEVGxaYVdFMVhSbHBWV0VKVVZGWm9RMlZzV2tWUmJFNVNDbUpXV25wWmExSmhWMGRHZEdWRlZs
#aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==

#only info was given in the cat it was stored is as base 64

import base64


with open('enc_flag') as file:
    data = file.read()

while 'picoCTF' not in data:        #search for unkownen const
    data = base64.b64decode(data).decode('utf8')

print(data) 