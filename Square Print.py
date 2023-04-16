n = int(input())
def star(n, k):
    print("*" * n) if (k == 0 or k == n - 1) else print("*" + (" " * (n - 2)) + "*")
[star(n, i) for i in range(n)]
