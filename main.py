import random


def pt():
	food = random.randint(1, 2)
	if food == 1:
		print("TOMATO")
	else:
		print("POTATO")
	food2 = input("Potato Or Tomato? ")
	if food2 == "Tomato":
		if food == 1:
			print("CORRECT")
			print("")
			pt()
		else:
			print("WRONG")
			print("")
			pt()
	elif food2 == "Potato":
		if food == 2:
			print("CORRECT")
			print("")
			pt()
		else:
			print("WRONG")
			print("")
			pt()
	else:
		print("YOU SPEELLDE THAT WRONG")
		print("")
		pt()


pt()