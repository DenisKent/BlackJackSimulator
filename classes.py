import csv

class Card(object):
    
    def __init__(self, name, hard, soft, type, suit):
        self.name = name
        self.hard = hard
        self.soft = soft
        self.type = type
        self.suit = suit

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
my_ace_diamonds = Card( 'Ace of Diamonds', 11, 1, 'ace', 'diamonds')
my_two_diamonds = Card( 'Two of Diamonds', 2, 2, 'two', 'diamonds')
my_three_diamonds = Card( 'Three of Diamonds', 3, 3, 'three', 'diamonds')
my_four_diamonds = Card( 'Four of Diamonds', 4, 4, 'four', 'diamonds')
my_five_diamonds = Card( 'Five of Diamonds', 5, 5, 'five', 'diamonds')
my_six_diamonds = Card( 'Six of Diamonds', 6, 6, 'six', 'diamonds')
my_seven_diamonds = Card( 'Seven of Diamonds', 7, 7, 'seven', 'diamonds')
my_eight_diamonds = Card( 'Eight of Diamonds', 8, 8, 'eight', 'diamonds')
my_nine_diamonds = Card( 'Nine of Diamonds', 9, 9, 'nine', 'diamonds')
my_ten_diamonds = Card( 'Ten of Diamonds', 10, 10, 'ten', 'diamonds')
my_jack_diamonds = Card( 'Jack of Diamonds', 10, 10, 'jack', 'diamonds')
my_queen_diamonds = Card( 'Queen of Diamonds', 10, 10, 'queen', 'diamonds')
my_king_diamonds = Card( 'King of Diamonds', 10, 10, 'king', 'diamonds')
my_ace_spades = Card( 'Ace of Spades', 11, 1, 'ace', 'spades')
my_two_spades = Card( 'Two of Spades', 2, 2, 'two', 'spades')
my_three_spades = Card( 'Three of Spades', 3, 3, 'three', 'spades')
my_four_spades = Card( 'Four of Spades', 4, 4, 'four', 'spades')
my_five_spades = Card( 'Five of Spades', 5, 5, 'five', 'spades')
my_six_spades = Card( 'Six of Spades', 6, 6, 'six', 'spades')
my_seven_spades = Card( 'Seven of Spades', 7, 7, 'seven', 'spades')
my_eight_spades = Card( 'Eight of Spades', 8, 8, 'eight', 'spades')
my_nine_spades = Card( 'Nine of Spades', 9, 9, 'nine', 'spades')
my_ten_spades = Card( 'Ten of Spades', 10, 10, 'ten', 'spades')
my_jack_spades = Card( 'Jack of Spades', 10, 10, 'jack', 'spades')
my_queen_spades = Card( 'Queen of Spades', 10, 10, 'queen', 'spades')
my_king_spades = Card( 'King of Spades', 10, 10, 'king', 'spades')
my_ace_clubs = Card( 'Ace of Clubs', 11, 1, 'ace', 'clubs')
my_two_clubs = Card( 'Two of Clubs', 2, 2, 'two', 'clubs')
my_three_clubs = Card( 'Three of Clubs', 3, 3, 'three', 'clubs')
my_four_clubs = Card( 'Four of Clubs', 4, 4, 'four', 'clubs')
my_five_clubs = Card( 'Five of Clubs', 5, 5, 'five', 'clubs')
my_six_clubs = Card( 'Six of Clubs', 6, 6, 'six', 'clubs')
my_seven_clubs = Card( 'Seven of Clubs', 7, 7, 'seven', 'clubs')
my_eight_clubs = Card( 'Eight of Clubs', 8, 8, 'eight', 'clubs')
my_nine_clubs = Card( 'Nine of Clubs', 9, 9, 'nine', 'clubs')
my_ten_clubs = Card( 'Ten of Clubs', 10, 10, 'ten', 'clubs')
my_jack_clubs = Card( 'Jack of Clubs', 10, 10, 'jack', 'clubs')
my_queen_clubs = Card( 'Queen of Clubs', 10, 10, 'queen', 'clubs')
my_king_clubs = Card( 'King of Clubs', 10, 10, 'king', 'clubs')

my_full_single_deck = [my_ace_hearts, my_two_hearts, my_three_hearts, my_four_hearts, my_five_hearts, my_six_hearts, my_seven_hearts, my_eight_hearts, my_nine_hearts, my_ten_hearts, my_jack_hearts, my_queen_hearts, my_king_hearts, my_ace_diamonds, my_two_diamonds, my_three_diamonds, my_four_diamonds, my_five_diamonds, my_six_diamonds, my_seven_diamonds, my_eight_diamonds, my_nine_diamonds, my_ten_diamonds, my_jack_diamonds, my_queen_diamonds, my_king_diamonds, my_ace_spades, my_two_spades, my_three_spades, my_four_spades, my_five_spades, my_six_spades, my_seven_spades, my_eight_spades, my_nine_spades, my_ten_spades, my_jack_spades, my_queen_spades, my_king_spades, my_ace_clubs, my_two_clubs, my_three_clubs, my_four_clubs, my_five_clubs, my_six_clubs, my_seven_clubs, my_eight_clubs, my_nine_clubs, my_ten_clubs, my_jack_clubs, my_queen_clubs, my_king_clubs]

# ----------------------------------------------------------------------

class Player(object):

#in the future could add bet and cashstack to this too
    def __init__(self, dealer, hands, losses, wins, bjwins, draws, dbwins, dblosses, handsplayed,cashstack):
        self.dealer = dealer
        self.hands = hands
        self.losses = losses
        self.wins = wins
        self.bjwins = bjwins
        self.draws = draws
        self.dbwins = dbwins
        self.dblosses = dblosses
        self.handsplayed = handsplayed
        self.cashstack = cashstack

#Creates players
def create_players(num_of_players):
    player_dealer_list = [Player(False,[],0,0,0,0,0,0,0,100.0) for i in range (num_of_players + 1)]
    player_dealer_list[0].dealer = True
    
    return player_dealer_list

# ----------------------------------------------------------------------

class Hand(object):
    def __init__(self, cards, bet, double):
        self.cards = cards
        self.bet = bet
        self.double = double

# ----------------------------------------------------------------------

class Testhand(object):
    def __init__(self, plhand, dlhand, plcardcount, dlcardcount, double, split, losses, wins, bjwins, draws, dbwins, dblosses, handsplayed):
        self.plhand = plhand
        self.dlhand = dlhand
        self.plcardcount = plcardcount
        self.dlcardcount = dlcardcount
        self.double = double
        self.split = split
        self.losses = losses
        self.wins = wins
        self.bjwins = bjwins
        self.draws = draws
        self.dbwins = dbwins
        self.dblosses = dblosses
        self.handsplayed = handsplayed

# ----------------------------------------------------------------------

#Imports basic strategy and organises it in an array. Imports the dealer titles for other imports
basic_strategy_file = open("/Users/deniskent6/Desktop/BJ/csv_files/strategy_excel.csv","rU")
basic_strategy = csv.reader(basic_strategy_file)

row_counter = 0
row_player_titles = []
basic_strategy_array = []
for row in basic_strategy:
    #stores each row of the excel, also records the row and column titles
    basic_strategy_array.append(row)
    row_player_titles.append(row[0])
    if row_counter == 0:
        column_dealer_titles = row
    row_counter += 1

basic_strategy_file.close()

# ----------------------------------------------------------------------

#Imports soft basic strategy and organises it in an array
soft_basic_strategy_file = open("/Users/deniskent6/Desktop/BJ/csv_files/soft_strategy_excel.csv","rU")
soft_basic_strategy = csv.reader(soft_basic_strategy_file)

row_player_titles = []
soft_basic_strategy_array = []
for row in soft_basic_strategy:
    #stores each row of the excel, also records the row and column titles
    soft_basic_strategy_array.append(row)
    row_player_titles.append(row[0])

soft_basic_strategy_file.close()

# ----------------------------------------------------------------------

#Imports split basic strategy and organises it in an array
split_basic_strategy_file = open("/Users/deniskent6/Desktop/BJ/csv_files/split_strategy_excel.csv","rU")
split_basic_strategy = csv.reader(split_basic_strategy_file)

row_split_player_titles = []
split_basic_strategy_array = []
for row in split_basic_strategy:
    #stores each row of the excel, also records the row and column titles
    split_basic_strategy_array.append(row)
    row_split_player_titles.append(row[0])

split_basic_strategy_file.close()

# ----------------------------------------------------------------------

#Imports double basic strategy and organises it in an array
double_basic_strategy_file = open("/Users/deniskent6/Desktop/BJ/csv_files/double_strategy_excel.csv","rU")
double_basic_strategy = csv.reader(double_basic_strategy_file)

row_double_player_titles = []
double_basic_strategy_array = []
for row in double_basic_strategy:
    #stores each row of the excel, also records the row and column titles
    double_basic_strategy_array.append(row)
    row_double_player_titles.append(row[0])

double_basic_strategy_file.close()

# ----------------------------------------------------------------------

#Imports soft double basic strategy and organises it in an array
soft_double_basic_strategy_file = open("/Users/deniskent6/Desktop/BJ/csv_files/soft_double_strategy_excel.csv","rU")
soft_double_basic_strategy = csv.reader(soft_double_basic_strategy_file)

row_soft_double_player_titles = []
soft_double_basic_strategy_array = []
for row in soft_double_basic_strategy:
    #stores each row of the excel, also records the row and column titles
    soft_double_basic_strategy_array.append(row)
    row_soft_double_player_titles.append(row[0])

soft_double_basic_strategy_file.close()