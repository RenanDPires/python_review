from datetime import datetime
historico_transacoes = []

saldo= 0
limite= 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    transacao= input('Informe a letra da transação desejada:\nd => Depósito\ns => Saque\ne => Extrato\n')
    
    if transacao.upper() == 'D':
        valor = float(input('Informe quanto deseja depositar\n R$ '))
        try:
            saldo = saldo + valor
            transacao_atual = [datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f"),valor]
            historico_transacoes.append(transacao_atual)
            print(f'Depósito realizado em\t{transacao_atual[0]} \t no valor de R$ {transacao_atual[1]:.2f}')
        
        except Exception as e:
            print('Para depósitos, apenas valores positivos são aceitos.\n',e)

    elif transacao.upper() == 'S':
        valor = float(input('Informe quanto deseja sacar\n R$ '))
        try:
            if (valor <= saldo) and numero_saques < 3 and valor <= 500:
                saldo = saldo - valor
                transacao_atual = [datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f"),-valor]
                historico_transacoes.append(transacao_atual)
                print(f'Saque realizado em\t{transacao_atual[0]} \t no valor de R$ {transacao_atual[1]:.2f}')

                numero_saques += 1
            elif numero_saques >= 3:
                print('Limite de saques diários excedido.')
            elif valor > 500:
                print('Valor de saques diários excedido.')
            else:
                print(f'Saldo inferior ao valor do saque.\n Saldo atual: R${saldo}')
        except Exception as e:
            print('Para depósitos, apenas valores positivos são aceitos.\n',e)

    elif transacao.upper() == 'E':
        for transacao in historico_transacoes:
            print(transacao[0],'\t',"{:.2f}".format(transacao[1]))
        print(f'Saldo final\tR$ {saldo:.2f}')
