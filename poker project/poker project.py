

import random
import operator

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
        card_val = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        for i in range(2, 11):
            card_val[i] = i
        return card_val



def cards_values_reversed():
    card_val_reversed = {1: "Ace"} # in case Ace is used as 1 in straight
    for i in cards_values():
        card_val_reversed[cards_values()[i]] = i
    return card_val_reversed 



'''class start_hand:
    def __init__(self,hand):
        self.hand=hand
    def __repr__(self):
        return str(self.hand[0])+ "," + str(self.hand[1])

best_hand_eu = start_hand([king_of_spades,king_of_diamonds])'''
#print (best_hand_eu)




def return_higher_card(list_of_cards):
    #L = get_compared_cards(card_1, card_2, card_3, card_4, card_5, card_6, card_7)
    sorted_L = sorted(list_of_cards, key=operator.attrgetter("number_value"), reverse=True)
    return sorted_L[0]


def return_lower_card(list_of_cards):
    #L = get_compared_cards(card_1, card_2, card_3, card_4, card_5, card_6, card_7)
    sorted_L = sorted(list_of_cards, key=operator.attrgetter("number_value"),reverse=True)
    return sorted_L[-1]


#עוד לבדוק מה קורה בפונקציות lower,higher כי מה שעכשיו קורה לא אמור לקרות!!!



class start_hand:
    def __init__(self,hand):
        self.hand=hand
    def __repr__(self):
        return str(self.hand[0])+ "," + str(self.hand[1])

king_of_diamonds =  cards("diamond","King")
king_of_spades= cards("spades","King")
best_hand_eu = start_hand([king_of_spades,king_of_diamonds])
print (best_hand_eu)



def combinations_ranking():
    #lst=[card_1,card_2,card_3,card_4,card_5,card_6,card_7]
    D={"High Card":0, "Pair":1 , "two pair":2, "Three of a kind":3, "Straight":4, "Flush":5, "Full house":6,\
    "Four of a kind":7, "Straight flush":8 , "ROYAL FLUSH":9}
    return D
 




def high_card(list_of_cards):
    higher_card_rank = return_higher_card(list_of_cards)
    return ("High Card", higher_card_rank)


def same_rank_combinations(list_of_cards):
    L= list_of_cards
    D={}
    for m in L:
        D[m.rank]=m
    lst=[]
    for n in L:
        lst.append(n.rank)
    combinations_list=[]
    tokens = 0
    double_value = None
    triple_value = None
    A = []  # list of pairs
    B = []  # list of triples
    for card in lst:
        if lst.count(card)==2:
            if card not in A:
                A.append(card)
        if lst.count(card) == 3:
            if card not in B:
                B.append(card)
        if lst.count(card)==4:
            combinations_list.append(("Four of a kind",[card]))
            break
    if len(A)==3:
          A.remove(return_lower_card([D[A[0]],D[A[1]],D[A[2]]]).rank)
    if len(A)==2:
        combinations_list.append(("two pair",sorted([A[0],A[1]], reverse= True)))
        tokens=2
    elif len(A)==1:
        combinations_list.append(("Pair",[A[0]]))
        tokens=1
    if len(B)==2:
        triple_value=return_higher_card([D[B[0]],D[B[1]]])
        B.remove(triple_value.rank)
        double_value=B[0]
    elif len(B)==1:
        triple_value=B[0]
        if tokens==2:
            double_value= return_higher_card([D[A[0]],D[A[1]]]).rank
        elif tokens==1:
            double_value= A[0]
        elif tokens==0:
            combinations_list.append(("Three of a kind",[B[0]]))
    if double_value is not None:
        combinations_list.append(("Full house",[triple_value,double_value]))
    if len(combinations_list) == 0:
        return
    E={}
    for t in combinations_list:
        E[t[0]]=t[1]
    a= max(E.keys(),key=combinations_ranking().get)
    return a,E[a]
#to show rest of the code for same_rank_combintaion press on arrow

def cards_same_suit(list_of_cards): #function for flush
    flush = False
    L = list_of_cards
    C=[]
    for j in L:
        a= sum(t.suit == j.suit for t in L)
        #print (a)
        if a >= 5:
            C.append(j)
            if len(C) >= 5:
                flush = True
    if flush is False:
        return 
    return C

def flush(list_of_cards):
    C = cards_same_suit(list_of_cards)
    if C is None:
        return 
    while len(C)>5:
        min_object= C[0]
        for i in range(1,len(C)):
            if min_object != return_lower_card([C[i],min_object]):
                min_object=C[i]
        C.remove(min_object)
    C = sorted(C, key=operator.attrgetter("number_value"), reverse= True)
    flush_cards_values = []
    for n in C:
        flush_cards_values.append(n.rank)
    return ("Flush", flush_cards_values)

def straight(list_of_cards):
    straight = False
    L= list_of_cards
    K= []
    for j in L:
        K.append(j.number_value)
    if 14 in K:
        K.append(1)  # in case Ace is used as 1 
    M = sorted(set(K))
    for i in range(len(K)- 4):
        if M[i+1]-M[i]==1 and M[i+2]-M[i+1]==1 and M[i+3]-M[i+2]==1 and M[i+4]-M[i+3]==1:
            straight = True
            highest_card_index = i+4
    if not straight:
        return 
    straight_cards = M[highest_card_index -4 : highest_card_index +1]
    straight_cards_values = []
    for n in straight_cards:
        straight_cards_values.append(cards_values_reversed()[n])
    return ("Straight",straight_cards_values)

def straight_flush_and_royal_flush(list_of_cards): #also includes flush and straight.
    A= cards_same_suit(list_of_cards) #first we check if there is a flush, if there
    if A is None: #isn't then there can't be straight F or royal F,and all thats left to check is if there is a straight.
        return straight(list_of_cards)
    B= straight(A)# now we check if there is a straight from the flush cards we got,if there
    if B is None:#isn't then there can't be straight F or royal F,and all thats left to return the flush.
        return flush(list_of_cards)# yes, there is some code duplication here.
    #there is no point to check if there is a regular straight because flush beats straight.
    if 10 in B[1] and "Jack" in B[1] and "Queen" in B[1] and "King" in B[1] and "Ace" in B[1]:
        return "ROYAL FLUSH" # we check the option for royal flush
    else:
        return ("Straight flush", B[1])


#print(straight_flush_and_royal_flush(card31, card32, card33, card34, card35, card36, card37))


king_of_diamonds =  cards("diamond","King")

king_of_spades= cards("spades","King")

card_1=cards("spades","King")
card_2=cards("spades","Ace")
card_3=cards("clubs",7)
card_4=cards("clubs",9)
card_5=cards("spades","Queen")
card_6=cards("spades",5)
card_7=cards("spades",10)

#print(same_rank_combinations([card_1,card_2,card_3,card_4,card_5,card_6,card_7]))


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

#######combinations and decision which combination is stronger ###################################################

def strongest_combination(list_of_cards):
    option_1= straight_flush_and_royal_flush(list_of_cards)
    option_2= same_rank_combinations(list_of_cards)
    #print(option_1, option_2)
    if option_1 is None and option_2 is None:
        return high_card(list_of_cards)
    if option_1 is None:
        return option_2
    elif option_2 is None:
        return option_1 
    if option_1 == "ROYAL FLUSH" or option_2 == "ROYAL FLUSH":
        return "ROYAL FLUSH"
    if combinations_ranking()[option_1[0]] > combinations_ranking()[option_2[0]]:
        return option_1
    else:
        return option_2

def pair_clash(pair_1,pair_2): #the arguments here will be best_hand_1 and best_hand_2
    #return pair_1,pair_2
    if cards_values()[pair_1[1][0]] > cards_values()[pair_2[1][0]]:
        return pair_1
    elif cards_values()[pair_2[1][0]] > cards_values()[pair_1[1][0]]:
        return pair_2
    else:
        return "draw"

def two_pair_clash(two_pair_1, two_pair_2): #same format as pair_clash
    first_pair_comparison = pair_clash(two_pair_1, two_pair_2)
    if first_pair_comparison != "draw":
        return first_pair_comparison
    else:
        if cards_values()[two_pair_1[1][1]] > cards_values()[two_pair_2[1][1]]:
            return two_pair_1
        elif cards_values()[two_pair_2[1][1]] > cards_values()[two_pair_1[1][1]]:
            return two_pair_2
        else:
            return "draw"

def Three_of_a_kind_clash(Three_of_a_kind_1, Three_of_a_kind_2): #same format as pair_clash
    return pair_clash(Three_of_a_kind_1, Three_of_a_kind_2)
    
def straight_clash(straight_1 , straight_2):
    if cards_values()[straight_1[1][-1]] > cards_values()[straight_2[1][-1]]:
        return straight_1
    elif cards_values()[straight_2[1][-1]] > cards_values()[straight_1[1][-1]]:
        return straight_2
    else:
        return "DRAW!"

def flush_clash(flush_1, flush_2):
    #return flush_1, flush_2
    for i in range(len(flush_1[1])):
        cur_high_card_1 = cards_values()[flush_1[1][i]]
        cur_high_card_2 = cards_values()[flush_2[1][i]]
        if cur_high_card_1 != cur_high_card_2: 
            if cur_high_card_1 > cur_high_card_2:
                return flush_1
            else:
                return flush_2
    return "DRAW!"

def full_house_clash(full_house_1, full_house_2):
    result = two_pair_clash(full_house_1, full_house_2)
    if result != "draw":
        return result
    else:
        return "DRAW!"

def four_of_a_kind_clash(four_of_a_kind_1, four_of_a_kind_2):
    return pair_clash(four_of_a_kind_1, four_of_a_kind_2)

def straight_flush_clash(straight_flush_1, straight_flush_2):
    return straight_clash(straight_flush_1, straight_flush_2)


def high_card_clash(high_card_1, high_card_2):
    sorted_1 = sorted(high_card_1, key=cards_values().get, reverse= True)
    sorted_2 = sorted(high_card_2, key=cards_values().get, reverse= True)
    for i in range(5):
        cur_high_card_1 = cards_values()[sorted_1[i]]
        cur_high_card_2 = cards_values()[sorted_2[i]]
        if cur_high_card_1 != cur_high_card_2: 
            if cur_high_card_1 > cur_high_card_2:
                return ("High Card" , sorted_1[i])
            else:
                return ("High Card" , sorted_2[i])
    return "DRAW!"



def strongest_hand(hand_1,hand_2):
    draw = False
    best_hand_1 = strongest_combination(hand_1)
    best_hand_2 = strongest_combination(hand_2)
    #return best_hand_1,best_hand_2
    if best_hand_1 == "ROYAL FLUSH" and best_hand_2 == "ROYAL FLUSH":
        return "DRAW"
    if best_hand_1 == "ROYAL FLUSH" or best_hand_2 == "ROYAL FLUSH":
        return "ROYAL FLUSH"

    if combinations_ranking()[best_hand_1[0]] > combinations_ranking()[best_hand_2[0]]: # to fix this so it will use the card_values dict for the comparison
        #print("lalala")
        return best_hand_1
    elif combinations_ranking()[best_hand_2[0]] > combinations_ranking()[best_hand_1[0]]:
        return best_hand_2
    else:
        if best_hand_1[0] == "High Card":
            print("lalalalal")
            lst_1 = []
            lst_2 = []
            for i in hand_1:
                lst_1.append(i.rank)
            for j in hand_2:
                lst_2.append(j.rank)
            return high_card_clash(lst_1, lst_2)

        #print("yoyo")
        if best_hand_1[0] == "Pair": # later on make one function for all 3 cases
            result = pair_clash(best_hand_1,best_hand_2)
            if result != "draw":
                return result
            else:
                draw = True
        elif best_hand_1[0] == "two pair":
            result = two_pair_clash(best_hand_1,best_hand_2)
            if result != "draw":
                return result
            else:
                draw = True

        elif best_hand_1[0] == "Three of a kind":
            result = Three_of_a_kind_clash(best_hand_1,best_hand_2)
            if result != "draw":
                return result
            else:
                draw = True

        elif best_hand_1[0] == "Four of a kind":
            result = four_of_a_kind_clash(best_hand_1,best_hand_2)
            if result != "draw":
                return result
            else:
                draw = True
        
        if best_hand_1[0] == "Pair" or best_hand_1[0] == "two pair" or best_hand_1[0] == "Three of a kind"\
            or best_hand_1[0] == "Four of a kind": 
            if draw is True:
                Kicker_1 = Kicker(hand_1,best_hand_1[1])
                Kicker_2 = Kicker(hand_2,best_hand_2[1])
                if Kicker_1.number_value != Kicker_2.number_value:
                    higher_kicker = return_higher_card([Kicker_1,Kicker_2])
                    return [best_hand_1, "kicker: " + str(higher_kicker.rank)] # couldeve written best_hand_2 as well
                else:
                    return "DRAW!"


        if best_hand_1[0] == "Straight":
            return straight_clash(best_hand_1, best_hand_2)
        
        if best_hand_1[0] == "Flush": 
            return flush_clash(best_hand_1, best_hand_2)
        
        if best_hand_1[0] == "Full house":
            return full_house_clash(best_hand_1, best_hand_2)

        #if best_hand_1[0] == "Four of a kind":
            #return four_of_a_kind_clash(best_hand_1, best_hand_2)
         
        if best_hand_1[0] == "Straight flush":
            return straight_flush_clash(best_hand_1, best_hand_2)

        


        # now i will build functions that can determin who is the winner between 2 combinations and 
        #then refer to them here.


def Kicker(hand, combination):
    #return hand,combination
    not_in_combination = []
    for card in hand:
        #print(card.rank)
        if card.rank not in combination:
            not_in_combination.append(card)
    #return not_in_combination
    Kicker = return_higher_card(not_in_combination)
    return Kicker

#######combinations and decision which combination is stronger ###################################################

#print (strongest_hand(lst_0,lst_1))



###card generator###

def card_generator():
    card1 = card_generator_beta_test()
    if current_cards(card1) == "no doubles please":
        return card_generator_beta_test()
    return card1

def card_generator_beta_test():
    suit= random.choice(["diamonds","spades","clubs","hearts"])
    L=list(range(2,11))
    #return L
    L.extend(["Jack","Queen","King","Ace"])
    rank= random.choice(L)
    #card1 = cards(suit,rank)
    return cards(suit,rank)

def current_cards(card):
    L= []
    if card not in L:
        L.append(card)
    else:
        return "no doubles please"

###card generator###





######## starting at 13.02.22


def single_card_generator():
    suit = random.choice(["diamonds","spades","clubs","hearts"])
    possible_ranks = list(range(2,11))
    possible_ranks.extend(["Jack","Queen","King","Ace"])
    #L.extend(["Jack","Queen","King","Ace"])
    rank = random.choice(possible_ranks)
    #card1 = cards(suit,rank)
    return cards(suit,rank)


print("single_card_generator: ", single_card_generator())


def multiple_card_generator(n, used_cards = []):
    # get n random generated cards without doubles.
    # the used_cards argument is a list of cards already used in a current poker round, and so if we wanted
    # to generate cards for rounds we should generate cards that were not used already in the current round.


    # if not used_cards:
    #     generated_cards = []
    # else:
    #     #generated_cards = used_cards
    #     generated_cards = used_cards.copy()

    generated_cards = []

    #card_count = 0
    while len(generated_cards) < n:
        generated_card = single_card_generator()
        if (generated_card not in generated_cards) and (generated_card not in used_cards):
            generated_cards.append(generated_card)
            #card_count +=1

    return generated_cards
             

    # while len(generated_cards) < n:
    #     generated_card = single_card_generator()
    #     if generated_card not in generated_cards:
    #         generated_cards.append(generated_card)
    # return generated_cards

print("multiple_card_generator: ",multiple_card_generator(7))


# c1 = cards("spades",7)
# c2 = cards("spades",7)
# print(c1 == c2) 
# print(str(c1)) 


######## starting at 13.02.22




class player:
    def __init__(self, name):
        self.name = name
        self.start_hand = []
        self.common_cards = []

    # generate starting hand for each round
    def get_current_starting_hand(self, cards):
        self.start_hand.extend(cards)

    # adds generated common cards to the player's common cards
    def add_cards_to_common(self, cards):
        self.common_cards.extend(cards)


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

generate_starting_hand_for_all_players(players)
print("\n")
# print("used_cards_for_current_round: ",used_cards_for_current_round)
for player in players:
    print(player.name,"starting hand: " ,player.start_hand)
# print("\n")


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

flop(non_folded_players)
turn(non_folded_players)
river(non_folded_players)
print("common_cards: ",common_cards)
print("\n")
print("used_cards_for_current_round: ",used_cards_for_current_round)
# print("maxim.common_cards: ",maxim.common_cards)
# print("dude.common_cards: ",dude.common_cards)
# print("bro.common_cards: ",bro.common_cards)


