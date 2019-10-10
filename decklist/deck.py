class Card:
    def __init__(self, name, num, owned):
        self.name = name
        self.num = num
        self.owned = owned


class Deck:
    def __init__(self, name=None, cards=None):
        self.name = name
        self.cards = {}
        for card in cards:
            self.add_card(card)

    def add_card(self, card):
        if name in self.cards:
            self.cards[card.name].num += card.num
            self.cards[card.name].owned += card.owned
        else:
            self.cards[card.name] = card
