from card import Card

class Hand:
    """
    Represents a hand of playing cards.
    """
    def __init__(self) -> None:
        self.cards = []
    
    def add_card(self, a_card: Card) -> None:
        self.cards.append(a_card)
    
    def total(self) -> int:
        tot = 0
        for c in self.cards:
            tot += c.value
        
        return tot
    
    def __str__(self) -> str:
        card_str = ""
        for c in self.cards:
            card_str += f"{c} "
        
        return card_str