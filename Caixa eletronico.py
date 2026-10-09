import random

def criar_conta(pessoas):
    while True:
        cpf = input("Digite o CPF que deseja cadastrar: ")
        cpf_rep = False

        for pessoa in pessoas:
            if cpf == pessoa["CPF"]:
                cpf_rep = True
                break

        if cpf_rep:
            print("CPF já cadastrado, tente novamente.")
        else:
            nome = input("Nome: ")
            idade = input("Idade: ")
            dinheiro = random.uniform(1600, 20000)
            pessoa = {
                "NOME": nome,
                "IDADE": idade,
                "CPF": cpf,
                "SALDO": dinheiro,
                "HISTORICO": []
            }

            pessoas.append(pessoa)
            print("Pessoa cadastrada com sucesso!")
            break

def depositar(pessoas):
    busca = input("Digite seu CPF para depositar: ")
    encontrou = False

    for pessoa in pessoas:
        if busca == pessoa["CPF"]:
            encontrou = True
            print(f"\nUsuario encontrado = {pessoa['NOME']}")

            while True:
                despositar = int(input("Quanto deseja depositar?: "))

                if despositar <= 0:
                    print("Digite um valor maior que zero.")
                else:
                    break

            pessoa["SALDO"] += despositar
            pessoa["HISTORICO"].append(f"Depositar: {despositar}")

            print(f"{despositar} foi depositado com sucesso!")

    if not encontrou:
        print("Usuario não encontrado.")

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
        
def consultar_saldo(pessoas):
    consultar = input("Digite o CPF da pessoas para consultar seu saldo: ")

    for pessoa in pessoas:
        if consultar == pessoa["CPF"]:
            print(f"{pessoa['NOME']} possui um saldo de {pessoa['SALDO']}")

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
            criar_conta(pessoas)

        elif escolha_do_usuario == "2":
            depositar(pessoas)

        elif escolha_do_usuario == "3":
            sacar(pessoas)

        elif escolha_do_usuario == "4":
            consultar_saldo(pessoas)

        elif escolha_do_usuario == "5":
            ver_historico(pessoas)

main()