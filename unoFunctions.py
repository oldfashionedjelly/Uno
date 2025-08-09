from unoClasses import *
from unoData import *
import random

def setUp(uno_deck):
  num_players = int(input("How many players are playing?\n"))
  if num_players > 1 and num_players < 11:
    for i in range(0, num_players):
      name = input("What is the name of player " + str(i + 1) + "?\n")
      player = UnoPlayer(name)
      players.append(player)
  else:
    print("Sorry, you need between 2 and 10 players to play")
  for i in range(0, 4):
    uno_deck.append(UnoCard("Wild", colors[i]))
    uno_deck.append(UnoCard("+4", colors[i]))
    uno_deck.append(UnoCard("0", colors[i]))
    for j in range(0, len(kinds)):
      uno_deck.append(UnoCard(kinds[j], colors[i]))
      uno_deck.append(UnoCard(kinds[j], colors[i]))

  #cards = Deck(uno_deck)
  for player in players:
    for i in range(0, 7):
      player.getCard(uno_deck)

  pile = DiscardPile()

  game = UNO(players, uno_deck, pile)
  return game
 
def isReversed(card, reverse):
  if card != None:
    if card.value == "Reverse":
      new_reverse = not reverse
    else:
      new_reverse = reverse
    return new_reverse
  else:
    return reverse

def isPlaying(player):
  if len(player.cards) == 1:
    print(player.name + " has UNO!")
    return True
  elif len(player.cards) == 0:
    print(player.name + " has won!")
    return False
  else:
    return True

def Add(add, card):
  if card != None:
    if card.value == "+4":
      add = 2
    elif card.value == "+2":
      add = 2
    elif card.value == "Skip":
      add = 2
    else:
      add = 1
  else:
    add = 1
  return add

def playGame(game):
  playing = True
  while playing:
    if len(players) > 1 and len(players) < 11:
      reverse = False
      nextTurn = 0
      add = 1
      player = players[nextTurn]
      while playing:
        card = playerTurn(game, player, nextTurn, uno_deck)
        reverse = isReversed(card, reverse)
        add = Add(add, card)
        if not reverse:
          nextTurn += add
        else:
          nextTurn -= add
        player = players[nextTurn % len(players)]
        if len(uno_deck) == 0:  
          for i in range(0, 4):
            uno_deck.append(UnoCard("Wild", colors[i]))
            uno_deck.append(UnoCard("+4", colors[i]))
            uno_deck.append(UnoCard("0", colors[i]))
            for j in range(0, len(kinds)):
              uno_deck.append(UnoCard(kinds[j], colors[i]))
              uno_deck.append(UnoCard(kinds[j], colors[i]))
        playing = isPlaying(player)

def playerTurn(game, player, turn, deck):
  playing = True
  while playing:
    play = False
    print("It is " + player.name + "'s turn")
    for i in range(0, len(player.cards)):
      print(str(i + 1) + ". " + str(player.cards[i]))
    if game.pile.number != None:
      if game.pile.number != "Wild" and game.pile.number != "+4":
        print("The top card is a " + game.pile.color + " " + str(game.pile.number) + " card")
      else:
        print("The top card is a " + str(game.pile.number) + " card")
      validCards = []
      for card in player.cards:
        if game.pile.validCard(card):
          validCards.append(card)
      if len(validCards) != 0:
        play = True
      else:
        print("Sorry, you don't have a valid card to play, " + player.name + "\nHere is your new card: ")
        newCard = player.getCard(game.deck)
        print(newCard)
        if game.pile.validCard(newCard):
          print("You can play your new card!")
          game.pile.addCard(player.playCard(newCard))
          if newCard.value == "+2":
            print("These are " + players[turn + 1].name + " new cards:\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)))
          if newCard.value == "+4":
            print("These are " + players[turn + 1].name + " new cards:\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)))
            return newCard
          else:
            return None
    else:
      play = True

    if play:
      isValid = False
      while not isValid:
        card_id = int(input("Chose a card to play (1, 2, 3, etc)\n"))
        card_to_play = player.cards[card_id - 1]
        if game.pile.validCard(player.cards[card_id - 1]) or game.pile.number == None:
          game.pile.addCard(player.playCard(card_to_play))
          isValid = True
          if card_to_play.value == "+2":
            print("These are " + players[turn + 1].name + " new cards:\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)))
          if card_to_play.value == "+4":
            print("These are " + players[turn + 1].name + " new cards:\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)) + "\n" + str(players[turn + 1].getCard(deck)))
        else:
          print("That card is not playable")
      return card_to_play
    else:
      return None

  playing = isPlaying(player)
