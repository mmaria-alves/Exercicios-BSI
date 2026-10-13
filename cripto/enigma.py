from cifradeslocamento import carregar_arquivo

ALFABETO = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
    "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
    "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
    "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25
}


# dicionário inverso para converter números para letras
NUMERO_PARA_LETRA = {v: k for k, v in ALFABETO.items()}

# 5 rotores fiação, letra de "notch" (que faz o rotor girar)
ROTORES = {
    1: ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    2: ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    3: ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    4: ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    5: ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
}

REFLETOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def passar_rotor(letra, fiacao, posicao, ida):
    entrada = (letra + posicao) % 26
    
    if ida:
        saida = ALFABETO[fiacao[entrada]]
    else:
        saida = fiacao.index(NUMERO_PARA_LETRA[entrada])
    
    return (saida - posicao) % 26

def cifraEnigma(texto, rotores, posicoes):
    # rotores[0] = esquerdo, rotores[1] = meio, rotores[2] = direito
    fiacoes = [ROTORES[r][0] for r in rotores]
    notches = [ALFABETO[ROTORES[r][1]] for r in rotores]
    posicao = [p - 1 for p in posicoes]

    resultado = []
    for char in texto.upper():
        if char not in ALFABETO:
            continue

        # 1. Giro dos rotores
        if posicao[1] == notches[1]:
            posicao[0] = (posicao[0] + 1) % 26
            posicao[1] = (posicao[1] + 1) % 26

        elif posicao[2] == notches[2]:
            posicao[1] = (posicao[1] + 1) % 26

        posicao[2] = (posicao[2] + 1) % 26

        # 2. Ida: da direita para a esquerda
        l = ALFABETO[char]
        for i in (2, 1, 0):
            l = passar_rotor(l, fiacoes[i], posicao[i], True)

        # 3. Refletor
        l = ALFABETO[REFLETOR[l]]

        # 4. volta: da esquerda para direita
        for i in (0, 1, 2):
            l = passar_rotor(l, fiacoes[i], posicao[i], False)

        resultado.append(NUMERO_PARA_LETRA[l])

    return "".join(resultado)



rotores = list(map(int, input("Rotores (3 números de 1 a 5, ex.: 1 2 3 ): ").split()))
posicoes = list(map(int, input("Posições iniciais (3 números de 1 a 26, ex.: 1 2 1): ").split()))
mensagem = carregar_arquivo('mensagem_secreta.txt')
    
print(cifraEnigma(mensagem, rotores, posicoes))