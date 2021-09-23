from random import *


def password():
	c_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	s_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	symbols = ['%', '@', '!', '#', '$', '*', '^', '&', '_', '.']
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	print("Welcome")
	n_letters = int(input("How many letter in password\n"))
	n_symbols = int(input("How many symbols in password\n"))
	n_numbers = int(input("How many numbers in password\n"))

	tot = n_letters + n_symbols + n_numbers
	password_list = []

	for i in range(0, tot):
		rm = randint(1, 4)
		if rm == 1:
			c = randint(0, 25)
			password_list.append(c_letters[c])

		elif rm == 2:
			c = randint(0, 25)
			password_list.append(s_letters[c])

		elif rm == 3:
			c = randint(0, 9)
			password_list.append(symbols[c])

		elif rm == 4:
			c = randint(0, 9)
			password_list.append(numbers[c])

	Password = ''.join(password_list)
	print("Your Password that has been generated is")
	print(Password)
