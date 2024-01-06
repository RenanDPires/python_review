from datetime import datetime
historico_transacoes = {}

saldo= 0
limite= 500
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    try:
        historico_transacoes[datetime.datetime.now()] = valor
        print(f'Depósito realizado em\t{historico_transacoes.keys()[-1]} \t no valor de {historico_transacoes.values()[-1]}')
    except:
        print('Para depósitos, apenas valores positivos são aceitos.')

while True:
    transacao= float(input('Informe a letra da transação desejada:\nd => Depósito\ns => Saque\ne => Extrato\n'))
    
    if transacao.upper() == 'D':
        valor = input('Informe quanto deseja depositar\n R$ ')
        deposito(valor)


