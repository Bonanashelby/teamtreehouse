import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'
print(re.match(last_name, data))
print(re.search(first_name, data))