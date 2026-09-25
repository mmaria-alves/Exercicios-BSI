import time
import threading

CAPACIDADE_MAXIMA = 100
armazenamento_utilizado = 0

trava = threading.Lock()

def fazerUpload(tamanho_arquivo):
    global armazenamento_utilizado

    trava.acquire()

    if (armazenamento_utilizado + tamanho_arquivo) <= CAPACIDADE_MAXIMA:
        time.sleep(0.1)

        armazenamento_utilizado += tamanho_arquivo
        print(f"Armazenamento atual: {armazenamento_utilizado}")
    else:
        print("Capacidade máxima excedida!")

    trava.release()

t1 = threading.Thread(target=fazerUpload, args=(70,))
t2 = threading.Thread(target=fazerUpload, args=(80,))

t1.start()
t2.start()

t1.join()
t2.join() 