while True:
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

    if jogador1 == jogador2:
        print("Empate!")
    elif jogador1 == "pedra":
        if jogador2 == "tesoura":
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")
    else:
        print("Opção inválida. Tente novamente.")

    tryAgain = input("Quer jogar novamente? (sim ou nao): ")
    if tryAgain.lower() != "sim":
        break