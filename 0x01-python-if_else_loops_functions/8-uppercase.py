#!/usr/bin/python3
# 8-uppercase.py
# ikenna


def uppercase(str):

	for i in str:
		if ord(i) >= 97 and ord(i) <= 122:
			c= chr(ord(i) - 32)
		print("{}".format(i), end="")
	print("")
