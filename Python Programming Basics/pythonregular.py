import re

inputstring = "1a."

print(re.findall("[a-zA-Z]|[0-9]",inputstring))

