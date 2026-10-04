# REGAS: Se o jogador tiver 1 ou 2 cartas, ele deve comprar mais cartas, se tiver 3 ou mais cartas, ele pode escolher se quer comprar mais cartas ou não. O objetivo do jogo é chegar o mais próximo possível de 21 sem ultrapassar esse valor. Se o jogador ultrapassar 21, ele perde automaticamente. O dealer deve comprar cartas até atingir pelo menos 17 pontos. Se o dealer ultrapassar 21, todos os jogadores que ainda estiverem no jogo ganham. Se o dealer não ultrapassar 21, o jogador com a pontuação mais próxima de 21 vence.

import random

def main():
    print("\nO dealer irá entregar 2 cartas para você e 2 cartas para ele.")
    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(baralho) # Embaralha o baralho

    # 2 cartas para o jogador e 2 cartas para o dealer ----------------------------------------
    jogador_cartas = [baralho.pop(), baralho.pop()]
    dealer_cartas = [baralho.pop(), baralho.pop()]
    print(f"Suas cartas: {jogador_cartas} = {sum(jogador_cartas)}, cartas do dealer: {dealer_cartas} = {sum(dealer_cartas)}")
    # -----------------------------------------------------------------------------------------

    # Fazer o dealer comprar cartas se ele tiver menos de 17 pontos
    while sum(dealer_cartas) < 17:
        dealer_cartas += [baralho.pop()]

    while sum(jogador_cartas) < 21:
        outra_carta = input("Deseja outra carta? (y/n): ")

        if outra_carta == "y":
            jogador_cartas.append(baralho.pop())
            print(f"Suas cartas: {jogador_cartas} = {sum(jogador_cartas)}")

        elif outra_carta == "n":
            break

    # Depois que você parar de comprar, o dealer joga
    while sum(dealer_cartas) < 17:
        dealer_cartas.append(baralho.pop())

    # Então a rodada é resolvida
    print(f"Suas cartas: {jogador_cartas} = {sum(jogador_cartas)}")
    print(f"Cartas do dealer: {dealer_cartas} = {sum(dealer_cartas)}")

    if sum(jogador_cartas) > 21:
        print("Você perdeu! Sua pontuação ultrapassou 21.")
    elif sum(dealer_cartas) > 21:
        print("O dealer ultrapassou 21! Você ganhou!")
    elif sum(jogador_cartas) > sum(dealer_cartas):
        print("Você ganhou!")
    elif sum(jogador_cartas) == sum(dealer_cartas):
        print("Empate!")
    else:
        print("O dealer ganhou!")


print("\nBem-vindo ao jogo de Blackjack!")
jogar = input("Deseja jogar? (y/n):" )

if jogar == "n":
    print("\nTudo bem, obg!!!\n")
elif jogar == "y":
    main()