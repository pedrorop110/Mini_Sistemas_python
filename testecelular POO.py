# Criar a classe Celular com marca e bateria (começa em 100).
# Método usar(): tira 10 da bateria.
# Método carregar(): soma 20, sem passar de 100.
# Criar um celular, usar 2 vezes, carregar 1 vez e imprimir a bateria. Resultado esperado: 100.

class celular:
    def __init__(self, marca, bateria=100):
        self.marca = marca
        self.bateria = bateria


    def usar(self):
        self.bateria -= 10


    def carregar(self):
        self.bateria += 20
        if self.bateria > 100:
            self.bateria = 100

def main():
    MeuCelular = celular("IOS")
    MeuCelular.usar()
    MeuCelular.usar()
    MeuCelular.carregar()
    print(MeuCelular.bateria)

main()
