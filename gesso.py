def op1():
    prec = 35.00
    metro = float(input('metro do forro: '))
    valor = metro * prec
    print('o valor é R${:.2f}\n'.format(valor))
def op2():
    prec = 45.00
    metro = float(input('metro do forro: '))
    valor = metro * prec
    print('o valor é R${:.2f}\n'.format(valor))
def op3():
    prec = 65.00
    comp = float(input('comprimento da parede: '))
    alt = float(input('altura da parede: '))
    metro = comp * alt
    valor = metro * prec
    print('A parede de {:.2f} e o valor é R${:.2f}\n'.format(metro, valor))
def op4():
    op = int(input('1 - serviço ou 2 - material\n'))
    if op == 1:
        prec = 65.00
        metro = float(input('quantos metros: '))
        valor = metro * prec
        print('o valor é R${:.2f}\n'.format(valor))
    if op == 2:
        q = int(input('1- 3d de 25,00 ou 2 -3d de 35,00: '))
        if q == 1:
            prec = 25.00
            metro = float(input('quantos metros: \n'))
            valor = metro * prec
            print('o valor é R${:.2f}\n'.format(valor))
        if q == 2:
            prec = 35.00
            metro = float(input('quantos metros: \n'))
            valor = metro * prec
            print('o valor é R${:.2f}\n'.format(valor))
def op5():
    prec = 27.00
    metro = float(input('quantos metros: \n'))
    valor = metro * prec
    print('o valor é R${:.2f}\n'.format(valor))
def op6():
    print(''',
          forro plaquinha = R$35,00
forro acartonado = R$45,00
3d = R$25,00
revestimento = R$27,00
parede de acartunado = R$180,00
moldura = R$15,00
parede de bloco = R$65,00
          ''')
def opcao_padrao():
   print('invalido\n')
   
opcoes = {
    1: op1,
    2: op2,
    3: op3,
    4: op4,
    5: op5,
    6: op6
}

def exibir_menu():
    print('1- forro plaquinha\n2- forro acartunado\n3 - parede de bloco de gesso\n4 - 3d\n5 - revestimento\n6 - tabela de preço\n0 - sair')

while True:
    exibir_menu()
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 0:
        break
    
    opcoes.get(escolha, opcao_padrao)()