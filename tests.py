from classes import Card, Player, Hand, my_full_single_deck, Testhand
from basic_toolbox import hand_value, is_bj, best_score, has_ace
from toolbox import deal_hands, play_hand_bs, calculate_scores, basic_strategy

my_ace_hearts = Card( 'Ace of Hearts', 11, 1, 'ace', 'hearts')
my_two_hearts = Card( 'Two of Hearts', 2, 2, 'two', 'hearts')
my_three_hearts = Card( 'Three of Hearts', 3, 3, 'three', 'hearts')
my_four_hearts = Card( 'Four of Hearts', 4, 4, 'four', 'hearts')
my_five_hearts = Card( 'Five of Hearts', 5, 5, 'five', 'hearts')
my_six_hearts = Card( 'Six of Hearts', 6, 6, 'six', 'hearts')
my_seven_hearts = Card( 'Seven of Hearts', 7, 7, 'seven', 'hearts')
my_eight_hearts = Card( 'Eight of Hearts', 8, 8, 'eight', 'hearts')
my_nine_hearts = Card( 'Nine of Hearts', 9, 9, 'nine', 'hearts')
my_ten_hearts = Card( 'Ten of Hearts', 10, 10, 'ten', 'hearts')
my_jack_hearts = Card( 'Jack of Hearts', 10, 10, 'jack', 'hearts')
my_queen_hearts = Card( 'Queen of Hearts', 10, 10, 'queen', 'hearts')
my_king_hearts = Card( 'King of Hearts', 10, 10, 'king', 'hearts')

#Tests, plhand, dlhand, plcardcount, dlcardcount, double, split, losses, wins, bjwins, draws, dbwins, dblosses, handsplayed
Test1 = Testhand([my_six_hearts,my_jack_hearts],[my_ten_hearts,my_six_hearts],2,3,0,0,0,1,0,0,0,0,1) #16 vs 6
Test2 = Testhand([my_six_hearts,my_jack_hearts],[my_nine_hearts,my_seven_hearts],3,3,0,0,1,0,0,0,0,0,1) #16 vs 7
Test3 = Testhand([my_two_hearts,my_jack_hearts],[my_two_hearts,my_three_hearts],3,4,0,0,1,0,0,0,0,0,1) #12 vs 3
Test4 = Testhand([my_two_hearts,my_jack_hearts],[my_two_hearts,my_four_hearts],2,4,0,0,0,1,0,0,0,0,1) #12 vs 4
Test5 = Testhand([my_two_hearts,my_jack_hearts],[my_two_hearts,my_six_hearts],2,3,0,0,1,0,0,0,0,0,1) #12 vs 6
Test6 = Testhand([my_two_hearts,my_jack_hearts],[my_ten_hearts,my_seven_hearts],3,2,0,0,1,0,0,0,0,0,1) #12 vs 7
Test7 = Testhand([my_two_hearts,my_nine_hearts],[my_two_hearts,my_king_hearts],3,3,1,0,0,0,0,0,1,0,1) #11 vs 10
Test8 = Testhand([my_two_hearts,my_nine_hearts],[my_two_hearts,my_ace_hearts],3,4,0,0,0,1,0,0,0,0,1) #11 vs A
Test9 = Testhand([my_two_hearts,my_seven_hearts],[my_two_hearts,my_three_hearts],3,4,1,0,0,0,0,0,1,0,1) #9 vs 3
Test10 = Testhand([my_ace_hearts,my_seven_hearts],[my_two_hearts,my_two_hearts],2,4,0,0,0,1,0,0,0,0,1) #A7 vs 2
Test11 = Testhand([my_ace_hearts,my_seven_hearts],[my_two_hearts,my_three_hearts],3,4,1,0,0,0,0,0,1,0,1) #A7 vs 3
Test12 = Testhand([my_ace_hearts,my_two_hearts],[my_two_hearts,my_five_hearts],3,3,1,0,0,0,0,0,0,1,1) #A2 vs 5
Test13 = Testhand([my_ace_hearts,my_ace_hearts],[my_two_hearts,my_five_hearts],2,3,0,1,0,0,2,0,0,0,2) #AA vs 5
Test14 = Testhand([my_nine_hearts,my_nine_hearts],[my_two_hearts,my_five_hearts],2,3,0,1,0,2,0,0,0,0,2) #99 vs 5
Test15 = Testhand([my_five_hearts,my_five_hearts],[my_two_hearts,my_five_hearts],3,3,1,0,0,0,0,0,1,0,1) #55 vs 5
Test16 = Testhand([my_four_hearts,my_four_hearts],[my_two_hearts,my_five_hearts],2,3,0,1,2,0,0,0,0,0,2) #44 vs 5
Test17 = Testhand([my_four_hearts,my_four_hearts],[my_two_hearts,my_four_hearts],3,4,0,0,0,1,0,0,0,0,1) #44 vs 4


Test_hands = [Test1,Test2,Test3,Test4,Test5,Test6,Test7,Test8,Test9,Test10,Test11,Test12,Test13,Test14,Test15,Test16,Test17]
#Loops through test hands
testcounter = 0
for testhand in Test_hands:
    testcounter +=1
    #Always draws a ten for all players - The test answers are based on this
    output_shoe = [my_ten_hearts]*100
    test_player_hand = Hand(testhand.plhand[0:2],0,False)
    test_dealer_hand = Hand(testhand.dlhand[0:2],0,False)
    test_dealer = Player(True,[test_dealer_hand],0,0,0,0,0,0,0)
    test_player = Player(False,[test_player_hand],0,0,0,0,0,0,0)

    #Tests to see if player and dealer choices are correct
    output_shoe, player_list = play_hand_bs(output_shoe, [test_dealer,test_player])
    
    if len(player_list[0].hands[0].cards) != testhand.dlcardcount:
        print "Test %i dealer draws cards wrong" %(testcounter)

    if len(player_list[1].hands[0].cards) != testhand.plcardcount:
        print "Test %i player draws cards wrong" %(testcounter)

    if player_list[1].hands[0].double != testhand.double:
        print "Test %i doubles wrong" %(testcounter)

    if len(player_list[1].hands) != (testhand.split +1):
        print "Test %i splits wrong" %(testcounter)

    player_list = calculate_scores(player_list)
    
    #Tests score calculations
    if player_list[1].wins != testhand.wins:
        print "Test %i win calculation wrong" %(testcounter)
    if player_list[1].losses != testhand.losses:
        print "Test %i losses calculation wrong" %(testcounter)
    if player_list[1].bjwins != testhand.bjwins:
        print "Test %i bjwin calculation wrong" %(testcounter)
    if player_list[1].draws != testhand.draws:
        print "Test %i draw calculation wrong" %(testcounter)
    if player_list[1].dbwins != testhand.dbwins:
        print "Test %i dbwin calculation wrong" %(testcounter)
    if player_list[1].dblosses != testhand.dblosses:
        print "Test %i dblosses calculation wrong" %(testcounter) 
    if player_list[1].handsplayed != testhand.handsplayed:
        print "Test %i hands played calculation wrong" %(testcounter)   

print "Tests carried out"
        
#         print "\nDealer cards:"
#         for card in player_list[0].hands[0].cards:
#             print card.name
#         print "\nPlayer cards:"
#         for card in player_list[1].hands[0].cards:
#             print card.name
#             print "\n"
