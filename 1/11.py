def fun(n):
	for i in range(n):
		if n % (i + 1) == 0:
			if (i+1) != n and i != 0:
				return "no prime"
	return "prime"
	return answer
n = int(input())
print(fun(n))
