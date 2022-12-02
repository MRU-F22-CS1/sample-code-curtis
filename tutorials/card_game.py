import random
from card import Card
from hand import Hand

def draw_card() -> Card:
    """
    Create and return a Card instance with random value and suit
    Valid values range from 1-13
    Valid suits are ♠♥♦♣
    """
    value = random.randint(1, 13)
    suit = random.choice('♠♥♦♣')
    return Card(value, suit)

def main() -> None:
    my_hand = Hand()
    for _ in range(6):
        rando_card = draw_card()
        my_hand.add_card(rando_card)

    print(f"Total value of cards: {my_hand.total()}")
    print(my_hand)
main()