#!/usr/bin/python3
num1 = int(input("please enter your first number : "))
num2 = int(input("Enter the second number : "))
print(num1 + num2)
print(num1 * num2)
print(num1/num2)

if (num1 == num2) :
	print("they are equal")
elif (num1 < num2) :
	print("num2 is bigger")
elif (num1 > num2) :
	print("num1 is bigger")
