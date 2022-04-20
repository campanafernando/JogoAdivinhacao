import random
adv = int(input('Vamos ver se você consegue adivinhar o número que estou pensando de 1 até 5!\n'))
resp = random.randint(1, 5)
if adv == resp:
 print('Você acertou!')
else:
 print(f'Você errou... eu estava pensando no número {resp}!')