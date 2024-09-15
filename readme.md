# Conta Bancária - Projeto Python

Este é um projeto simples de sistema de conta bancária desenvolvido em Python. O sistema permite que um usuário faça depósitos, saques e visualize o extrato da conta. O código foi projetado para funcionar com um único usuário e não requer identificação de agência ou número da conta.

## Funcionalidades

- **Depositar**: Permite o depósito de valores positivos na conta. O sistema impede depósitos com valores negativos e atualiza o saldo e o extrato com o valor depositado.
- **Sacar**: Permite realizar até 3 saques diários com um limite máximo de R$ 500,00 por saque. O sistema verifica se o saldo é suficiente e se o limite de saques foi atingido antes de processar o saque.
- **Extrato**: Lista todos os depósitos e saques realizados. Exibe o saldo atual da conta no formato R$ xxx.xx.

## Como Usar

1. Interaja com o sistema através das opções disponíveis no menu:

    - `[d]` para Depositar
    - `[s]` para Sacar
    - `[e]` para Extrato
    - `[q]` para Sair

## Código

O código do projeto é dividido da seguinte maneira:

- **Depositar**: Adiciona um valor ao saldo da conta e o armazena no extrato.
- **Sacar**: Verifica se o valor do saque é permitido e realiza o saque, atualizando o saldo e o extrato.
- **Extrato**: Mostra uma lista de todas as operações realizadas e o saldo atual da conta.

## Exemplo de Uso

```plaintext
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> d
Deposito:
Qual valor voce quer depositar: 100
O valor do novo saldo é: 100 A quantidade de deposito foi: 1

=> s
Saque
Quanto voce quer sacar? 50
O novo saldo é 50

=> e
Extrato
Depósito: R$100.00
Saque: R$50.00
Saldo atual: R$50.00
