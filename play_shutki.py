
from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input("сколка шутек вы хотите: "))
o = []
def get_jokes(n):
    while n != 0:

        mess = choice(nouns)
        mess_2 = choice(adverbs)
        mess_3 = choice(adjectives)
        print([mess + " " + mess_2 + " " + mess_3])
        n -=1




get_jokes(n)