#!/usr/bin/python3

var1 = (raw_input("enter first string : "))
var2 = (raw_input("enter second string : "))
var3 = (int(input("enter a number between 1 and 3 : ")))
if (var3 < 1) or (var3 > 3) :
	var3 = (int(input("please try again : ")))	
	
var1len = len(var1)
var2len = len(var2)

if (var1len > var2len) and (var1len > var3) :
	print("var1 length is bigger ")
elif (var2len > var1len) and (var2len > var3) :
	print("var2 length is bigger ") 
elif (var3 > var1len) and (var3 > var2len) :
	print("var3 length is bigger ")

if (var1 in var2 and var3) :
	print var1 ("is in them")
