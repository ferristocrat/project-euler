power = input('Enter a number: ')

number = 2 ** power
number = str(number)

output = 0

for x in number:
	output += int(x)

print (output)