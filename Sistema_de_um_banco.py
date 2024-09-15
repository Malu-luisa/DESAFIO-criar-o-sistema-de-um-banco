# Menu de opções do sistema
menu = '''
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=>'''

# Inicialização das variáveis
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo por saque
extrato = ''  # Extrato da conta, inicialmente vazio
numero_saques = 0  # Número de saques realizados
LIMITE_SAQUES = 3  # Limite diário de saques
quant_de_deposito = 0  # Quantidade total de depósitos realizados

while True:
    opcao = input(menu)  # Exibe o menu e recebe a opção do usuário

    if opcao == 'd':
        # Opção para depósito
        print('Depósito:')
        deposito = int(input('Qual valor você quer depositar: '))  # Recebe o valor a ser depositado
        
        if deposito <= 0: 
            print('Não é possível adicionar esse valor')  # Verifica se o valor é válido
        else:
            saldo += deposito  # Atualiza o saldo com o depósito
            quant_de_deposito += 1  # Incrementa a quantidade de depósitos
            print('O valor do novo saldo é:', saldo, 'A quantidade de depósitos foi:', quant_de_deposito)
            extrato += f"Depósito: R${deposito:.2f}\n"  # Adiciona o depósito ao extrato

    elif opcao == 's':
        # Opção para saque
        print('Saque')
        saque = int(input('Quanto você quer sacar?'))  # Recebe o valor a ser sacado

        if saque > saldo:
            print('Saldo insuficiente!!!')  # Verifica se há saldo suficiente
        elif numero_saques >= LIMITE_SAQUES:
            print('Você já atingiu o limite máximo de saques diários.')  # Verifica o limite de saques diários
        elif saque > limite:
            print('O valor excedeu o limite')  # Verifica o limite do valor do saque
        else:
            saldo -= saque  # Atualiza o saldo após o saque
            numero_saques += 1  # Incrementa o número de saques realizados
            extrato += f"Saque: R${saque:.2f}\n"  # Adiciona o saque ao extrato

    elif opcao == 'e':
        # Opção para visualizar o extrato
        print('Extrato')
        print(extrato)  # Exibe o extrato com todas as transações
        print(f"Saldo atual: R${saldo:.2f}")  # Exibe o saldo atual

    elif opcao == 'q':
        # Opção para sair do sistema
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada')  # Mensagem para opções inválidas
