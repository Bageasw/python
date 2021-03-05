
def odd_nums(n):
    for i in range(1, n + 1, 2):

        yield i
for i in odd_nums(15):
    print(i)

n = int(input())
print(*[i for i in range(1, n + 1, 2)])