#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The file, poker.txt, contains one-thousand random hands
# dealt to two players. Each line of the file contains ten
# cards (separated by a single space): the first five are
# Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid 
# characters or repeated cards), each player's hand is in 
# no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
#
import math,sys,string,itertools

fh = open('./p054-poker.txt', 'r')
games = []

order=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def order_hand(hand):
  ordered = []
  for rank in order:
    for card in hand:
      if card[0] == rank:
        ordered.append(card)
  return ordered

# all cards must have same suit
def is_flush(hand):
  suit = [x[1] for x in hand]
  if len(sorted(set(suit))) == 1:
    return True
  else:
    return False

# for an ordered hand to be a straight,
# the last card must be 4 values higher than the first
# and all ranks must be unique
def is_straight(hand):
  span = order.index(hand[4][0]) - order.index(hand[0][0])
  rank = [x[0] for x in hand]
  if span == 4 and len(sorted(set(rank))) == 5:
    return True
  else:
    return False

def set_count(hand):
  sets = [0 for x in range(0,len(order))]
  for card in hand:
    sets[order.index(card[0])] += 1
  return sets

def high_card(hand):
  set_array = set_count(hand)
  ranks = [i for i, e in enumerate(set_array) if e != 0]
  return sorted(set(ranks))[-1]

# 1 High Card: Highest value card.
# 2 One Pair: Two cards of the same value.
# 3 Two Pairs: Two different pairs.
# 4 Three of a Kind: Three cards of the same value.
# 5 Straight: All cards are consecutive values.
# 6 Flush: All cards of the same suit.
# 7 Full House: Three of a kind and a pair.
# 8 Four of a Kind: Four cards of the same value.
# 9 Straight Flush: All cards are consecutive values of same suit.
def hand_value(hand):
  if is_flush(hand) and is_straight(hand):
    print "Straight Flush, " + order[high_card(hand)] + " high"
    return [9,high_card(hand)]
  elif is_straight(hand):
    print "Straight, " + order[high_card(hand)] + " high"
    return [5,high_card(hand)]
  elif is_flush(hand):
    print "Flush, " + order[high_card(hand)] + " high"
    return [6,high_card(hand)]

  if 4 in set_count(hand):
    high = set_count(hand).index(4)
    print "4 of a kind, " + order[high] + " high"
    return [8,high]

  if 3 in set_count(hand):
    high = set_count(hand).index(3)
    if 2 in set_count(hand):
      print "Full house, " + order[high] + " high"
      return [7,high]
    print "3 of a kind, " + order[high] + " high"
    return [4,high]

  if 2 in set_count(hand):
    high = 0
    pairs = 0
    hand_set = set_count(hand)
    for i in range(0,len(order)):
      if hand_set[i] == 2:
        high = i
        pairs += 1
    if pairs == 2:
      print "Two Pairs, " + order[high] + " high"
      return [3,high]
    else:
      print "One Pair, " + order[high] + " high"
      return [2,high]

  print "High Card, " + str(high_card(hand))
  return [1,high_card(hand)]

for line in fh:
  games.append([str(x) for x in line.strip().split(' ')])

solution = 0

for game in games:
  hand_1 = order_hand(game[:5])
  hand_2 = order_hand(game[5:])
  print hand_1, hand_2
  if hand_value(hand_1)[0] > hand_value(hand_2)[0]:
    print "hand 1 wins"
    solution += 1
  elif hand_value(hand_1)[0] < hand_value(hand_2)[0]:
    print "hand 2 wins"
  elif hand_value(hand_1)[1] > hand_value(hand_2)[1]:
    print "hand 1 wins"
    solution += 1
  elif hand_value(hand_1)[1] < hand_value(hand_2)[1]:
    print "hand 2 wins"
  else:
    print "TIE!"

print "Solution: " + str(solution)

