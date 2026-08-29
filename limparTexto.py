# separação dos caracteres especiais
caracteres_especiais = [",", ".", ";", ":", "!", "?", "_", "-", "+", "=", "@", "&", "/", "*"]
c_esp_A = ["á", "à", "ã", "ä", "â"]
c_esp_E = ["é", "è", "ẽ", "ë", "ê"]
c_esp_I = ["í", "ì", "ĩ", "ï", "î"]
c_esp_O = ["ó", "ò", "õ", "ö", "ô"]
c_esp_U = ["ú", "ù", "ũ", "ü", "û"]
c_esp_C = ["c"]


def limparTexto(mensagem_poluida):
    # para remover os espaços
    mensagem_poluida = mensagem_poluida.replace(" ", "")

    # para remover as letras acentuadas e caracteres especiais
    for char in mensagem_poluida:
        if char in caracteres_especiais:
            mensagem_poluida = mensagem_poluida.replace(char, "")
        elif char in c_esp_A:
            mensagem_poluida = mensagem_poluida.replace(char, "a")
        elif char in c_esp_E:
            mensagem_poluida = mensagem_poluida.replace(char, "e")
        elif char in c_esp_I:
            mensagem_poluida = mensagem_poluida.replace(char, "i")
        elif char in c_esp_O:
            mensagem_poluida = mensagem_poluida.replace(char, "o")
        elif char in c_esp_U:
            mensagem_poluida = mensagem_poluida.replace(char, "u")
        elif char in c_esp_C:
            mensagem_poluida = mensagem_poluida.replace(char, "c")

    # para remover os números
    lista_mensagem = list(map(str, mensagem_poluida))
    for char in lista_mensagem:
        if char.isnumeric():
            lista_mensagem.remove(char)

    mensagem_limpa = "".join(lista_mensagem)
    return mensagem_limpa

# mensagens testes
mensagem_teste1 = "Mas há front2eiras no5s jar8dins da razão"
mensagem_teste2 = "E3ssá lua cheìa 9traz u_m sentim7ento"

mensagem = input().lower()

print(limparTexto(mensagem))
