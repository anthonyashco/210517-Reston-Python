n = int(input("Input Triforce size: "))

triangle = ["*" * (i * 2 - 1) for i in range(1, n + 1)]
gap = [" " * (n - i) for i in range(1, n + 1)]
pad = " " * n

for i in range(n):
    if i == 0:
        print("." + pad[1:] + gap[i] + triangle[i])
    else:
        print(pad + gap[i] + triangle[i])

for i in range(n):
    print(gap[i] + triangle[i] + 2 * gap[i] + " " + triangle[i])
