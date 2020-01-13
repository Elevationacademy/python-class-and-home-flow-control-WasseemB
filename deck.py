import random


class Card:
    def __init__(self, card_type, card_number):
        self.card_number = card_number
        self.card_type = card_type

    def __str__(self):
        return f"{self.card_number}, {self.card_type}"


class Deck:

    def __init__(self):
        self.card_list = []
        [self.card_list.append(Card("Red", i)) for i in range(1, 11)]
        [self.card_list.append(Card("Blue", i)) for i in range(1, 11)]
        [self.card_list.append(Card("Green", i)) for i in range(1, 11)]
        [self.card_list.append(Card("Yellow", i)) for i in range(1, 11)]
        self.max = len(self.card_list)

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.card_list:
            raise StopIteration
        self.num += 1
        return self.card_list.pop()

    def __bool__(self):
        return len(self.card_list) > 0

    def shuffle(self):
        return random.shuffle(self.card_list)

    def deal(self):
        self.card_list.pop()


deck = Deck()
deck.shuffle()
count = 0
if deck:
    print("The deck is not empty")
else:
    print("The deck is empty")
for card in deck:
    count += 1
    print(f"{count}, {card}")

print("------")
if deck:
    print("The deck is not empty")
else:
    print("The deck is empty")
