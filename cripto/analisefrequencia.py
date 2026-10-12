from cifradeslocamento import carregar_arquivo

# Dicionário com a frequência percentual das letras no português
FREQUENCIA_LETRAS = {
    'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2,
    'f': 1.0, 'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4,
    'k': 0.1, 'l': 2.8, 'm': 4.2, 'n': 5.3, 'o': 10.8,
    'p': 2.9, 'q': 0.9, 'r': 6.9, 's': 7.9, 't': 4.9,
    'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3, 'y': 0.0, 'z': 0.4
}

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


def analiseFrequencia(texto_cifrado):
    melhor_chave = 0
    maior_pontuacao = -1
    total_letras = len(texto_cifrado)

    for chave in range(26):
        frequencias_cand = {letra: 0 for letra in FREQUENCIA_LETRAS.keys()}

        for char in texto_cifrado:
            posicao_atual = ALFABETO[char]

            nova_posicao = (posicao_atual - chave) % 26
            novo_char = NUMERO_PARA_LETRA[nova_posicao]
            
            frequencias_cand[novo_char] += 1

        # calcula as porcentagens para a chave atual
        porcentagens_cand = {}
        for letra, contagem in frequencias_cand.items():
            porcentagens_cand[letra] = (contagem / total_letras)

        # calcula a pontuacao de correlacao
        pontuacao = 0
        for letra, freq_esperada in FREQUENCIA_LETRAS.items():
            freq_encontrada = porcentagens_cand.get(letra, 0.0)
            pontuacao += freq_esperada * freq_encontrada

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_chave = chave

    return melhor_chave

texto_criptografado = carregar_arquivo('texto_criptografado.txt')
print(analiseFrequencia(texto_criptografado))