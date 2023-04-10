def prime_check(numm):
    flag = True
    for i in range(2, int((numm ** 0.5) + 1)):
        if (numm % i == 0) or (numm == 1):
            flag = False
            break
    if (numm == 2):
        flag = True
    return flag

n = int(input())
ini = range(1, 10)
lis_t = [2, 3, 5, 7]
for i in range(2, n + 1):
    lis_t2 = list()
    for j in lis_t:
        for m in ini:
            casee = (10 * j) + m
            if prime_check(casee):
                lis_t2.append(casee)
                lis_t = lis_t2
for n in range(len(lis_t)):
    print(lis_t[n])
