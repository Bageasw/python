dic = {"one": "один", "two": "два","three": "три", "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate():
    k = input("ввидите слово: ")
    print(dic.get(k))

num_translate(1)

