#! /usr/bin/python3

n = input("")
x = int(input("Current Position "))
k = int(input("Times press bottun"))
name = dict()

for i in range(int(n)):
	name[i + 1] = input()
for j in range(k):
	if x == int(n):
		x = 1
		continue
	x += 1
print(name[x])
