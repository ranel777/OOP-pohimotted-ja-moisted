class Card:
    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['hearts', 'diamonds', 'clubs', 'spades']
    
    def __init__(self, value: str, suit: str):
        if value not in Card.valid_values:
            raise ValueError(f"Invalid card value: {value}")
        if suit not in Card.valid_suits:
            raise ValueError(f"Invalid suit: {suit}")
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Hand:
    def __init__(self):
        self.cards = []
    
    def can_add_card(self, card: Card) -> bool:
        if len(self.cards) >= 5:
            return False
        if any(c.value == card.value and c.suit == card.suit for c in self.cards):
            return False
        return True

    def add_card(self, card: Card):
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card) -> bool:
        return card in self.cards

    def remove_card(self, card: Card):
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        return self.cards
    
    def is_straight(self):
        if len(self.cards) != 5:
            return False
        sorted_values = sorted([self.card_value(card) for card in self.cards])
        return sorted_values == list(range(sorted_values[0], sorted_values[0] + 5))

    def card_value(self, card: Card):
        """ Abimeetod kaardi väärtuse muutmiseks numbriks """
        value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return value_map[card.value]

    def is_flush(self):
        return len(set(card.suit for card in self.cards)) == 1

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        value_counts = {card.value: sum(1 for c in self.cards if c.value == card.value) for card in self.cards}
        return sorted(value_counts.values()) == [2, 3]

    def is_four_of_a_kind(self):
        value_counts = {card.value: sum(1 for c in self.cards if c.value == card.value) for card in self.cards}
        return 4 in value_counts.values()

    def is_three_of_a_kind(self):
        value_counts = {card.value: sum(1 for c in self.cards if c.value == card.value) for card in self.cards}
        return 3 in value_counts.values()

    def is_pair(self):
        value_counts = {card.value: sum(1 for c in self.cards if c.value == card.value) for card in self.cards}
        return 2 in value_counts.values()

    def get_hand_type(self):
        if len(self.cards) < 5:
            return None
        if self.is_straight_flush():
            return "straight flush"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_full_house():
            return "full house"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"
        return "high card"

    def __repr__(self):
        hand_type = self.get_hand_type()
        if hand_type:
            return f"I got a {hand_type} with cards: {', '.join(map(str, self.cards))}"
        else:
            return f"I'm holding {', '.join(map(str, self.cards))}"


