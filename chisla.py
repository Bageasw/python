from random import randint
f = 11
src = []

while f > 0 :

    src.append(randint(0, 999))
    f -= 1

print(src)

big = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(big)