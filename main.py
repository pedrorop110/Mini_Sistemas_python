from banco import consultar_saldo as consultar_saldodb
from banco import criar_conta as criar_contadb
from banco import depositar as depositardb

def criar_conta():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    saldo = float(input("Saldo: "))

    criar_contadb(cpf, nome, idade, saldo)

def depositar():
    cpf = input("Digite seu CPF: ")

    conta = consultar_saldodb(cpf)
    if conta is None:
        print("Conta não encontrada.")
        return

    valor = float(input("Digite uma quantia para depositar: "))

    while valor <= 0:
        valor = float(input("Digite um valor maior que 0: "))

    linhas_atualizadas = depositardb(cpf, valor)
    if linhas_atualizadas == 0:
        print("Não foi possível concluir o depósito.")
        return

    print(f"R$ {valor:.2f} depositados com sucesso para {conta[0]}.")

def sacar(pessoas):
    busca = input("Digite seu CPF para sacar: ")
    encontrou = False

    for pessoa in pessoas:
        if busca == pessoa["CPF"]:
            encontrou = True
            print(f"\nUsuário encontrado = {pessoa['NOME']}")

            while True:
                sacar = int(input("Quanto deseja sacar?: "))

                if sacar <= 0:
                    print("Digite um valor maior que zero.")
                elif sacar > pessoa["SALDO"]:
                    print("Saldo insuficiente.")
                else:
                    break

            pessoa["SALDO"] -= sacar
            pessoa["HISTORICO"].append(f"Saque: {sacar}")
            print(f"R$ {sacar} sacados com sucesso!")

            break

    if not encontrou:
        print("Usuário não encontrado.")

def consultar_saldo():
    cpf = input("Digite o CPF: ")
    info = consultar_saldodb(cpf)

    if info is None:
        print("Conta não encontrada.")
    else:
        print(f"({info[0]}) possuí um saldo de R$ {info[1]:.2f}")

def ver_historico(pessoas):
    busca = input("Digite o CPF que deseja ver o historico: ")
    encontrou = False
    for pessoa in pessoas:
        if busca == pessoa["CPF"]:
            encontrou = True

            print(pessoa["HISTORICO"])

    if not encontrou:
        print("Usuario não encontrado.")

def main():

    pessoas = []
    escolha_do_usuario = 0

    while escolha_do_usuario != "6":
        print("\n===== BANCO =====")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar saldo")
        print("5 - Ver histórico")
        print("6 - Sair")
        escolha_do_usuario = input("\nEscolha: ")

        if escolha_do_usuario == "6":
            print("O usuario saiu.")
            break

        elif escolha_do_usuario == "1":
            criar_conta()

        elif escolha_do_usuario == "2":
            depositar()

        elif escolha_do_usuario == "3":
            sacar()

        elif escolha_do_usuario == "4":
            consultar_saldo()

        elif escolha_do_usuario == "5":
            ver_historico()

main()
