salario = 0
novo_salario = 0
porcentagem = 0

salario = float(input("Digite o salário atual: "))

# 20% ------------------------------------------------------------------------------
if salario <= 1000:
    porcentagem = 20
    novo_salario = salario + (salario * porcentagem / 100)

    print(f"Novo salario = {novo_salario:.2f}")
    novo_salario -= salario
    print(f"Aumento do salario = {novo_salario:.2f}")
    print(f"Porcentagem = {porcentagem} %")
#----------------------------------------------------------------------------------

# 15% ------------------------------------------------------------------------------
elif salario > 1000 and salario <= 3000:
    porcentagem = 15
    novo_salario = salario + (salario * porcentagem / 100)

    print(f"Novo salario = {novo_salario:.2f}")
    novo_salario -= salario
    print(f"Aumento do salario = {novo_salario:.2f}")
    print(f"Porcentagem = {porcentagem} %")
#----------------------------------------------------------------------------------

# 10% ------------------------------------------------------------------------------
elif salario > 3000 and salario <= 8000:
    porcentagem = 10
    novo_salario = salario + (salario * porcentagem / 100)

    print(f"Novo salario = {novo_salario:.2f}")
    novo_salario -= salario
    print(f"Aumento do salario = {novo_salario:.2f}")
    print(f"Porcentagem = {porcentagem} %")
#----------------------------------------------------------------------------------

# 5% ------------------------------------------------------------------------------
elif salario > 8000:
    porcentagem = 5
    novo_salario = salario + (salario * porcentagem / 100)

    print(f"Novo salario = {novo_salario:.2f}")
    novo_salario -= salario
    print(f"Aumento do salario = {novo_salario:.2f}")
    print(f"Porcentagem = {porcentagem} %")
#----------------------------------------------------------------------------------