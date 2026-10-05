# SISTEMA DE CADASTRO. O programa deve funcionar através de um menu no terminal e permitir que o usuário cadastre, visualize, busque e remova pessoas.

# Cada pessoa cadastrada deve possuir nome, idade e CPF. Os dados devem ser armazenados em uma lista, permitindo que várias pessoas sejam cadastradas durante a execução do programa.
    
# O programa deve continuar mostrando o menu até que o usuário escolha a opção de sair.
# Ao escolher cadastrar, o programa deve pedir os dados da pessoa e adicioná-los à lista.
# Ao escolher listar, deve mostrar todas as pessoas já cadastradas e suas informações.
# Ao escolher buscar, deve pedir uma informação como nome ou CPF e procurar a pessoa correspondente.
# Ao escolher remover, deve pedir o CPF da pessoa e removê-la da lista, caso ela exista.
# O programa deve tratar situações como tentar buscar ou remover uma pessoa que não está cadastrada e tentar cadastrar um CPF que já existe.

# Organize o programa em funções para cada responsabilidade e mantenha o menu principal separado das funções que manipulam os dados. = cadastrar(), listar(), buscar(), remover(), main()

# ===== CADASTRO =====
# 1 - Cadastrar pessoa
# 2 - Listar pessoas
# 3 - Buscar pessoa
# 4 - Remover pessoa
# 5 - Sair

def cadastrar(pessoas):
    while True:
        cpf = input("CPF: ")

        cpf_rep = False

        for pessoa in pessoas:
            if cpf == pessoa["cpf"]:
                cpf_rep = True
                break

        if cpf_rep:
            print("CPF já cadastrado, tente novamente.")
        else:
            nome = input("Nome: ")
            idade = input("Idade: ")

            pessoa = {
                "nome": nome,
                "idade": idade,
                "cpf": cpf
            }

            pessoas.append(pessoa)
            print("Pessoa cadastrada com sucesso!")
            break

def listar(pessoas):
    # Para cada pessoa dentro de pessoas -> print(a pessoa)
    for pessoa in pessoas:
        print(pessoa)

def buscar(pessoas):
    #buscar uma pessoa especifica
    busca = input("Digite o nome ou CPF: ")
    encontrou = False   

    for pessoa in pessoas:
        if busca == pessoa["nome"] or busca == pessoa["cpf"]:
            print(pessoa)
            encontrou = True

    if not encontrou:
        print("Não foi possivel encontrar esta pessoa.")

def remover(pessoas):
    busca = input("Qual pessoa deseja remover? ( Digite o Nome ou CPF ): ")
    encontrou = False

    for pessoa in pessoas:
        if busca == pessoa["nome"] or busca == pessoa["cpf"]:
            pessoas.remove(pessoa)
            encontrou = True
            print(f"{pessoa['nome']} Foi removida(o).")
            break

    if not encontrou:
        print("Não foi possivel encontrar esta pessoa.")

def main():
    pessoas = [] # Armazena os dados das pessoas

    escolha_do_usuario = 0

    while escolha_do_usuario != "5":
        print("\n===== CADASTRO =====")
        print("1 - Cadastrar pessoa")
        print("2 - Listar pessoas")
        print("3 - Buscar pessoa")
        print("4 - Remover pessoa")
        print("5 - Sair")
        escolha_do_usuario = (input("\nEscolha: "))

        if escolha_do_usuario == "5":
            print("O usuario saiu.\n")
            break

        elif escolha_do_usuario == "1":
            cadastrar(pessoas)

        elif escolha_do_usuario == "2":
            listar(pessoas)

        elif escolha_do_usuario == "3":
            buscar(pessoas)

        elif escolha_do_usuario == "4":
            remover(pessoas)

main()