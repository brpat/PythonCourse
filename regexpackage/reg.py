import re

pattern = re.compile('this')
text = 'search inside this string please'
# a is a match object
a = pattern.search(text)
# Find all instances.
b = pattern.findall(text)
print(a)
print(a.span())
print(a.group())
print(b)


# Emails.
test_string = "Please send to brpatel0807@gmail.com when you get a chance"


