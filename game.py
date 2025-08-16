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
      return "Ничья"
  for i, j in a.items():
    if comp == i and pl == j:
      return "Вы проиграли :("

    elif pl == i and comp == j:
      return "Вы победили :)"

class ScoreBoard:
    def __init__(self, filename='scores.txt'):
        self.player_score = 0
        self.computer_score = 0
        self.filename = filename
        self.load_scores()  # Загружаем сохраненные результаты при инициализации

    def update_score(self, player_won):
        if player_won == 'Вы победили :)':
            self.player_score += 1
        elif player_won == 'Вы проиграли :(':
            self.computer_score += 1
        self.save_scores()  # Сохраняем результаты после обновления

    def display_score(self):
        print("\n=== ТЕКУЩИЙ СЧЕТ ===")
        print(f"Игрок: {self.player_score}")
        print(f"Компьютер: {self.computer_score}")
        print("===================\n")

    def save_scores(self):
        with open(self.filename, 'w') as file:
            file.write(f"{self.player_score},{self.computer_score}")

    def load_scores(self):
        try:
            with open(self.filename, 'r') as file:
                scores = file.read().split(',')
                self.player_score = int(scores[0])
                self.computer_score = int(scores[1])
        except FileNotFoundError:
            self.player_score = 0
            self.computer_score = 0
            self.save_scores()
        except Exception as e:
            print(f"Ошибка при загрузке счета: {e}")
            self.player_score = 0
            self.computer_score = 0

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.save_scores()


def play():
  q = ScoreBoard()
  print('Добро пожаловать в игру камень, ножницы, бумага')
  while True:
    player = choose_player()
    computer = choose_comp()
    res = winer(computer, player)
    print(res)
    q.update_score(res)
    q.display_score()
    a = input('Хотите ли вы продолжить игру? (+ для продолжения, - для выхода)\n')
    if a == '+':
      continue
    else:
      break

play()
