print("Write name 1 ")
player1 = input()
print("Write name 2 ")
player2 = input()
while 1:
	print("You can choose 'Rock' , 'Paper' or 'Scissors' ")
	c = ("Rock" , "Paper" , "Scissors")
	print("Write your element (player 1)")
	a = input();
	print("Write your element (player 2)")
	b = input();
	if a in c and b in c:
		if a == "Rock":
			if b == "Scissors":
				print(player1 ," winner")
			elif b == "Rock":
				print("draw")
			else:
				print(player2 ," winner")
		if a == "Scissors":
			if b == "Paper":
				print(player1 ," winner")
			elif b == "Scissors":
				print("draw")
			else:
				print(player2 ," winner")
		if a == "Paper":
			if b == "Rock":
				print(player1 ," winner")
			elif b == "Paper":
				print("draw")
			else:
				print(player2 ," winner")
	else:
		if a == "exit" or b == "exit":
			break
		else:
			print("no element")

