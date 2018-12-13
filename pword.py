secret = "joe"

num = 2
num = int(num)
while (num < 3):
	pword = input("enter a password: ")
	
	if (secret == pword):
		print("welcome")
		break 
	else:
		print("incorrect ...")