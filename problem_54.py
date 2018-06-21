# Functions for determining a hand
def flush(hand):
	return (hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and 
	   	    hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1])

def straight(hand):
	return ((hand[0][0] == hand[1][0] + 1 and hand[1][0] == hand[2][0] + 1 and 
		     hand[2][0] == hand[3][0] + 1 and hand[3][0] == hand[4][0] + 1) or
		    (hand[0][0] == 14 and hand[1][0] == 5 and hand[2][0] == 4 and 
	         hand[3][0] == 3 and hand[4][0] == 2))

def royal_flush(hand):
	return (flush(hand) and hand[0][0] == 14 and hand[1][0] == 13 and 
	        hand[2][0] == 12 and hand[3][0] == 11 and hand[4][0] == 10)

def straight_flush(hand):
	return flush(hand) and straight(hand)

def four_of_a_kind(hand):
	return (hand[1][0] == hand[2][0] and hand[1][0] == hand[3][0] and 
		    (hand[0][0] == hand[1][0] or hand[4][0] == hand[1][0]))

def full_house(hand):
	return ((hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] == hand[4][0]) or
		    (hand[0][0] == hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]))

def three_of_a_kind(hand):
	return ((hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0]) or
		    (hand[0][0] != hand[1][0] and hand[1][0] == hand[2][0] and 
			 hand[2][0] == hand[3][0] and hand[3][0] != hand[4][0]) or
		    (hand[0][0] != hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]))

def two_pair(hand):
	return ((hand[0][0] == hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] == hand[3][0] and hand[3][0] != hand[4][0]) or
		    (hand[0][0] == hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] == hand[4][0]) or
		    (hand[0][0] != hand[1][0] and hand[1][0] == hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] == hand[4][0]))

def pair(hand):
	return ((hand[0][0] == hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0]) or
		    (hand[0][0] != hand[1][0] and hand[1][0] == hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0]) or
		    (hand[0][0] != hand[1][0] and hand[1][0] != hand[2][0] and 
	  		 hand[2][0] == hand[3][0] and hand[3][0] != hand[4][0]) or
	 	    (hand[0][0] != hand[1][0] and hand[1][0] != hand[2][0] and 
			 hand[2][0] != hand[3][0] and hand[3][0] == hand[4][0]))

# Functions for comparing if the hands are the same
def compare_straight(h1, h2):
	highcard1 = 5 if (h1[0][0] == 14 and h1[1][0] == 5) else h1[0][0] 
	highcard2 = 5 if (h2[0][0] == 14 and h2[1][0] == 5) else h2[0][0]
	return highcard1 > highcard2

def compare_straight_flush(h1, h2):
	return compare_straight(h1, h2)

def compare_high_card(h1, h2):
	''' True if h1 is better than h2. '''
	return ((h1[0][0] > h2[0][0]) or (h1[0][0] == h2[0][0] and h1[1][0] > h2[1][0]) or
		    (h1[0][0] == h2[0][0] and h1[1][0] == h2[1][0] and h1[2][0] > h2[2][0]) or
		    (h1[0][0] == h2[0][0] and h1[1][0] == h2[1][0] and 
		   	 h1[2][0] == h2[2][0] and h1[3][0] > h2[3][0]) or
		    (h1[0][0] == h2[0][0] and h1[1][0] == h2[1][0] and h1[2][0] == h2[2][0] and 
		   	 h1[3][0] == h2[3][0] and h1[4][0] > h2[4][0]))

def compare_flush(h1, h2):
	return compare_high_card(h1, h2)

def compare_four_of_a_kind(h1, h2):
	h1_four = h1[0][0] if h1[0][0] == h1[1][0] else h1[1][0]
	h1_one  = h1[4][0] if h1[0][0] == h1[1][0] else h1[0][0]
	h2_four = h2[0][0] if h2[0][0] == h2[1][0] else h2[1][0]
	h2_one  = h2[4][0] if h2[0][0] == h2[1][0] else h2[0][0]
	return (h1_four > h2_four) or (h1_four == h2_four and h1_one > h2_one)

def compare_full_house(h1, h2):
	h1_three = h1[0][0] if h1[1][0] == h1[2][0] else h1[2][0]
	h1_two   = h1[3][0] if h1[1][0] == h1[2][0] else h1[0][0]
	h2_three = h2[0][0] if h2[1][0] == h2[2][0] else h2[2][0]
	h2_two   = h2[3][0] if h2[1][0] == h2[2][0] else h2[0][0]
	return (h1_three > h2_three) or (h1_three == h2_three and h1_two > h2_two)

def compare_three_of_a_kind(h1, h2):
	h1_three, h2_three = h1[2][0], h2[2][0]
	return compare_high_card(h1, h2) if h1_three == h2_three else (h1_three > h2_three)

def compare_two_pair(h1, h2):
	h1_p1, h1_p2, h2_p1, h2_p2 = h1[1][0], h1[3][0], h2[1][0], h2[3][0]
	if h1_p1 > h2_p1:
		return True
	elif h1_p1 == h2_p1 and h1_p2 > h2_p2:
		return True
	elif h1_p1 == h2_p1 and h1_p2 == h2_p2:
		return compare_high_card(h1, h2)
	else:
		return False

def compare_pair(h1, h2):
	h1_p = (h1[0][0] if h1[0][0] == h1[1][0] else h1[1][0] if h1[1][0] == h1[2][0] else
		    h1[2][0] if h1[2][0] == h1[3][0] else h1[3][0])
	h2_p = (h2[0][0] if h2[0][0] == h2[1][0] else h2[1][0] if h2[1][0] == h2[2][0] else
		    h2[2][0] if h2[2][0] == h2[3][0] else h2[3][0])
	if h1_p > h2_p:
		return True
	elif h1_p == h2_p:
		return compare_high_card(h1, h2)
	else: 
		return False

# Load in the hands
mapping_value_to_int = {
	'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
	'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
hands = [line.split(' ') for line in open('p054_poker.txt','r').readlines()]
hands = [[(mapping_value_to_int[card[0]], card[1]) for card in hand] for hand in hands]
hands_p1, hands_p2 = [hand[:5] for hand in hands], [hand[5:] for hand in hands]

# Sort the hands on value
hands_p1 = [sorted(h, key=lambda x: x[0], reverse=True) for h in hands_p1]
hands_p2 = [sorted(h, key=lambda x: x[0], reverse=True) for h in hands_p2]

# Each hand is a list of tuples (value, suit). For each, figure out the best.
wins = 0
for h1, h2 in zip(hands_p1, hands_p2):
	if royal_flush(h1) or royal_flush(h2):
		wins += 1 if royal_flush(h1) else 0
	elif four_of_a_kind(h1) or four_of_a_kind(h2):
		if four_of_a_kind(h1) and not four_of_a_kind(h2):
			wins += 1
		elif four_of_a_kind(h1) and four_of_a_kind(h2):
			wins += 1 if compare_four_of_a_kind(h1, h2) else 0
	elif full_house(h1) or full_house(h2):
		if full_house(h1) and not full_house(h2):
			wins += 1
		elif full_house(h1) and full_house(h2):
			wins += 1 if compare_full_house(h1, h2) else 0
	elif flush(h1) or flush(h2):
		if flush(h1) and not flush(h2):
			wins += 1
		elif flush(h1) and flush(h2):
			wins += 1 if compare_flush(h1, h2) else 0
	elif straight(h1) or straight(h2):
		if straight(h1) and not straight(h2):
			wins += 1
		elif straight(h1) and straight(h2):
			wins += 1 if compare_straight(h1, h2) else 0
	elif three_of_a_kind(h1) or three_of_a_kind(h2):
		if three_of_a_kind(h1) and not three_of_a_kind(h2):
			wins += 1
		elif three_of_a_kind(h1) and three_of_a_kind(h2):
			wins += 1 if compare_three_of_a_kind(h1, h2) else 0
	elif two_pair(h1) or two_pair(h2):
		if two_pair(h1) and not two_pair(h2):
			wins += 1
		elif two_pair(h1) and two_pair(h2):
			wins += 1 if compare_two_pair(h1, h2) else 0
	elif pair(h1) or pair(h2):
		if pair(h1) and not pair(h2):
			wins += 1
		elif pair(h1) and pair(h2):
			wins += 1 if compare_pair(h1, h2) else 0
	else:
		wins += 1 if compare_high_card(h1, h2) else 0
print wins
