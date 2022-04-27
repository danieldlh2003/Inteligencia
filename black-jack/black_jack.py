"""Functions to help play and score a game of blackjack.
 
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.
 
    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    
    if card in "JQK":
        return 10
    
    if card == "A":
        return 1
    
    return int(card)
def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    if card_one_value > card_two_value:
        return card_one
    
    if card_one_value < card_two_value:
        return card_two
    
    return (card_one, card_two)
def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.
 
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.
 
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    if "A" in (card_one + card_two):
        if card_one == "A":
            card_one_value = 11
        if card_two == "A":
            card_two_value = 11
    
    if card_one_value + card_two_value + 11 > 21:
        return 1
    
    return 11
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    if "A" in (card_one + card_two):
        if card_one == "A":
            card_one_value = 11
        if card_two == "A":
            card_two_value = 11
    
    return card_one_value + card_two_value == 21
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    
    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    return card_one_value == card_two_value
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
 
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    return card_one_value + card_two_value in [9, 10, 11]
