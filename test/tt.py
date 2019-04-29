import re


str='Showing 3,913,146 results'
str='320.08 in Thread'
#str = "a123b"
print re.findall(r"a(.+?)b",str)
result = re.findall(r"\d+(\.\d+)?", str)

print result

string="A1.45, b5, 6.45, 8.82"
print re.findall(r"\d+\.?\d*",string)[0]

# ['1.45', '5', '6.45', '8.82']

