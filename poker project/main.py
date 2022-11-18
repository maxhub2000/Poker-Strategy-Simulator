import random
import operator

from combinations_and_decision import *


# TO DO LIST COMPREHENSION IN THE CODE LATER

def cards_values_for_class(self):
        card_val = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        for i in range(2, 11):
            card_val[i] = i
        return card_val

class cards:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.number_value= cards_values_for_class(self)[self.rank]

    def number_value_maker(self):
        self.number_value += cards_values_for_class(self)[self.rank]

    def __repr__(self):
        return str(self.rank) + " of " + str(self.suit)


    # 13.02.2022 update:
    # comparison function between 2 cards instances
    def __eq__(self, other):
        if (isinstance(other, cards)):
            return self.suit == other.suit and self.rank == other.rank
        return False


    '''def cards_values(self):
        card_val = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        for i in range(2, 11):
            card_val[i] = i
        return card_val'''


def cards_values():
        # initiate the dict with the numbered cards
        card_val = { i:i for i in range(2, 11) }
        # add the non-numbered cards to the dict 
        card_val.update({"Jack": 11, "Queen": 12, "King": 13, "Ace": 14})
        return card_val


def cards_values_reversed():
    # Create the dict by using reversing keys and values from cards_values dict
    card_val_reversed = { cards_values()[i]:i for i in cards_values() }
    # In case Ace is used as 1 in straight    
    card_val_reversed.update({1: "Ace"}) 
    return card_val_reversed







class start_hand:
    def __init__(self,hand):
        self.hand=hand
    def __repr__(self):
        return str(self.hand[0])+ "," + str(self.hand[1])

king_of_diamonds =  cards("diamond","King")
king_of_spades= cards("spades","King")
best_hand_eu = start_hand([king_of_spades,king_of_diamonds])
print (best_hand_eu)




#print(straight_flush_and_royal_flush(card31, card32, card33, card34, card35, card36, card37))
#print(same_rank_combinations([card_1,card_2,card_3,card_4,card_5,card_6,card_7]))



card_1=cards("spades","King")
card_2=cards("spades","Ace")
card_3=cards("clubs",7)
card_4=cards("clubs",9)
card_5=cards("spades","Queen")
card_6=cards("spades",5)
card_7=cards("spades",10)

card11=cards("spades","Queen")
card12=cards("clubs",9)
card13=cards("spades",10)
card14=cards("hearts","Queen")
card15=cards("spades","Ace")
card16=cards("spades","King")
card17=cards("spades",5)

card21=cards("diamonds",3)
card22=cards("diamonds",8)
card23=cards("diamonds",5)
card24=cards("spades",5)
card25=cards("clubs","Queen")
card26=cards("diamonds","King")
card27=cards("diamonds",8)

card31=cards("spades",8)
card32=cards("spades",9)
card33=cards("spades",10)
card34=cards("diamonds","Jack")
card35=cards("diamonds","Queen")
card36=cards("spades",2)
card37=cards("spades","Ace")

lst_0 = [card_1,card_2,card_3,card_4,card_5,card_6,card_7]
lst_1 = [card11,card12,card13,card14,card15,card16,card17]
lst_2 = [card21,card22,card23,card24,card25,card26,card27]
lst_3 = [card31,card32,card33,card34,card35,card36,card37]




######## starting at 13.02.22


def single_card_generator():
    suit = random.choice(["diamonds","spades","clubs","hearts"])
    possible_ranks = list(range(2,11))
    possible_ranks.extend(["Jack","Queen","King","Ace"])
    rank = random.choice(possible_ranks)
    return cards(suit,rank)


print("single_card_generator: ", single_card_generator())


def multiple_card_generator(n, used_cards = []):
    # get n random generated cards without doubles.
    # the used_cards argument is a list of cards already used in a current poker round, and so if we wanted
    # to generate cards for rounds we should generate cards that were not used already in the current round.
    generated_cards = []
    while len(generated_cards) < n:
        generated_card = single_card_generator()
        if (generated_card not in generated_cards) and (generated_card not in used_cards):
            generated_cards.append(generated_card)
    return generated_cards

print("multiple_card_generator: ",multiple_card_generator(7))


######## starting at 13.02.22


class player:
    def __init__(self, name):
        self.name = name
        self.start_hand = []
        self.common_cards = []
        self.final_hand = []

    # generate starting hand for each round
    def get_current_starting_hand(self, cards):
        self.start_hand.extend(cards)

    # adds generated common cards to the player's common cards
    def add_cards_to_common(self, cards):
        self.common_cards.extend(cards)

    # creates final hand for non-folded players after 5 common cards has been revealed
    def create_final_hand(self):
        if len(self.start_hand) + len(self.common_cards) ==7: # making sure it's possible to create the final hand
            self.final_hand = self.start_hand + self.common_cards


maxim = player("maxim")
dude = player("dude")
bro = player("bro")


players = [maxim, dude, bro]
non_folded_players = [maxim, dude, bro] # list of players that didn't fold yet. At the start of each round all players will be in it
common_cards = [] # general (not specific to a player) list of common cards that were opened. In poker also called: "community cards"

used_cards_for_current_round = [] # list of cards that were already used for this round, so we know we can't use them anymore.


def generate_starting_hand_for_all_players(players):
    # generate starting hands and add them each of the players
    for player in players:
        cards = multiple_card_generator(2, used_cards_for_current_round) # generate 2 cards for starting hand
        used_cards_for_current_round.extend(cards) # update list of cards that were already used for this round
        player.get_current_starting_hand(cards) # add the starting hand to the player object


def generate_common_cards(n, non_folded_players):
    # adds the generated cards to the general common_cards list and also
    # to the common_cards list of each of the non folded players
    cards = multiple_card_generator(n, used_cards_for_current_round) # generate n cards 
    common_cards.extend(cards) # update list of general common cards 
    used_cards_for_current_round.extend(cards) # update list of cards that were already used for this round
    for player in non_folded_players:
        # update list of common cards for each of the non-folded players
        player.add_cards_to_common(cards)

def flop(non_folded_players):
    # generate 3 cards for flop
    generate_common_cards(3, non_folded_players)

def turn(non_folded_players):
    # generate 1 card for turn
    generate_common_cards(1, non_folded_players)

def river(non_folded_players):
    # generate 1 card for river
    generate_common_cards(1, non_folded_players)

#add_card_to_common(non_folded_players)



generate_starting_hand_for_all_players(players)
print("\n")
for player in players:
    print(player.name,"starting hand: " ,player.start_hand)


flop(non_folded_players)
turn(non_folded_players)
river(non_folded_players)
print("common_cards: ",common_cards)
print("used_cards_for_current_round: ",used_cards_for_current_round)



# def determine_winner_for_current_round(non_folded_players):
#     winner = non_folded_players[0]
#     if len(non_folded_players) ==1:
#         #winner = non_folded_players[0]
#         return winner
#     else:
#         for player in non_folded_players[1:]:
#             if 






















