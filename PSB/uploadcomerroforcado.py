import time
import threading

CAPACIDADE_MAXIMA = 100
armazenamento_utilizado = 0

def fazerUpload(tamanho_arquivo):
    global armazenamento_utilizado
    if (tamanho_arquivo + armazenamento_utilizado) <= CAPACIDADE_MAXIMA:
        time.sleep(0.1)

        armazenamento_utilizado += tamanho_arquivo
        print(f"Armazenamento atual: {armazenamento_utilizado}")
    else:
        print("Capacidade máxima excedida.")

t1 = threading.Thread(target=fazerUpload, args=(70,))
t2 = threading.Thread(target=fazerUpload, args=(80,))

t1.start()
t2.start()

t1.join()
t2.join()