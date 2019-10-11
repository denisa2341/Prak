import random
print(" Welcome to the Cows and Bulls Game! ")
n = random.randrange(0 , 9999)
ans = -1
while n != ans:
	print("Enter a number:")
	ans = int(input())
	if ans > 9999 or ans < 0:
		break
	comp = []
	n1 = n
	for i in range(4):
		comp.append(n1%10)
		n1 = n1//10
	plr = []
	n2 = ans
	for i in range(4):
		plr.append(n2%10)
		n2 = n2//10
	cows = 0
	bulls = 0
	for i in range(4):
		if comp[3-i] == plr[3-i]:
			bulls +=1
			del comp[3-i]
			del plr[3-i]
	for x in comp:
		if x in plr:
			cows +=1
	print(bulls , " - bulls")
	print(cows , " - cows")
	if n == ans:
		print("You win")
