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

# if player_quantity != int():
#   print("O input precisa ser um número inteiro")
#   player_quantity = int(input("Quantidade de jogadores do jogo: "))
# elif player_quantity <= 1:
#   print("Não é possível jogar sozinho. Tente com alguém.")
#   player_quantity = int(input("Quantidade de jogadores do jogo: "))
# Pequisei inúmeras maneiras de conseguir diferenciar, vi o método type(), isinstance()... dava errado,
# então parti pra algo fora do escopo pedido na checklist

while True:
  try:
    player_quantity = int(input("Máximo de jogadores permitidos é 8, quantos irão jogar? : "))
    assert player_quantity > 1
    assert player_quantity < 9
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

# Estou pensando em poder deixar cada nome ser assignado
# print("Cada um dos jogadores foram assignados nomes númericos em ordem crescente.")
# print("Você deseja assignar nomes ou deixar os padrões? y/n :")

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
# GREEN_DICE = 'TPPCCC'
# YELLOW_DICE = 'TTPPCC'
# RED_DICE = 'TTTPPC'

# prefiro dessa maneira se não seria um inferno de ifs maior do que já é, espero que entenda prof.
GREEN_DICE = ['TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO', 'CÉREBRO', 'CÉREBRO']
YELLOW_DICE = ['TIRO', 'TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO', 'CÉREBRO']
RED_DICE = ['TIRO', 'TIRO', 'TIRO', 'PASSOS', 'PASSOS', 'CÉREBRO']
brain_count = 0
shot_count = 0
player_turn_iterator = 0

# função que quando chamada executa o jogo, ficou com muitas linhas pra uma função e num futuro posso corrigir isso
def start_game():

  global brain_count
  global shot_count

  green_dice_result = random.choice(GREEN_DICE)
  yellow_dice_result = random.choice(YELLOW_DICE)
  red_dice_result = random.choice(RED_DICE)

  print(f"-----------\nA vez é do: {player_scoreboard[player_turn_iterator][0]}\n-----------")

  roll_dices = random.sample(range(1, 14), 3)

  if roll_dices[0] <= 6:
    print(f"Você pegou um dado VERDE e rolou {green_dice_result}")
    if green_dice_result == "CÉREBRO":
      brain_count += 1
      print(f"Total de cérebros comidos: {brain_count}\n")
    elif green_dice_result == "TIRO": 
      shot_count += 1
      print(f"Total de tiros recebidos: {shot_count}\n")
    else:
      print("A vítima escapou!\n")

  elif roll_dices[0] >= 7 and roll_dices[0] <= 10:
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

# -=-=-=-=-=-=-=-=-=-=-=-=-

  if roll_dices[1] <= 6 :
    print(f"Você pegou um dado VERDE e rolou {green_dice_result}")
    if green_dice_result == "CÉREBRO":
      brain_count += 1
      print(f"Total de cérebros comidos: {brain_count}\n")
    elif green_dice_result == "TIRO": 
      shot_count += 1
      print(f"Total de tiros recebidos: {shot_count}\n")
    else:
      print("A vítima escapou!\n")

  elif roll_dices[1] >= 7 and roll_dices[0] <= 10:
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

# -=-=-=-=-=-=-=-=-=-=-=-=-

  if roll_dices[2] <= 6:
    print(f"Você pegou um dado VERDE e rolou {green_dice_result}")
    if green_dice_result == "CÉREBRO":
      brain_count += 1
      print(f"Total de cérebros comidos: {brain_count}\n")
    elif green_dice_result == "TIRO": 
      shot_count += 1
      print(f"Total de tiros recebidos: {shot_count}\n")
    else:
      print("A vítima escapou!\n")

  elif roll_dices[2] >= 7 and roll_dices[0] <= 10:
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

# Inicía o jogo
start_game()

while True:
  try:
    turn = input("Deseja [t]entar novamente, [p]assar o turno ou [f]inalizar o jogo? t/p/f :").lower()
    assert turn == "t" or turn =="p" or turn =="f"
    if turn == "p":
      # retira score de cérebros antigo, soma com a quantidade nova e checa o score para aviso de que perdeu ou ganhou
      old_score = player_scoreboard[player_turn_iterator].pop(1)
      player_scoreboard[player_turn_iterator].insert(1,  brain_count + old_score) 
      if player_scoreboard[player_turn_iterator][1] >= 13:
        print(f"Você venceu o jogo, {player_scoreboard[player_turn_iterator][0]}!!!!!!!!!!!!!!!!!!!!!\n")
        print(player_scoreboard)
        break
      # adiciona score de tiros novo
      old_score = player_scoreboard[player_turn_iterator].pop(2)
      player_scoreboard[player_turn_iterator].insert(2,  shot_count + old_score)

      if player_scoreboard[player_turn_iterator][2] >= 3:
        print(f"\n \n------ {player_scoreboard[player_turn_iterator][0]} ,você perdeu todos os pontos! ------\n \n")
        player_scoreboard[player_turn_iterator][1] = 0
        player_scoreboard[player_turn_iterator][2] = 0
      shot_count = 0
      brain_count = 0
      player_turn_iterator += 1
      print(f"Scoreboard: \n {player_scoreboard}")
      start_game()
    elif turn =="f":
      print(player_scoreboard)
      break
    else:
      print("\n---- Tentando novamente ----\n")
      print(player_scoreboard)
      start_game()
  except AssertionError:
    print("Somente tn/p são aceitos")
  except IndexError:
    player_turn_iterator = 0
    start_game()