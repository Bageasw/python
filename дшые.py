import  sys
nums = []
for num in range(1, 10 ** 6+1, 2):
    nums.append(num ** 2)
print(type(nums), sys.getsizeof(nums))