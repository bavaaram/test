st = input()
start, i, paras = 0, 0, []
for m in st:
	if m == " ":
		paras.append(st[start:i])
		start = i + 1
	else: pass
	i += 1
paras.append(st[start:i])	
n, x, k = int(paras[0]), int(paras[1]) - 1, int(paras[2])
name = []
for i in range(n):
	name.append(input())
for j in range(k):
	if x == (n - 1):
		x = 0
	else:
		x += 1
print(name[x])
