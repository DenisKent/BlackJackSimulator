import random
from classes import Card, my_full_single_deck, Player, create_players, Hand
from toolbox import deal_hands, play_hand_bs, calculate_scores
from basic_toolbox import hand_value, best_score

#Creates the players, and the shoe

player_list = create_players(4)
for x in range(400):

    my_shoe = my_full_single_deck * 4
    random.shuffle(my_shoe)

    #Assigns the red card to be between 20% and 40% of the deck
    red_card_location = (len(my_shoe)*0.2) + (random.uniform(0,1)*len(my_shoe)*0.20)
    while len(my_shoe)> red_card_location:
        #Deals out a hand, then plays hand, then tots up scores
        output_shoe, player_list = deal_hands(my_shoe, player_list)
        output_shoe, player_list = play_hand_bs(output_shoe, player_list)
        player_list = calculate_scores(player_list)
        #tot out scores


for player in player_list:
    if player.dealer == False:
        no_of_hands = player.wins + player.bjwins + player.dbwins + player.losses + player.dblosses + player.draws
        #Weighted odds are wins/wins+losses, weighted by the amount won and lost, draws bring the odds closer to 50%
        weighted_odds = (player.wins + 1.5*player.bjwins + 2*player.dbwins + player.draws) \
            / float(player.wins + player.bjwins + 2*player.dbwins + 2*player.draws + player.losses + 2*player.dblosses)
        value_change_per_hand = ((player.wins + 1.5*player.bjwins + 2*player.dbwins) - (player.losses + 2*player.dblosses)) \
            / float(no_of_hands)
#         print "wins: %d" %(player.wins)
#         print "losses: %d" %(player.losses)
#         print "draws: %d" %(player.draws)
#         print "BJ wins: %d" %(player.bjwins)
#         print "double wins: %d" %(player.dbwins)
#         print "double losses: %d" %(player.dblosses)
        print "number of hands:         %d" %(no_of_hands)
        print player.handsplayed
        print "weighted odds =          " "{0:.2f}%".format(weighted_odds*100)
        print "value change per hand =  " "{0:.2f}%".format(value_change_per_hand*100)
        print "player cashtack = ", player.cashstack
