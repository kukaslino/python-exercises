import random

n = random.randint(1, 9)

while True:

    tent = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para encerrar o jogo): ")

    if tent.lower() == "sair":
        break

    if tent == n:
        print("Parabéns! Você acertou o número.")
        n = random.randint(1, 9)
    elif tent < n:
        print("O número é maior do que a sua tentativa.")
    else:
        print("O número é menor do que a sua tentativa.")