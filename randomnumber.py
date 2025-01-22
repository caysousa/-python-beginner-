import random

print ('Seja bem vindo ao "Guess the number!"')
choice_number = input('Digite o número teto do desafio: ')

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Erro: Valor informado não é númerico. Execute novamente e informe um número.')
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input('Adivinhe o número: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print('Erro: Valor informado não é númerico. Execute novamente e informe um número.')
        continue

    n_choices = 0 + 1
    if answer_user == random_number:
        print ('CORRETO!')
        break
    elif answer_user > random_number:
      print ('Alto demais! O numero é menor que esse!')
    else:
      print ('Baixo demais! O numero é maior que esse!')

print ('Numero de tentativas: ' + str(n_choices))
        