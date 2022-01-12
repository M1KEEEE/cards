""" игра в пьяницу

	+ создать перемешанную колоду из 36 карт:
		4 масти, 9 значений
		коллекция из карт
		карта: масть + значение

	+ раздать карты:
		карты игрока - 1/2 от колоды
		карты игрока - 1/2 от колоды

	+ начать раунд:
		взять верхнюю карту	игрока и положить на стол
		взять верхнюю карту	соперника и положить на стол

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



deck = make_deck(suits)
user_deck = split_deck(deck)[0]
computer_deck = split_deck(deck)[1]

"""
начало игры
"""
desk = []
desk.append(user_deck.pop())
desk.append(computer_deck.pop())

print("игрок выбросил", desk[0]["значение"])
print("компьютер выбросил", desk[1]["значение"])

if desk[0]["значение"] > desk[1]["значение"]:
	print("игрок победил")
elif desk[0]["значение"] < desk[1]["значение"]:
	print("компьютер победил")
else:
	print("спор")