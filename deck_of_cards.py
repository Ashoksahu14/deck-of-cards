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
    
   shades =('Green','Red','Yellow'    )
   def __init__(self):
      """initializes deck of cards as pair of ('shade','number') where shades are
      in ['Green','Red','Yellow' ] and number ranges from 1 to 13 inclusive"""
      
      self.deck_of_cards= deque([(y,x) for x in range(1,14) for y in Cards.shades])
           
   def shuffle(self):
      """Shuffles the deck of cards"""
      random.shuffle(self.deck_of_cards)
      return self.deck_of_cards         
      
   def get_top_card(self):
      """Retruns top of the card"""
      if len(self.deck_of_cards)==0:
         raise DeckEmptyError("Invalid operation: No more elements in Deck")
      else:   
         return self.deck_of_cards.pop()

   def sort(self,color_list):
      """Sorts the deck of cards in order of color_list parameter and number of the
      card. For example If the deck has a card contains with following order 
      (red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2) 
      Sort cards([yellow, green, red]) will return the cards with following order 
      (yellow, 3), (green, 0), (green, 5), (red, 0), (red, 1)"""
      sorted_list= deque()
      if len(color_list)==0:
         print("Invalid input, expecting non-empty color list")
         return
         
      for x in color_list:
        if x not in Cards.shades:
           print("Invalid Input, invalid color given as input")
           return      
          
      for x in color_list:
          sort1=deque()
          for y in self.deck_of_cards:
             if x == y[0]:
                sort1.append(y)
          sort1=sorted(sort1,key=lambda x:x[1])
          sorted_list.extend(sort1)
      self.deck_of_cards = sorted_list
      return self.deck_of_cards
      
class GameInterface(object):
    """Game Interface to be inherited by concrete game classes"""
    
    def play(self):
        """Play game."""
        pass
 
    def reset(self):
        """Reset and restart the game."""
        pass
        
    def stop(self):
        """Stop the game."""
        pass
    
    def display_winner(self):
        """Display 1st winner."""
        pass
    
    def print_player_rank(self):
        """Display 1st winner."""
        pass
        
    def print_player_rank_and_points(self):
        """Display player rank and corresponding points"""
        pass
        
    def display_player_points():
        """Display player points in order"""
        pass
        
        
class DrawCardsGame(GameInterface):
    '''This is a drawing cards game which takes as input number of users and 
    lets users pick 3 cards by taking turns and after all the draws it calculates
    winner as below:
       Whoever has the high score wins the game. (color point calculation, 
       red = 3, yellow =2, green = 1) the point is calculated by 
       color point * number in the card.'''
    
    #Dictionary with card color as key and corresponding value as points.
    shades_points_dict = {'Green': 1,'Red': 3,'Yellow' : 2}
    
    #Number of turns per player till finish of game.
    num_turns = 3
    
    def __init__(self):
        self.cards = Cards()
        self.player_points = {}
        self.player_draws = {}
        self.num_players=0
        
    def _initialize_player_stats(self):
        """initialize player points and stats"""
        self.reset()
        for x in range(self.num_players):
            self.player_draws[f'{x}']=[]
            self.player_points[f'{x}']= 0       
        
    def _rank(self):
        """sort the player points dictionary with key as the points of each 
        player in desending order and return the sorted list"""
        return sorted(self.player_points.items(),key=lambda x:x[1],reverse=True)


    def determine_winner(self,list1,list2):
        """ Determines the winner for 2 player games, takes as input the list
        of all the draws for for both the players"""
        
        points_player1=0
        points_player2=0 
        
        if len(list1) !=DrawCardsGame.num_turns or\
            len(list2) !=DrawCardsGame.num_turns:
            print(f"Invalid Input, please make {DrawCardsGame.num_turns} draws for each player")
            return f"Invalid Input, please make {DrawCardsGame.num_turns} draws for each player"
        
                
        for x in list1:
            points_player1+=DrawCardsGame.shades_points_dict[x[0]] * x[1]
            
        for x in list2:
            points_player2+=DrawCardsGame.shades_points_dict[x[0]] * x[1]
            
        if points_player1>points_player2:
            print("Congratulations!!!,Winner is player1")
            return "Winner player1"
        elif points_player2>points_player1:
            print("Congratulations!!!,Winner is player2")
            return "Winner player2"
        else:
             print("Its a draw")      
             return "Its a draw"          
        
    def play(self):
        """ Makes player play the game. After the game is done winner is determined"""
        self.num_players = int(input("Welcome to card drawing game, Please enter number of players:"))
        #contains all the draws from different players as list of draws per player.
        #with player number as key
        print(f"Num players:{self.num_players}")
        
        #initialize player points and draws
        self._initialize_player_stats()
            
        for y in range(DrawCardsGame.num_turns):
            for x in range(self.num_players):
                input(f"Press enter for turn no {y+1} to draw for player {x+1}:")
                card_drawn = self.cards.get_top_card()
                self.player_draws[f'{x}'].append(card_drawn)
                print(f"card_drawn {card_drawn}")
                self.player_points[f'{x}']+= DrawCardsGame.shades_points_dict[card_drawn[0]] * card_drawn[1]
                print(f"player_points {self.player_points}")
        
        print(repr(self.player_draws))        
        print(repr(self.player_points))        
        self.determine_winner(self.player_draws['0'],self.player_draws['1'])
        self.determine_winner1()
        
    def Reset(self):
        """Resets player stats and game state information"""    
        self.player_draws.clear()
        self.player_points.clear()
        self.num_players=0
        self.cards.shuffle()
         
    def stop(self):
        """Stops/aborts the game and reset player stats"""    
        print("Thank you for playing the game, hope you had fun!!!")
        self.reset()
    
    def determine_winner1(self):
        """prints player rank in sorted order starting with rank 1st. Works for 
         any number of players"""    
        sorted_player_rank = self._rank()
        print(f"sorted player rank: {sorted_player_rank}")
        print(f"winner is player {sorted_player_rank[0]}: with points {sorted_player_rank[0][1]}")
              

   
my_cards = DrawCardsGame()

print(str(my_cards.cards))

print(my_cards.cards.sort(['Yellow','Red','Green']))

print(str(my_cards.cards.sort(['Yellow','Red','Blue'])))

print(str(my_cards.cards.sort([])))


#if __name__ == '__main__':
#   try:
#     for x in range (1,50):
#       print(str(my_cards.cards.get_top_card()))
     
#   except Exception as e:
#        print(e)
print(str(my_cards.cards.shuffle()))

my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Red',1),('Red',2),('Red',3)])
my_cards.determine_winner([('Red',1),('Red',2),('Red',3)],[('Green',1),('Green',2),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2)],[('Green',1),('Green',3)])
my_cards.determine_winner([('Green',1),('Green',2),('Green',3)],[('Green',2),('Green',3)])
my_cards.determine_winner([('Green',2),('Green',3)],[('Green',1),('Green',2),('Green',3)])

import unittest

class TestStringMethods(unittest.TestCase):

    def test_determine_winner(self):
        mycards = DrawCardsGame()
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
    #unittest.main()
    my_cards.play()