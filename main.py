import random
import time
import colorama

from colorama import init
from colorama import Fore, Back, Style

init(autoreset = True)
  
num_ship = 5
opp_num_ship = 5

#Battleship Game Logo

print (Fore.RED + '************************************************')
print (Fore.WHITE + '                   BATTLESHIP')
print (Fore.WHITE + '''
                      __/____
                _____/_______|
        ______/_____\________\_____
        \              < < <      /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
print (Fore.RED + '************************************************')

#Greet user and ask for name
print ("Welcome aboard! May I please have your name?")
name = input (">")
name = name.title()
print ()
print (f"Good day! Admiral {name}, I am your assistant Bort. ")

# Ask if it is their first time playing this game
print ()
while True:
  print ("Is this your first time playing this game? (Y/N)")
  first_time = input (">")
  first_time = first_time.upper()

  #Give background information and game rules if it's their first time, skip if not

  if first_time == "Y":
    print ()
    print ("It's great to have you on board!")
    print ()
    print ("""Here are the rules of the game:
      You are in charge of a fleet of 5 battleships.
      Hide your battleships in your ocean grid to
      avoid attacks from your opponent.
      You and your opponent will take turns to fire
      shots at each other's ocean grid.
      You win if you sink all your opponent's
      battleships.
      You lose if your opponent sink all of yours first.
      """)
    break
  elif first_time == "N":
    print ()
    print ("Welcome back! Let's jump right into it.")
    break
  else:
    print ()
    print (f"Sorry Admiral {name}, I don't quite catch that.")

#Ask if user is ready
while True:
  print ()
  print ("Are you ready to play? (Y/N)")
  ready = input (">")
  ready = ready.upper()
  if ready == "Y":
    break
  elif ready == "N":
    print ()
    print ("Here are the rules again:")
    print ("""
      You are in charge of a fleet of 5 battleships.
      Hide your battleships in your ocean grid to
      avoid attacks from your opponent.
      You and your opponent will take turns to fire
      shots at each other's ocean grid.
      You win if you sink all your opponent's
      battleships.
      You lose if your opponent sink all of yours first.
      """)
  else:
    print ("I am sorry. I don't get that.")


#Make ocean grids (5x5 each)

#User's ocean grid
board1 = ['   ','   ','   ','   ','   ',
        #   0     1     2     3     4
          '   ','   ','   ','   ','   ',
        #   5     6     7     8     9
          '   ','   ','   ','   ','   ',
        #  10     11    12    13    14
          '   ','   ','   ','   ','   ',
        #  15    16     17   18    19
          '   ','   ','   ','   ','   ']
        #  20     21   22    23    24   

#Opponent/Computer's ocean grid
board2 = ['   ','   ','   ','   ','   ',
        #   0     1     2     3     4
          '   ','   ','   ','   ','   ',
        #   5     6     7     8     9
          '   ','   ','   ','   ','   ',
        #  10     11    12    13    14
          '   ','   ','   ','   ','   ',
        #  15    16     17   18    19
          '   ','   ','   ','   ','   ']
        #  20     21   22    23    24        

#Opponent's ocean grid user's view
board3 = ['   ','   ','   ','   ','   ',
        #   0     1     2     3     4
          '   ','   ','   ','   ','   ',
        #   5     6     7     8     9
          '   ','   ','   ','   ','   ',
        #  10     11    12    13    14
          '   ','   ','   ','   ','   ',
        #  15    16     17   18    19
          '   ','   ','   ','   ','   ']
        #  20     21   22    23    24   


def print_board(list):
  print('   ' + '|' + ' 1 ' + '|' + ' 2 ' + '|' + ' 3 ' + '|' + ' 4 ' + '|' + ' 5 ')
  print('---+---+---+---+---+---')
  print(' A ' + '|' + list [0] + '|' + list [1] + '|' + list [2] + '|' + list [3] + '|' + list [4])
  print('---+---+---+---+---+---')
  print(' B ' + '|' + list [5] + '|' + list [6] + '|' + list [7] + '|' + list [8] + '|' + list [9])
  print('---+---+---+---+---+---')
  print(' C ' + '|' + list [10] + '|' + list [11] + '|' + list [12] + '|' + list [13] + '|' + list [14])
  print('---+---+---+---+---+---')
  print(' D ' + '|' + list [15] + '|' + list [16] + '|' + list [17] + '|' + list [18] + '|' + list [19])
  print('---+---+---+---+---+---')
  print(' E ' + '|' + list [20] + '|' + list [21] + '|' + list [22] + '|' + list [23] + '|' + list [24])


#Ask user to hide their 5 battleships on grid
print ()
print (Fore.RED + "***** " + Fore.WHITE + "Preparation" + Fore.RED + " *****")
print ()
print ("You are responsible for hiding 5 battleships from your opponent.")
print ()
print ("This is how your ocean grid will look like:")
print ()
print_board(board1)

i=0
while i<5:
  print ()
  print (f"Where do you want to hide your battleship number {i+1}?")
  battleship = input (">")
  battleship = battleship.upper()
  
  if battleship == 'A1' and board1[0] == '   ':
    board1[0] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'A2' and board1[1] == '   ':
    board1[1] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'A3' and board1[2] == '   ':
    board1[2] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'A4' and board1[3] == '   ':
    board1[3] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'A5' and board1[4] == '   ':
    board1[4] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'B1' and board1[5] == '   ':
    board1[5] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'B2' and board1[6] == '   ':
    board1[6] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'B3' and board1[7] == '   ':
    board1[7] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'B4' and board1[8] == '   ':
    board1[8] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'B5' and board1[9] == '   ':
    board1[9] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'C1' and board1[10] == '   ':
    board1[10] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'C2' and board1[11] == '   ':
    board1[11] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'C3' and board1[12] == '   ':
    board1[12] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'C4' and board1[13] == '   ':
    board1[13] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'C5' and board1[14] == '   ':
    board1[14] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'D1' and board1[15] == '   ':
    board1[15] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'D2' and board1[16] == '   ':
    board1[16] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'D3' and board1[17] == '   ':
    board1[17] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'D4' and board1[18] == '   ':
    board1[18] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'D5' and board1[19] == '   ':
    board1[19] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'E1' and board1[20] == '   ':
    board1[20] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'E2' and board1[21] == '   ':
    board1[21] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'E3' and board1[22] == '   ':
    board1[22] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'E4' and board1[23] == '   ':
    board1[23] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  elif battleship == 'E5' and board1[24] == '   ':
    board1[24] = Fore.GREEN + ' X ' + Style.RESET_ALL
    i += 1
  else:
    print ()
    print ("Invalid choice. Please choose again.")

print ()
print ("Great! This how your ocean grid looks like:")
print_board(board1)

#Make opponents' board through randomization

i=0
while i<5:
  opp_battleship = random.randint(0,24)
  
  if board2[opp_battleship] == '   ':
    board2[opp_battleship] = ' X '
    i += 1

#Game start
time.sleep(5)
print ()
print (Fore.RED + "***** " + Fore.WHITE + "Game Start" + Fore.RED + " *****")
time.sleep(1)
print ()
print ("Get ready to battle!")
print ()
time.sleep(1)
print ("Your ocean grid:")
print_board(board1)
print ()
print ("Your opponent's ocean grid:")
print_board(board3)

#Function for user's turn to guess location

def user_turn():
  #Ask for location
  while True:
    print ()
    print ("Where do you want to shoot?")
    shot = input(">")
    shot = shot.upper()
  
    #Convert choice to index
    if shot == 'A1':
      shot_ind = 0
    elif shot == 'A2':
      shot_ind = 1
    elif shot == 'A3':
      shot_ind = 2
    elif shot == 'A4':
      shot_ind = 3
    elif shot == 'A5':
      shot_ind = 4
    elif shot == 'B1':
      shot_ind = 5
    elif shot == 'B2':
      shot_ind = 6
    elif shot == 'B3':
      shot_ind = 7
    elif shot == 'B4':
      shot_ind = 8
    elif shot == 'B5':
      shot_ind = 9
    elif shot == 'C1':
      shot_ind = 10
    elif shot == 'C2':
      shot_ind = 11
    elif shot == 'C3':
      shot_ind = 12
    elif shot == 'C4':
      shot_ind = 13
    elif shot == 'C5':
      shot_ind = 14
    elif shot == 'D1':
      shot_ind = 15
    elif shot == 'D2':
      shot_ind = 16
    elif shot == 'D3':
      shot_ind = 17
    elif shot == 'D4':
      shot_ind = 18
    elif shot == 'D5':
      shot_ind = 19
    elif shot == 'E1':
      shot_ind = 20
    elif shot == 'E2':
      shot_ind = 21
    elif shot == 'E3':
      shot_ind = 22
    elif shot == 'E4':
      shot_ind = 23
    elif shot == 'E5':
      shot_ind = 24
    else:
      shot_ind = 999
    
    #Determine if it's a hit or miss and mark on grid
    if shot_ind not in range (0,25):
      print ()
      print ("Your choice is out of range, please choose again.")
    else:
      if board2[shot_ind] == ' X ' and board3[shot_ind] == '   ':
        print ()
        print ("It's a hit! You sank one of your opponent's battleship.")
        board3[shot_ind] = Fore.YELLOW + ' X ' + Style.RESET_ALL
        return True
      elif board2 [shot_ind] == ' X ' and board3[shot_ind] == Fore.YELLOW + ' X ' + Style.RESET_ALL:
        print ()
        print ("You have attacked this spot before, please choose again.")
      elif board3[shot_ind] == ' - ':
        print ()
        print ("You have attacked this spot before, please choose again.")
      else:
        print ()
        print ("It's a miss! Try again later.")
        board3[shot_ind] = ' - '
        return False

#Function for computer's turn to guess location
def computer_turn():
  while True:
    #Generate a random location index
    opp_shot_ind = random.randint(0,24)

    #Determine if it's a hit or miss and mark on grid
    if board1[opp_shot_ind] == Fore.GREEN + ' X ' +Style.RESET_ALL:
      print ()
      print ("Your opponent hit one of your ship! It has sunk!")
      board1[opp_shot_ind] = Fore.BLUE + ' S ' + Style.RESET_ALL
      return True
    elif board1[opp_shot_ind] == '   ':
      print ()
      print ("Your opponent missed!")
      board1[opp_shot_ind] = ' - '
      return False

#Taking turns to play game

while True:
  if user_turn():
    opp_num_ship = opp_num_ship -1
  time.sleep(1)
  if computer_turn():
    num_ship = num_ship - 1
  time.sleep(1)
  print ()
  print (Fore.RED + "***** " + Fore.WHITE + "Situation Update" + Fore.RED + " *****")
  print ()
  print ("Your ocean grid:")
  print_board(board1)
  print ()
  print ("Your opponent's ocean grid:")
  print_board(board3)
  print()
  time.sleep(2)

  #Winner determination
  if num_ship == 0 and opp_num_ship >0:
    print ("All your battleships have sunk.")
    print ()
    print (Fore.YELLOW + "*****YOU LOSE*****")
    break
  elif opp_num_ship == 0 and num_ship >0: 
    print ("You have sunk all of your opponent's battleships!")
    print ()
    print (Fore.YELLOW + "*****YOU WIN*****")
    break
  elif num_ship == 0 and opp_num_ship == 0:
    print ("All of your battleships have sunk at the same time.")
    print ()
    print (Fore.YELLO + "*****IT'S A TIE*****")




