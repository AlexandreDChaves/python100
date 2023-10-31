print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Bem vindo a ilha do tesouro!")
print("Sua missão é descobrir o tesouro!")
caminho = input(
    "voce esta em uma encruzilhada entre dois caminhos, o da esquerda e o da direita. Esquerda ou direita?")

if caminho == "esquerda":
    rota = input("Caminhar para a floresta ou para a cidade?")

    if rota == "floresta":
        input("Voce encontrou uma onça! Você é um aventureiro que está viajando pela floresta para encontrar um tesouro perdido. Se você derrotar a onça, você estará um passo mais perto do tesouro.")
    elif rota == "cidade":
        input("Voce chegou a cidade! Você está cansado e precisa descansar. Você decide ficar na cidade por alguns dias para se recuperar.")

else:
    rota = input("Caminhar para o castelo ou voltar para casa?")

    if rota == "castelo":
        input("Voce chegou ao castelo! Você é um cavaleiro que está viajando para o castelo para desafiar o rei. Se você derrotar o rei, você salvará o reino.")
    elif rota == "casa":
        input("Voce voltou para casa! Voce está feliz por estar em casa, mas você sabe que tem mais aventuras pela frente.")
