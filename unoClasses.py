import random
from unoFunctions import *
from unoData import *

class UnoCard():
  def __init__(self, value, color):
    self.value = value
    self.color = color
    if self.value == "Wild" or self.value == "+4":
      self.color = None
  def __str__(self):
    if self.color != None:
      return self.color + " " + str(self.value) + " card"
    else:
      return self.value + " card"

class UnoPlayer():
  def __init__(self, name):
    self.cards = []
    self.name = name

  def __str__(self):
    return self.name

  def getCard(self, uno_deck):
    card = uno_deck[random.randint(0, len(uno_deck) - 1)]
    uno_deck.remove(card)
    self.cards.append(card)
    return card

  def playCard(self, card):
    self.cards.remove(card)
    return card

#class Deck():
  #def __init__(self, deck):
    #self.deck = deck

class DiscardPile():
  def __init__(self):
    self.color = colors[random.randint(0, len(colors) - 1)]
    self.number = kinds[random.randint(0, len(kinds) - 1)]

  def validCard(self, card):
    if card.color == self.color:
      return True
    if card.value == self.number:
      return True
    if card.value == "Wild":
      return True
    if card.value == "+4":
      return True

  def addCard(self, card):
    if card.value == "Wild" or card.value == "+4":
      self.wildCard()
      return
    self.color = card.color
    self.number = card.value

  def wildCard(self):
    color = input("What would you like the color to be?\nGreen, Red, Blue, or Yellow: ")
    self.color = color
    self.number = "Wild"
    print("The new color is " + color)

class UNO():
  def __init__(self, players, deck, pile):
    self.players = players
    self.deck = deck
    self.pile = pile
