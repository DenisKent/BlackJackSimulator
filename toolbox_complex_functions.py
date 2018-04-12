from classes import Card, Player, Hand 
from classes import basic_strategy_array, soft_basic_strategy_array, double_basic_strategy_array, soft_double_basic_strategy_array, column_dealer_titles, row_player_titles
from classes import split_basic_strategy_array, row_split_player_titles
from basic_toolbox import hand_value, is_bj, best_score, has_ace

# Function which clears player hands and deals to cards to each player
def deal_hands(output_deck, player_list):
    for player in player_list:
        player.hands = [Hand([],0,False)]
    for x in range(2):
        for player in player_list:
            if player.dealer == False:
                for hand in player.hands:
                    hand.cards.append(output_deck.pop(0))
        player_list[0].hands[0].cards.append(output_deck.pop(0))

    return output_deck, player_list

#--------------------------------------    

#Function which determines if the player should hit against the dealer
def basic_strategy(dealer, hand, type):
    dealer_value = str(dealer.hands[0].cards[1].hard)
    if type == "hard":
        player_value = str(hand_value(hand,"hard"))
        basic_strategy_row = basic_strategy_array[row_player_titles.index(player_value)]
    elif type == "soft":
        player_value = str(hand_value(hand,"soft"))
        basic_strategy_row = soft_basic_strategy_array[row_player_titles.index(player_value)]
    elif type == "split":
        player_value = str(hand[0].type)
        basic_strategy_row = split_basic_strategy_array[row_split_player_titles.index(player_value)]
    elif type == "double":
        player_value = str(hand_value(hand,"hard"))
        basic_strategy_row = double_basic_strategy_array[row_player_titles.index(player_value)]
    elif type == "soft_double":
        player_value = str(hand_value(hand,"soft"))
        basic_strategy_row = soft_double_basic_strategy_array[row_player_titles.index(player_value)]   
    
    return basic_strategy_row[column_dealer_titles.index(dealer_value)]
# dealer_value = str(9)
# player_value = str(8)
# basic_strategy_row = soft_basic_strategy_array[row_player_titles.index(player_value)]
# print basic_strategy_row[column_dealer_titles.index(dealer_value)]

#--------------------------------------

#Function which plays to the end of the turn for every player using basic strategy
def play_hand_bs(output_deck, player_list):

    #Non-dealer players first
    for player in player_list:
        if player.dealer == False:
            
            #Checks for any splits, and does the split
            check_again = True
            while check_again:
                check_again = False
                for hand in player.hands:
                    if hand.cards[0].type == hand.cards[1].type and len(hand.cards) == 2:
                        if basic_strategy(player_list[0],hand.cards,"split") == "split":
                            player.hands.append(Hand([hand.cards.pop(1),output_deck.pop(0)],hand.bet,hand.double))
                            hand.cards.append(output_deck.pop(0))
                            check_again = True

            for hand in player.hands:
                while hand_value(hand.cards,"soft") < 22:
                    #Checks for doubles, only works if hand has 2 cards
                    #Checks for soft doubles
                    #Checks for doubles with no ace
                    if  (len(hand.cards) == 2) \
                        and ((has_ace(hand.cards) and basic_strategy(player_list[0],hand.cards,"soft_double") == "double") \
                        or basic_strategy(player_list[0],hand.cards,"double") == "double"):
                            hand.cards.append(output_deck.pop(0))
                            hand.double = True
                            break

                    #Checks for ace
                    elif has_ace(hand.cards):
                        if basic_strategy(player_list[0], hand.cards,"soft") == "hit":
                            hand.cards.append(output_deck.pop(0))
                        else:
                            break                         
                    #Normal play, checks if player hits
                    else:
                        if basic_strategy(player_list[0], hand.cards,"hard") == "hit":
                            hand.cards.append(output_deck.pop(0))
                        else:
                            break

    #Dealer plays, only ever has one hand
    while (hand_value(player_list[0].hands[0].cards, "soft") < 17):
        hard_score = hand_value(player_list[0].hands[0].cards, "hard")
        if (hard_score > 16 and hard_score < 22):
            break
        player_list[0].hands[0].cards.append(output_deck.pop(0))

    return output_deck, player_list


#--------------------------------------

#Function which works out if a player won or lost

def calculate_scores(player_list):

    dealer_cards = player_list[0].hands[0].cards
    for player in player_list:
        if player.dealer == False:
            for hand in player.hands:
                player.handsplayed += 1
                hand_result = "NA"
                dealer_score = best_score(dealer_cards)
                player_score = best_score(hand.cards)

                #Player goes bust or Player loses to dealer
                if hand_value(hand.cards,"soft") > 21 \
                   or (dealer_score < 22 and dealer_score > player_score):
                    hand_result = "loss"

                #Player gets blackjack
                elif is_bj(hand.cards) and not is_bj(dealer_cards):
                    player.bjwins += 1
                    player.cashstack += 1.5
                    hand_result = "BJ"

                #Player wins due to dealer bust or Player wins due to winning score
                elif (dealer_score > 21 and player_score < 22) \
                    or (player_score <22 and player_score > dealer_score):
                    hand_result = "win"
                
                #Player draws
                elif best_score(dealer_cards) == best_score(hand.cards):
                    player.draws += 1
                    hand_result = "draw"
                
                #Scores for a double
                if hand.double == True:
                    if hand_result == "win":
                        player.dbwins += 1
                        player.cashstack += 2
                    if hand_result == "loss":
                        player.dblosses += 1
                        player.cashstack -= 2
                if hand.double == False:
                    if hand_result == "win":
                        player.wins += 1
                        player.cashstack += 1
                    if hand_result == "loss":
                        player.losses += 1
                        player.cashstack -= 1

                if hand_result == "NA":
                    print "win/loss assignment error"

    return player_list


