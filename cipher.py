def encode(x):
	lst = []
	spaces = int(input("Enter no. of spaces you want to Enter "))
	for i in x:
		converting = ord(i) + spaces
		lst.append(chr(converting))
	Str = ''.join(lst)
	return Str


def decode(x):
	lst = []
	spaces = int(input("Enter no. of spaces you have Enter "))
	for i in x:
		converting = ord(i) - spaces
		lst.append(chr(converting))
	Str = ''.join(lst)
	return Str


def encode_decode():
	choose = input("Do you want to encode or decode ")
	if choose.lower() == "encode":
		number = input("Enter your code")
		result = encode(number)
		print(result)


	elif choose.lower() == "decode":
		number = input("Enter your code")
		result = decode(number)
		print(result)
	else:
		print("you have entered wrong option")
		encode_decode()
	flag = 0
	while flag != 1:
		chart = input("Do you want to continue 'Y' for Yes and 'N' for No ")
		if chart.upper() == 'Y':
			encode_decode()
			flag = 1
		elif chart.upper() == 'N':
			flag = 1
		else:
			print("you have entered wrong option")
