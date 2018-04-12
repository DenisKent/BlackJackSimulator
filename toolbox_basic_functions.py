from classes import Card, Player, Hand

#Function which counts the value of a players hand, hard or soft
def hand_value(hand,hard_or_soft):
    hand_counter = 0
    for card in hand:
        if hard_or_soft == "hard":
            hand_counter += card.hard
        elif hard_or_soft == "soft":
            hand_counter += card.soft
        else:
            hand_counter = "Should it count hard or soft" 
    return hand_counter

#--------------------------------------
#Function which works out whether a hand is a blackjack

def is_bj(hand):
    if hand_value(hand,"hard") == 21 and len(hand) == 2:
        return True
    else:
        return False
        
#--------------------------------------       
# Function which returns the best possible score from a hand

def best_score(hand):
    ace_counter = 0
    score_counter = 0
    
    for card in hand:
        if card.type == "ace":
            ace_counter += 1
        else:
            score_counter += card.hard
    soft_hand = score_counter + ace_counter
    hard_hand = score_counter + ace_counter + 10
    if hard_hand > 21:
        return soft_hand
    else:
        return hard_hand

#--------------------------------------    
    
#Function which returns True if player hand has an Ace
def has_ace(hand):
    if hand_value(hand,"hard") != hand_value(hand,"soft"):
        return True
    else:
        return False
 
    