# Note this is the same solution for problem 67
def main():
	# reads the input file and parses into a list of lists
	input_file = '067_input.txt'
	with open(input_file) as f:
		data = f.readlines()
	data[:] = [x.split() for x in data]
	for num, line in enumerate(data):
		data[num] = map(int, line)

	final_tree = build_tree(data)
	max_val = max(final_tree[-1])
	print max_val


# takes a list of lists of nodes transformed already
def build_tree(data):
	new_list = list(data)
	for num, line in enumerate(data[1:], start=1):
		for num2, node in enumerate(line):
			if num2 == 0:
				new_list[num][num2] = data[num][num2]+data[num-1][0]
			elif num2 == (len(line)-1):
				new_list[num][num2] = data[num][num2]+data[num-1][-1]
			else:
				left = data[num][num2]+data[num-1][num2-1]
				right = data[num][num2]+data[num-1][num2]
				if left > right:
					new_list[num][num2] = left
				else:
					new_list[num][num2] = right
	return new_list

main()