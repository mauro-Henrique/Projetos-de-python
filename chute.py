import random

numero = random.randint(1,100)
i = int(input('chute um numero: '))
print(i)
if  i > numero:
    print('chute um numero mais baixo')
    print(f'o numero era {numero}')
elif i < numero:
    print('chute um numero mais alto')
    print(f'o numero era {numero}')
else:
    print('voce acertou')
