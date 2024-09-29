def verificar_senha():
    senha_correta = "8526"
    tentativas = 3

    while tentativas > 0:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            return True
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Senha incorreta! Você tem {tentativas} tentativa(s) restantes.")
            else:
                print("Senha incorreta! Seu acesso foi bloqueado. Por favor, procure sua agência.")
                return False  # Retorna False se as tentativas se esgotarem

def main():
    if not verificar_senha():
        return

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Voce Depositou o valor de: ", valor)
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("\nSeu deposito no valor de:", valor, "foi bem Sucedido!")
                print("\nfoi bem Sucedido!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
