from limparTexto import limparTexto

# Código para cifrar

def cifrarVigenere(texto, chave):
    # usa a função para limpar textos da atividade 1
    texto = texto.lower()
    texto_limpo = limparTexto(texto)
    
    chave = chave.lower()
    chave_limpa = limparTexto(chave)
    
    tamanho_chave = len(chave_limpa)
    texto_criptografado = []
    indice_chave = 0
    
    alfabeto = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
        "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
        "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
        "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25
    }
    
    # dicionario inverso para achar a letra pelo número (ex.: 0 -> a)
    numero_para_letra = {v: k for k, v in alfabeto.items()}

    for char in texto_limpo:
        valor_original = alfabeto[char]

        # 1. Pega a letra da chave e o valor numérico dela
        posicao_senha = indice_chave % tamanho_chave
        letra_chave = chave_limpa[posicao_senha]
        valor_senha = alfabeto[letra_chave]

        # 2. Calcula a nova posição 
        nova_posicao = (valor_original + valor_senha) % 26

        # 3. Converte a nova posição de volta para letra
        nova_letra = numero_para_letra[nova_posicao]
        texto_criptografado.append(nova_letra)
            
        indice_chave += 1
                    
    return "".join(texto_criptografado)

# teste 1 - saída esperada: MQYRREJPQYPSWUSUXGACOEZIAVQ 
print(cifrarVigenere("you really know how to make me cry", "ocean eyes"))

# teste 2 - saída esperada: DNKVEADQGNRWWTYWJ
print(cifrarVigenere("luke, i am your father", "star wars")) 

# Código para decifrar

def decifrarVigenere(texto, chave):
    texto = texto.lower()
    chave = chave.lower()
    chave_limpa = limparTexto(chave)
        
    tamanho_chave = len(chave_limpa)
    texto_criptografado = []
    indice_chave = 0
        
    alfabeto = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
        "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
        "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
        "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25
    }
        
    # dicionario inverso para achar a letra pelo número (ex.: 0 -> a)
    numero_para_letra = {v: k for k, v in alfabeto.items()}
    
    for char in texto:
        valor_original = alfabeto[char]
    
        # 1. Pega a letra da chave e o valor numérico dela
        posicao_senha = indice_chave % tamanho_chave
        letra_chave = chave_limpa[posicao_senha]
        valor_senha = alfabeto[letra_chave]
    
        # 2. Calcula a nova posição, mas ao invés de somar, subtrai para decifrar
        nova_posicao = (valor_original - valor_senha) % 26
    
        # 3. Converte a nova posição de volta para letra
        nova_letra = numero_para_letra[nova_posicao]
        texto_criptografado.append(nova_letra)
                
        indice_chave += 1
                        
    return "".join(texto_criptografado)

# teste 1 - saída esperada: youreallyknowhowtomakemecry
print(decifrarVigenere("MQYRREJPQYPSWUSUXGACOEZIAVQ", "ocean eyes"))

# teste 2 - saída esperada: lukeiamyourfather
print(decifrarVigenere("DNKVEADQGNRWWTYWJ", "star wars"))