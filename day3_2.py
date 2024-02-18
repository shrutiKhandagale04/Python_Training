"""try:
    result = 10/0
    value = int('abc')
except ValueError: print('Invalid value')
except ZeroDivisionError: print('Zero error')
except Exception as e: print(e)
"""

#r= raw format, re=regular expression
import re
text = 'The cat is cute cut ctt'
pattern = r"c.t" #a pattern with single character between two characters
result = re.search(pattern, text)
print(result)

pattern = r"^hello" # displays what starts with hello
text = "hellogod, hello world"
result = re.search(pattern,text)
print(result)

pattern = r"world$" #ends with world
text = "hello world, hllogof happyworld"
result = re.search(pattern,text)
print(result)

pattern = r"[aeiou]" # matches any lowecase alphabetic characters
text = "hello World"
result = re.findall(pattern,text)
print(result)

pattern = r"[^0-9]" #matches any characters that is not a digit
text = "hello, worls 1 2 3 4 "
result = re.findall(pattern,text)
print(result)

pattern = r"[a-z]"
text = "hello world 1233!"
result = re.findall(pattern,text)