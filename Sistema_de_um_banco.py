menu = '''

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair



=>'''

saldo = 0 
limite = 500
extrato = ''
numero_saques = 0 
LIMITE_SAQUES = 3

quant_de_deposito = 0 

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Deposito:')
        deposito = (int(input('Qual valor voce quer depositar: ')))
        if deposito <= 0: 
            print('Não é possivel adicionar esse valor')
        else:
            saldo += deposito
            quant_de_deposito +=1 
            print('O valor do novo saldo é:', saldo ,'A quantidade de deposito foi:', quant_de_deposito )
            extrato += f"Depósito: R${deposito:.2f}\n"

    elif opcao == 's':  
        print('Saque')
        saque = int(input('Quanto voce quer sacar?'))


        if saque > saldo : 
            print('Saldo insuficiente!!!')

        elif numero_saques >= LIMITE_SAQUES:
            print('Você já atingiu o limite máximo de saques diários.')
        

        elif saque > limite:
            print('O valor excedeu o limite')
            
        else: 
            saldo -= saque 
            numero_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
    elif opcao == 'e':
        print('Extrato')
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada')