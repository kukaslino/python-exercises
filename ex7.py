with open('names.txt', 'r') as arquivo:
    nomes_contagem = {}
    linha = arquivo.readline()
    while linha:
        nome = linha.strip()
        if nome in nomes_contagem:
            nomes_contagem[nome] += 1
        else:
            nomes_contagem[nome] = 1
        linha = arquivo.readline()
    
    for nome, contagem in nomes_contagem.items():
        print(f'{nome}: {contagem}')
