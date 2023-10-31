import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

tesoura = ''' 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_imagens = [papel, pedra, tesoura]

print("************Pedra Papel e Tesoura*************")
print("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura")
jogador = int(input("Qual a sua jogada?\n "))
print(game_imagens[jogador])

cpu = random.randint(0,2)
print("Computador jogou:")
print(game_imagens[cpu])

if jogador >= 3 or jogador < 0:
    print("Voce digitou um numero invalido!. Voce perdeu.")  
elif jogador == 0 and cpu == 2:
    print("Voce ganhou!") 
elif cpu == 0 and jogador == 2:
    print("Voce perdeu!")
elif cpu > jogador:
    print("Voce perdeu!")
elif jogador > cpu:
    print("Voce ganhou!")
elif jogador == cpu:
    print("Empate!")
  