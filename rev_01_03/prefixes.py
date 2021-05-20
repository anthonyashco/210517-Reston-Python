n = int(input())
words = []
for i in range(n):
    words.append(input())

for word in words:
    prefix = ""
    for i in range(len(word)):
        if i == len(word):
            break
        prefix = prefix + word[i]
        hits = 0
        for check in words:
            if i < len(check) and word[:i + 1] == check[:i + 1]:
                hits += 1
        if hits == 1:
            break
    print(prefix)