<<<<<<< HEAD
from random import randint

def printArr(arr, n) :
	for i in range(n) :
		print(arr[i], end = " ")

def randomList(m, n):
	arr = [0] * m
	for i in range(n) :
        print(randint(0, n) % m)
        prin
		arr[randint(0, n) % m] += 1
	printArr(arr, m)



n = int(input("Enter Total Number :- "))
m = int(input("Enter Random Number :- "))
=======
from random import randint

def printArr(arr, n) :
	for i in range(n) :
		print(arr[i], end = " ")

def randomList(m, n):
	arr = [0] * m
	for i in range(n) :
        print(randint(0, n) % m)
        prin
		arr[randint(0, n) % m] += 1
	printArr(arr, m)



n = int(input("Enter Total Number :- "))
m = int(input("Enter Random Number :- "))
>>>>>>> 5f13f01fb3310c1cd630e84b82790a0e8749c085
randomList(m, n)