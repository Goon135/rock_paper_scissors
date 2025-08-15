import random

def choose_comp():
  return random.choice(['камень','ножницы','бумага'])

def choose_player():
  print('Введите камень/ножницы/бумага')
  while True:
    pl = input()
    pl = pl.lower()
    if pl == 'ножницы' or pl == 'камень' or pl == 'бумага':
      break
    else:  
      print('Возможно вы ошиблись при написании. Повторите попытку')
  return pl

def winer(comp, pl):
  a = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
  }
  if comp == pl:
      print( "ничья")
  for i, j in a.items():
    if comp == i and pl == j:
      print( "Вы проиграли :(")

    elif pl == i and comp == j:
      print( "Вы победили :)")

def play():
  print('Добро пожаловать в игру камень, ножницы, бумага')
  while True:
    player = choose_player()
    computer = choose_comp()
    winer(computer, player)
    a = input('Хотите ли вы продолжить игру? (+ для продолжения, - для выхода)\n')
    if a == '+':
      continue
    else:
      break

play()
