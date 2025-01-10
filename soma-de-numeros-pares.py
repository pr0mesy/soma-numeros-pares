print('Insira abaixo dois números inteiros, os quais representam o início e fim de um intervalo. ')

inicio = int(input('Início do intervalo: '))
fim = int(input('Fim do intervalo: '))

if inicio > fim:
    print('ERRO. O início do intervalo não pode ser maior que o fim.')
else:
    soma = 0

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

if soma > 0:
    print(f'A soma dos números pares no intervalo entre {inicio} e {fim} é {soma}. ')
else:
    print('Não há números pares no intervalo informado')