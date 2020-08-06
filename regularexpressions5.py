# find all numbers in the text and return them to me as strings
# if without + it gives 2,1,9,4,2
# if with * it gives a "," for every non number and 2,1,9,4,2 in between
# with + it gives 2,19,42. + means one or more times
import re
x = 'my favorite numbers are 2 followed by 19 and 42'
y = re.findall ('[0-9]+',x)
print (y)