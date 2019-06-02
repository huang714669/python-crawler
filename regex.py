import re
test_string = 'hello'

# result = re.search('l',test_string)
# result = re.findall('l',test_string)
result = re.sub('l','m',test_string)
print(result)