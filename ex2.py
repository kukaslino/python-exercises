name = input("Digite uma palavra: ")

if name == name[::-1]:
    print(name, "é um palíndromo.")
else:
    print(name, "não é um palíndromo.")
