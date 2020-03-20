from collections import deque
import random

class DeckEmptyError(Exception):
   # Constructor or Initializer 
   def __init__(self, value): 
      self.value = value 
     
   # __str__ is to print() the value 
   def __str__(self): 
      return(repr(self.value)) 

class Cards(object):

   #Dictionary with card color as key and corresponding value as points.
   shades_points_dict = {'Green': 1,'Red': 3,'Yellow' : 2}
       
   def __init__(self):
      self.deck_of_cards= deque([(y,x) for x in range(1,14) for y in Cards.shades_points_dict.keys()])
           
   def shuffle(self):
      random.shuffle(self.deck_of_cards)
      return self.deck_of_cards         
      
   def get_top_card(self):
      if len(self.deck_of_cards)==0:
         raise DeckEmptyError("Invalid operation: No more elements in Deck")
      else:   
         return self.deck_of_cards.pop()

   def sort(self,color_list):
      sorted_list= deque()
      if len(color_list)==0:
         print("Invalid input, expecting non-empty color list")
         return
         
      for x in color_list:
        if x not in Cards.shades_points_dict.keys():
           print("Invalid Input, invalid color given as input")
           return      
          
      for x in color_list:
          sort1=deque()
          for y in self.deck_of_cards:
             if x == y[0]:
                sort1.append(y)
          sort1=sorted(sort1,key=lambda card:card[1])
          sorted_list.extend(sort1)
      self.deck_of_cards = sorted_list
      return self.deck_of_cards
       
   def determine_winner(self,list1,list2):
      points_player1=0
      points_player2=0 
      if len(list1) !=3 or\
         len(list2) !=3:
         print("Invalid Input, please make 3 draws for each player")
         return "Invalid Input, please make 3 draws for each player"
         
      for x in list1:
          points_player1+=Cards.shades_points_dict[x[0]] * x[1]
      for x in list2:
          points_player2+=Cards.shades_points_dict[x[0]] * x[1]
      if points_player1>points_player2:
         print("Congratulations!!!,Winner is player1")
         return "Winner player1"
      elif points_player2>points_player1:
         print("Congratulations!!!,Winner is player2")
         return "Winner player2"
      else:
         print("Its a draw")      
         return "Its a draw"
           
my_cards = Cards()

print(str(my_cards.deck_of_cards))

print(my_cards.sort(['Yellow','Red','Green']))

print(str(my_cards.sort(['Yellow','Red','Blue'])))

print(str(my_cards.sort([])))


if __name__ == '__main__':
   try:
     for x in range (1,50):
       print(str(my_cards.get_top_card()))
   except Exception as e:
        print(e)

print(str(my_cards.shuffle()))

my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Red',1),('Red',2),('Red',3)])
my_cards.determine_winner([('Red',1),('Red',2),('Red',3)],[('Green',1),('Green',2),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2)],[('Green',1),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',2),('Green',3)])
my_cards.determine_winner([('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])

import unittest

class TestStringMethods(unittest.TestCase):

    def test_determine_winner(self):
        mycards = Cards()
        self.assertEqual(my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Red',1),('Red',2),('Red',3)])
, "Winner player2")
        self.assertEqual(my_cards.determine_winner([('Red',1),('Red',2),('Red',3)],[('Green',1),('Green',2),('Green',3)])
, "Winner player1")
        self.assertEqual(my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])
, "Its a draw")
        self.assertEqual(my_cards.determine_winner([('Green',1),('Green',2)],[('Green',1),('Green',3)])
, "Invalid Input, please make 3 draws for each player")
        self.assertEqual(my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',2),('Green',3)])
, "Invalid Input, please make 3 draws for each player")
        self.assertEqual(my_cards.determine_winner([('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])
, "Invalid Input, please make 3 draws for each player")

    def test_sort(self):
        my_cards= Cards()
        self.assertEqual(my_cards.sort([]),None)
        self.assertEqual(my_cards.sort(['Yellow','Red','Green']),deque([('Yellow', 1), ('Yellow', 2), ('Yellow', 3), ('Yellow', 4), ('Yellow', 5), ('Yellow', 6), ('Yellow', 7), ('Yellow', 8), ('Yellow', 9), ('Yellow', 10), ('Yellow', 11), ('Yellow', 12), ('Yellow', 13), ('Red', 1), ('Red', 2), ('Red', 3), ('Red', 4), ('Red', 5), ('Red', 6), ('Red', 7), ('Red', 8), ('Red', 9), ('Red', 10), ('Red', 11), ('Red', 12), ('Red', 13), ('Green', 1), ('Green', 2), ('Green', 3), ('Green', 4), ('Green', 5), ('Green', 6), ('Green', 7), ('Green', 8), ('Green', 9), ('Green', 10), ('Green', 11), ('Green', 12), ('Green', 13)]))
        self.assertEqual(my_cards.sort(['Yellow','Red','Blue']),None)

    def test_get_top_card(self):
        my_cards= Cards()
        self.assertEqual(my_cards.get_top_card(), ('Yellow', 13))
        

if __name__ == '__main__':
    unittest.main()