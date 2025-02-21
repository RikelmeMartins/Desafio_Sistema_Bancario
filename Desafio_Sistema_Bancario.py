menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_de_saque = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Depositar")
        
        valor = float(input("Qual valor do deposito: "))
        if valor <= 0:   
            print("Valor invalido!")
            break
        else: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == 's':
        print("Sacar")

        if limite_de_saque > 0:
            valor = float(input("Qual valor do saque: "))
            if valor > limite:
                print("Valor invalido!")
                break
            else:
                if valor > saldo: 
                    print("Conta sem o valor necessario!")
                else:
                    saldo -= valor
                    limite_de_saque -= 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Limite de saque ultrapassado!")           

    elif opcao == 'e':

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 'q':
        print("Saindo...")
        break

    else:
        print("Opção invalida!")