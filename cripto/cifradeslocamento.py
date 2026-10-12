from limparTexto import limparTexto

# dicionário do alfabeto
ALFABETO = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
    "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
    "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
    "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
    "y": 24, "z": 25
}

# dicionário inverso para converter números para letras
NUMERO_PARA_LETRA = {v: k for k, v in ALFABETO.items()}

# função para carregar os textos por arquivos .txt
def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo:
        return arquivo.read()

def cifraDeslocamento(texto, chave):
    # utiliza a função limparTexto criada nas atividades anteriores
    texto_limpo = limparTexto(texto)
    texto_criptografado = []
    
    for char in texto_limpo:
        posicao_atual = ALFABETO[char]
        nova_posicao = (posicao_atual + chave) % 26
        nova_letra = NUMERO_PARA_LETRA[nova_posicao]
        texto_criptografado.append(nova_letra)

    return "".join(texto_criptografado)


texto_original = carregar_arquivo('texto_original.txt')
print(cifraDeslocamento(texto_original, 7))