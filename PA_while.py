prim = int(input('Qual o primeiro termo? '))
raz = int(input('Qual a razão?'))
termo = prim
cont = 1
total = 0
rept = 10

while rept != 0:
    total += rept
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA')
    rept = int(input('Quantos termos a mais você deseja apresentar?'))
print('O número de termos que apareceram foi igual a {}'.format(total))