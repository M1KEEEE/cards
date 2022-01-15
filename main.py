""" игра в пьяницу

    + создать перемешанную колоду из 36 карт:
        4 масти, 9 значений
        коллекция из карт
        карта: масть + значение

    + раздать карты:
        карты игрока - 1/2 от колоды
        карты игрока - 1/2 от колоды

    + начать раунд:
        взять верхнюю карту    игрока и положить на стол
        взять верхнюю карту    соперника и положить на стол

    сравниваем карты на столе:
        вариант значение карты игрока > соперника
            карты игрока += стол (снизу карт)
        вариант значение карты игрока < соперника
            карты соперника += стол (снизу карт)
        вариант значение карты игрока == соперника
            выбросить еще пару и сравнить опять

    победа и проигрыш:
        кончились карты
        нечем ответить в споре
"""
import random

suits = ("червей", "пик","крестей", "бубен")


def make_deck(suits):
    deck = []
    for suit in suits:
        for value in range(6, 15):
            card = {}
            card["масть"] = suit
            card["значение"] = value
            deck.append(card)
    random.shuffle(deck)
    return deck


def split_deck(deck):
    user_deck = deck[:18]
    computer_deck = deck[18:]
    return user_deck, computer_deck

def new_game():
	make_deck()
	split_deck()
	table = []

	while table[0]["значение"] == table[1]["значение"]:
		new_round(user_deck, computer_deck, table)


deck = make_deck(suits)
user_deck = split_deck(deck)[0]
computer_deck = split_deck(deck)[1]

"""
начало игры
"""
table = []
table.append(user_deck.pop())
table.append(computer_deck.pop())

print("игрок выбросил", table[0]["значение"])
print("компьютер выбросил", table[1]["значение"])

if table[0]["значение"] > table[1]["значение"]:
    print("игрок победил")
elif table[0]["значение"] < table[1]["значение"]:
    print("компьютер победил")
else:
    print("спор")
    new_game()
