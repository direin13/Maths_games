#!/usr/bin/env python

import sys
from timeit import default_timer as timer
import random

class Results(object):

   def __init__(self, player, score):
      self.player = player
      self.score = score

   def player_result(self):
      return '\n{} score: {}/{}\n{}'.format(self.player, self.score[0], self.score[1] - 1, '-' * 30)

   def overall_result(self, other):
      if self.score == other.score:
         return 'Result: Draw'
      else:
         overall = {self.player: self.score[0],
                    other.player: other.score[0]}
         return '\nResult: Winner is {} - {} points'.format(max(overall.items(), key=high_value)[0], max(overall.items(), key=high_value)[1])

 
def high_value(t):
   return t[1]



def multiples_and_addition(max_time, player, difficulty, mode, insults, cpu_speed=1):
   
   print('\n---{} begin!---\n'.format(player))

   elapsed = timer()

   player_score = 0
   total = 1
   while timer() <= (max_time + elapsed):
      print('{}'.format('-' * 30))
      if player == 'CPU':
         cpu_clock = timer() 

      if mode == 'multiples':
         n1, n2 = random.randint(1, difficulty), random.randint(1, difficulty)
         expression = n1 * n2
         sign = 'x'

      if mode == 'additions':
         n1, n2 = (random.randint(1, difficulty) ** 2), (random.randint(1, difficulty) ** 2)
         expression = n1 + n2
         sign = '+'
      try:
         print('\n--Q{}: {} {} {} ='.format(total, n1, sign, n2))

         print("--Time left: {:0.1f}'s".format(-(timer() - elapsed - max_time)))

         if player == 'CPU':
            while timer() <= (cpu_speed + cpu_clock):
               pass
            answer = random.randint(expression, expression + cpu_speed)
            print(answer)

         else:
            answer = input()

         if int(answer) == expression:
            print('\n-correct-\n')
            player_score += 1

         else:
            print('{}. Answer = {}'.format(random.choice(insults), expression))
         total += 1
         print('{}'.format('\n' * 2))


      except:
         print('\ntype a number bro\n')

   return (player_score, total)

def hot_potatoe(player, difficulty, mode):
   pass

'-------------------------------------------------------------------------------------------------'


games = ['multiples', 'additions', 'hot potatoe']

insults = ['\n"stupid ass..."', '\n"retard"', '\n"you need help bruh"', '\n"yo mama shoulda swallowed you"', '\n"you make donald trump look smart"', '\n""', '\n"someone please help this dumbass nigga"', '\n"You as stupid as tunmise"']

#choosing you game -->
print('{}---Welcome!---\n\nEnter game: [multiples], [additions]\n'.format('\n' * 30))

choice = input()

while choice not in games:
   print('\n! Enter an actual game you fool\n')

   print('\nEnter game: [mutliples], [additions]\n')

   choice = input()

#Multiples -->
if choice == 'multiples' or choice == 'additions':
   print('\n---Welcome to {} vs---\n'.format(choice.capitalize()))

   print('\n--Would you like to play "2 player" or "cpu" mode?--\n\n2player = 1\n\nCpu = 2\n')

   game_mode = input()

   #2player mode -->
   if game_mode == '1':

      #Time allocated
      print('\n-Enter time limit (in seconds)-\n')

      max_time = -1

      try:
         max_time = float(input())
      except:
         print('\nsmh I already know your gonna struggle in this game...\n')
         while max_time < 0:
            print('\ntry again...\n')
            try:
               max_time = float(input())
            except:
               pass

      print('\n--Choose your difficulty--\n\nEasy = 1 (1-5 numbers)\n\nMedium = 2 (1-10 numbers)\n\nHard = 3 (1-20 numbers)')

      answer = input()

      if answer == '1':
         difficulty = 5

      if answer == '2':
         difficulty = 10

      if answer == '3':
         difficulty = 20

      print('\n\nPLAYER 1 press "enter" to begin\n')

      input()

      elapsed = timer()

      #PLAYER 1 -->

      game_on = multiples_and_addition(max_time, 'PLAYER 1', difficulty, choice, insults)

      p1 = Results('PLAYER 1', game_on)

      print("\n---Time's up!---")

      print(p1.player_result())

      #PLAYER 2 -->

      print('\n\nPLAYER 2 press "enter" to begin\n')

      input()

      elapsed = timer()

      game_on = multiples_and_addition(max_time, 'PLAYER 2', difficulty, choice, insults)

      p2 = Results('PLAYER 2', game_on)  

      print("\n---Time's up!---")
      print(p2.player_result())

      #overall winner
      print(p1.overall_result(p2))


   #Player vs cpu -->
   if game_mode == '2':
      print('\n--Choose your difficulty--\n\nEasy = 1 (1-5 numbers)\n\nMedium = 2 (1-10 numbers)\n\nHard = 3 (1-20 numbers)')

      answer = input()

      if answer == '1':
         difficulty = 5
         cpu_speed = 3

      if answer == '2':
         difficulty = 10
         cpu_speed = 2

      if answer == '3':
         difficulty = 20
         cpu_speed = 1

      print('\n\n--Enter time limit (in seconds)--\n')

      max_time = -1

      try:
         max_time = float(input())
      except:
         print('\nsmh I already know your gonna struggle in this game...\n')
         while max_time < 0:
            print('\ntry again...\n')
            try:
               max_time = float(input())
            except:
               pass

      #CPU -->

      elapsed = timer()

      game_on = multiples_and_addition(max_time, 'CPU', difficulty, choice, insults, cpu_speed)

      cpu_score = game_on[0]

      cpu = Results('CPU', game_on)

      print("\n---Time's up!---")
      print(cpu.player_result())

      print('\n\nP1 press enter to begin\n')

      input()

      #p1 -->

      game_on = multiples_and_addition(max_time, 'PLAYER 1', difficulty, choice, insults)

      p1 = Results('PLAYER 1', game_on)

      print("\n---Time's up!---")

      print(p1.player_result())

      #overall result
      print(p1.overall_result(cpu))
