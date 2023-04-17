import random
import string

def gerar_senha_forte():
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = random.choice(caracteres)
    
    for i in range(8):
    
        senha += random.choice(caracteres)

    return senha

senha1 = gerar_senha_forte()
print(senha1)