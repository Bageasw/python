my_list = ["в", "5", "часов", "17", "минут", "температура", "воздуха", "была", "+5", "градусов"]
my_list2 = []

"""my_list.pop(1)
my_list.pop(-2),
my_list.insert(-1, "+05")
my_list.insert(1, "05")

my_list2 = my_list.copy()
my_list2.pop(0)
my_list2.insert(0, "05")
my_list2.pop(1)
my_list2.insert(1, "+05")
"""
my_list[1] = "05"
my_list[-2] = "+05"
my_list.insert(-1, '"')
my_list.insert(-3, '"')
my_list.insert(4, '"')
my_list.insert(3, '"')
my_list.insert(2, '"')
my_list.insert(1, '"')
print(my_list)
print(" ".join(my_list))