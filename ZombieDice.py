import random
print('''
 ________                          __          _            ______      _                     
|  __   _|                        [  |        (_)          |_   _ `.   (_)                    
|_/  / /     .--.    _ .--..--.    | |.--.    __    .---.    | | `. \  __    .---.   .---.    
   .'.' _  / .'`\ \ [ `.-. .-. |   | '/'`\ \ [  |  / /__\\   | |  | | [  |  / /'`\] / /__\\   
 _/ /__/ | | \__. |  | | | | | |   |  \__/ |  | |  | \__.,  _| |_.' /  | |  | \__.  | \__.,   
|________|  '.__.'  [___||__||__] [__;.__.'  [___]  '.__.' |______.'  [___] '.___.'  '.__.'   
                                                                                            
''')
# usuário insere nome que é armazenado numa lista de jogadores junto com o placar inicial de pontuação ["Nome", cerebros, tiros]
player_scoreboard = [[input("Insira seu nick: "), 0, 0]]
while True:
  try:
    player_quantity = int(input("Máximo de jogadores permitidos é 8, quantos irão jogar? : "))
    assert player_quantity > 1
    assert player_quantity <= 8
    break
  except ValueError:
    print("Forneça um número inteiro!")
  except AssertionError:
    print("Não é possível jogar com esta quantidade de jogadores!")

for player in range(2, player_quantity + 1):
  player_scoreboard.insert(player,[f'Jogador{player}', 0, 0])

print("----- Total de Jogadores -----")
for iterator in range(0, player_quantity):
  print('\t', player_scoreboard[iterator][0])

print('''
Os dados sempre serão rolados automaticamente, mas a decisão de continuar ou não é sua!
-=-=-=-=-=-= Lista de Regras/Objetivos -=-=-=-=-=-=-=-=-=-=-=-=-=
1. Um jogador deve alcançar 13 cérebros comidos para vencer o jogo
2. A cada rodada, três dados aleatórios devem ser jogados randomicamente
  2.1 Caso um dos dados tenha caído numa pegada e o jogador continue rolando, você rola estes dados com pegadas com outros da caixa
3. Cada jogador pode decidir entre continuar jogando ou passar a vez
4. Três tiros de espingardas e você perde todos os cérebros(pontos)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
O jogo irá começar agora!
''')

# prefiro dessa maneira se não seria um inferno de ifs maior do que já é, espero que entenda prof.
GREEN_DICE = ['TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO', 'CÉREBRO', 'CÉREBRO']
YELLOW_DICE = ['TIRO', 'TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO', 'CÉREBRO']
RED_DICE = ['TIRO', 'TIRO', 'TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO']
brain_count = 0
shot_count = 0
player_turn_iterator = 0

# Checa a quantidade de pontos
def check_score():
  global shot_count
  global player_turn_iterator
  if shot_count >= 3 or player_scoreboard[player_turn_iterator][2] >= 3:
    print(f"\n------ {player_scoreboard[player_turn_iterator][0]} ,você levou muitos tiros e perdeu todos os pontos! ------")
    print(f"------ O turno foi passado automáticamente. ------ \n")
    player_scoreboard[player_turn_iterator][1] = 0
    player_scoreboard[player_turn_iterator][2] = 0
    player_turn_iterator += 1
    brain_count = 0
    shot_count = 0
    roll_dices()
  elif player_scoreboard[player_turn_iterator][1] >= 13:
    print(f"Você venceu o jogo, {player_scoreboard[player_turn_iterator][0]}!!!!!!!!!!!!!!!!!!!!!\n")
    print(f'Scoreboard: {player_scoreboard}\n')
    exit()

# Adiciona os pontos
def add_score():
  old_score = player_scoreboard[player_turn_iterator].pop(1)
  player_scoreboard[player_turn_iterator].insert(1,  brain_count + old_score) 
  
  old_score = player_scoreboard[player_turn_iterator].pop(2)
  player_scoreboard[player_turn_iterator].insert(2,  shot_count + old_score)

# Rola os dados
def roll_dices():
  global brain_count
  global shot_count
  dice_iterator = 0
  dice_box = random.sample(range(1, 14), 3)
  green_dice_result = random.choice(GREEN_DICE)
  yellow_dice_result = random.choice(YELLOW_DICE)
  red_dice_result = random.choice(RED_DICE)

  print(f"-----------\nA vez é do: {player_scoreboard[player_turn_iterator][0]}\n-----------")

  while dice_iterator < 3:
    if dice_box[dice_iterator] <= 6:
      print(f"Você pegou um dado VERDE e rolou {green_dice_result}")
      if green_dice_result == "CÉREBRO":
        brain_count += 1
        print(f"Total de cérebros comidos: {brain_count}\n")
      elif green_dice_result == "TIRO": 
        shot_count += 1
        print(f"Total de tiros recebidos: {shot_count}\n")
      else:
        print("A vítima escapou!\n")

    elif dice_box[dice_iterator] >= 7 and dice_box[dice_iterator] <= 10:
      print(f"Você pegou um dado AMARELO e rolou {yellow_dice_result}")
      if yellow_dice_result == "CÉREBRO":
        brain_count += 1
        print(f"Total de cérebros comidos: {brain_count}\n")
      elif yellow_dice_result == "TIRO": 
        shot_count += 1
        print(f"Total de tiros recebidos: {shot_count}\n")
      else:
        print("A vítima escapou!\n")

    else:
      print(f"Você pegou um dado VERMELHO e rolou {red_dice_result}")
      if red_dice_result == "CÉREBRO":
        brain_count += 1
        print(f"Total de cérebros comidos: {brain_count}\n")
      elif red_dice_result == "TIRO": 
        shot_count += 1
        print(f"Total de tiros recebidos: {shot_count}\n")
      else:
        print("A vítima escapou!\n")
    dice_iterator += 1

# função que quando chamada executa o jogo
def start_game():
  roll_dices()
  add_score()
  check_score()

# Inicía o jogo
start_game()

while True:
  try:
    turn = input("Deseja [t]entar novamente, [p]assar o turno ou [f]inalizar o jogo? t/p/f :").lower()
    assert turn == "t" or turn =="p" or turn =="f"
    # passa o turno
    if turn == "p":
      brain_count = 0
      shot_count = 0
      player_turn_iterator += 1
      print(f"\n Scoreboard:{player_scoreboard}")
      start_game()

    # finaliza jogo printando scoreboard final dos jogadores [f]
    elif turn =="f":
      print(f'\n Scoreboard: {player_scoreboard}\n')
      break

    # caso o player decida rolar os dados novamente [t]
    else:
      brain_count = 0
      shot_count = 0
      print("\n---- Tentando novamente ----")
      print(f"\n Scoreboard: {player_scoreboard}")
      start_game()     
  except AssertionError:
    print("Somente t/p/f são aceitos")
  except IndexError:
    player_turn_iterator = 0
    start_game()
