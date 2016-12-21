input_number = input('Enter a number: ')

list = []

for x in xrange(2,input_number):
	if (x % 3 == 0) or (x % 5 == 0):
		list.append(x)
output = 0
for x in list:
	output += x

print (output)