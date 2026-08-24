mensagem_teste = "Mas há front2eiras no5s jar8dins da razão"
c_esp_A = ["á", "à", "ã", "ä"]
c_esp_E = ["é", "è", "ẽ", "ë"]
c_esp_I = ["í", "ì", "ĩ", "ï"]
c_esp_O = ["ó", "ò", "õ", "ö"]
c_esp_U = ["ú", "ù", "ũ", "ü"]
c_esp_Ç = ["c"]


def limparTexto(mensagem_teste):
    mensagem_teste = mensagem_teste.replace(" ", "") # para remover os espaços

    # para remover as letras acentuadas
    for char in mensagem_teste:
        if char in c_esp_A:
            mensagem_teste = mensagem_teste.replace(char, "a")
        elif char in c_esp_E:
            mensagem_teste = mensagem_teste.replace(char, "e")
        elif char in c_esp_I:
            mensagem_teste = mensagem_teste.replace(char, "i")
        elif char in c_esp_O:
            mensagem_teste = mensagem_teste.replace(char, "o")
        elif char in c_esp_U:
            mensagem_teste = mensagem_teste.replace(char, "u")
        elif char in c_esp_Ç:
            mensagem_teste = mensagem_teste.replace(char, "c")

    lista_mensagem = list(map(str, mensagem_teste))

    for char in lista_mensagem:
        # limpar números
        if char.isnumeric():
            lista_mensagem.remove(char)
    
    mensagem_limpa = "".join(lista_mensagem)        
    return mensagem_limpa


mensagem = input().lower()
print(limparTexto(mensagem))
