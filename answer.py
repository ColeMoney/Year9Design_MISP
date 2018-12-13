# get user input using input() function
num = input(" enter a number: ")
# converting or casting string to an integer
num = int(num)

mylist = {1,2,3,4,5}
for n in mylist:
	if (n == num):
		print("you found it " + str(num))
		break
	else:
		print(str(num) +  " is not equal to " + str(n))