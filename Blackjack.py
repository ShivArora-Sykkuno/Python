from random import *


def blackjack():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

	user_card_1 = choice(cards)
	user_card_2 = choice(cards)
	user_card_3 = 0

	comp_card_1 = choice(cards)
	comp_card_2 = choice(cards)
	comp_card_3 = 0

	user_sum = user_card_2 + user_card_1
	comp_sum = comp_card_2 + comp_card_1

	print(f"Your Cards: {[user_card_1, user_card_2]} ")
	print(f"Computer Card: {comp_card_1, comp_card_2} ")

	while user_sum <= 21 and comp_sum <= 21:
		print("Type 'Y' tp get another card, type 'N' to pass: ")
		yn = input()
		if yn.upper() == 'Y':
			user_card_3 = choice(cards)
			print(f"You picked  {user_card_3}")
			if user_card_3 + user_card_2 + user_card_1 > 21:
				if user_card_1 == 11:
					user_card_1 = 1
				elif user_card_2 == 11:
					user_card_2 = 1
				elif user_card_3 == 11:
					user_card_3 = 1

				if user_card_3 + user_card_2 + user_card_1 > 21:
					user_sum = 0
					break

			elif user_card_3 + user_card_2 + user_card_1 < 21:
				user_sum += user_card_3
				if comp_card_2 + comp_card_1 < 17:
					comp_card_3 = choice(cards)
				else:
					break

				if comp_card_3 + comp_card_2 + comp_card_1 > 21:
					if comp_card_1 == 11:
						comp_card_1 = 1
					elif comp_card_2 == 11:
						comp_card_2 = 1
					elif user_card_3 == 11:
						comp_card_3 = 1

					if comp_card_3 + comp_card_2 + comp_card_1 > 21:
						comp_sum = 0
						break
				elif comp_card_3 + comp_card_2 + comp_card_1 < 21:
					comp_sum += comp_card_3

		elif yn.upper() == 'N':
			break

	if user_sum == comp_sum:
		print("Draw")
		if comp_card_3 != 0:
			print(f"Computer cards were {[comp_card_1, comp_card_2, comp_card_3]}")
		else:
			print(f"Computer cards were {[comp_card_1, comp_card_2]}")
		if user_card_3 != 0:
			print(f"Your cards were {[user_card_1, user_card_2, user_card_3]}")
		else:
			print(f"Your cards were {[user_card_1, user_card_2]}")
	elif user_sum > comp_sum:
		print("You Won")
		if comp_card_3 != 0:
			print(f"Computer cards were {[comp_card_1, comp_card_2, comp_card_3]}")
		else:
			print(f"Computer cards were {[comp_card_1, comp_card_2]}")
		if user_card_3 != 0:
			print(f"Your cards were {[user_card_1, user_card_2, user_card_3]}")
		else:
			print(f"Your cards were {[user_card_1, user_card_2]}")
	else:
		print("You Lost")
		if comp_card_3 != 0:
			print(f"Computer cards were {[comp_card_1, comp_card_2, comp_card_3]}")
		else:
			print(f"Computer cards were {[comp_card_1, comp_card_2]}")
		if user_card_3 != 0:
			print(f"Your cards were {[user_card_1, user_card_2, user_card_3]}")
		else:
			print(f"Your cards were {[user_card_1, user_card_2]}")
