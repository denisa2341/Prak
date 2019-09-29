import random
print("Welcome to the Cows and Bulls Game!")
n = random.randrange(1000 , 9999)
ans = 0
while n != ans:
	print("Enter a number:")
	ans = int(input())
	if ans > 9999 or ans < 1000:
		break
	comp = []
	n1 = n
	while n1 > 0:
		comp.append(n1%10)
		n1 = n1//10
	plr = []
	n2 = ans
	while n2 > 0:
		plr.append(n2%10)
		n2 = n2//10
	cows = 0
	bulls = 0
	for i in range(3):
		if comp[i] == plr[i]:
			cows +=1
			del comp[i]
			del plr[i]
	for x in comp:
		if x in plr:
			bulls +=1
	print(bulls , " - bulls")
	print(cows , " - cows")
	if n == ans:
		print("You win")