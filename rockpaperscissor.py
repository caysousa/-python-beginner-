import random

user_points = 0
computer_points = 0

options = ["r", "t", "p"]

while True:
    user_choice = input ('Escolha R (Pedra) / T (Tesoura) / P (Papel) ou Q para sair: ').lower()

    if user_choice == 'q':
        break
    if user_choice not in options:
        continue

    computer_choice = random.randint (0,2)
    # 0 = pedra 1 = tesoura e 2 = papel
    computer_option = options [computer_choice]

    print ('A escolha do computador foi: ' + computer_option)

    if user_choice == computer_option:
        print ('É um empate!')

    elif user_choice  == 'r' and computer_option == 't':
        print ('Você ganhou!')
        user_points = user_points + 1

    elif user_choice  == 'p' and computer_option == 'r':
        print ('Você ganhou!')
        user_points = user_points + 1

    elif user_choice  == 't' and computer_option == 'p':
        print ('Você ganhou!')
        user_points = user_points + 1
    

    else:
        print ('Poxa! Você perdeu!')
        computer_points = computer_points + 1

print ('Sua pontução é: ' + str (user_points))
print ('Essa é a pontuação do computador: ' + str (computer_points))

if computer_points > user_points:
    print ('Você foi derrotado!')
elif computer_points == user_points:
    print ('Foi um empate!')
else:
    print ('Você ganhou!')


