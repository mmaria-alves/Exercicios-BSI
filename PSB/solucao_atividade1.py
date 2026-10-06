import os
import time
import threading

def funcao(valor_temp):
    global i

    for i in range(valor_temp):
        z = i * i

def calibrador():
    # valor temporário e só pra função iterar sobre
    amostra = 50_000_000

    start_time = time.time()
    funcao(amostra)
    duracao = (time.time() - start_time)

    # regra de três básica para gerar o n° aproximado de iteracoes
    return (amostra * 60 / duracao)

def alterar_prioridade(passo):
    tid = os.getpid()
    nice_atual = os.getpriority(os.PRIO_PROCESS, tid)
    novo_nice = max(-20, min(19, nice_atual + passo))

    try:
        os.setpriority(os.PRIO_PROCESS, tid, novo_nice)
        print("Alterando prioridade", flush=True)
        print(f"{nice_atual} -> {novo_nice}", flush=True)

    except PermissionError:
        print("Sem permissão.", flush=True)

def monitorar(total_iteracoes, inicio_execucao):
    while ativo:
        time.sleep(1)

        tempo_decorrido = time.time() - inicio_execucao

        progresso_real = i / total_iteracoes
        progresso_esperado = (time.time() - inicio_execucao) / 60.0

        diferenca = progresso_real - progresso_esperado

        nice_atual = os.getpriority(os.PRIO_PROCESS, tid)

        print(f"[{tempo_decorrido:.0f}s] progresso {progresso_real:.1%} | esperado {progresso_esperado:.1%} | nice: {nice_atual}", flush=True)

        # atrasado -> aumenta prioridade
        if diferenca < -0.01:
            alterar_prioridade(-1)
        # adiantado -> diminui prioridade
        elif diferenca > 0.01:
            alterar_prioridade(1)

i = 0
ativo = True
tid = os.getpid()
nice_inicial = os.getpriority(os.PRIO_PROCESS, tid)

print("Iniciando execução...", flush=True)
print(f"PID: {os.getpid()}")
print(f"TID: {threading.get_native_id()}")
print(f"Nice inicial: {nice_inicial}")

total_iteracoes = calibrador()
print(f"\nA função será executada {total_iteracoes:,} vezes em, aproximadamente, 60s")

inicio_execucao = time.time()
t1 = threading.Thread(target=monitorar, args=(total_iteracoes, inicio_execucao), daemon=True)
t1.start()

funcao(total_iteracoes)

ativo = False
t1.join()

nice_final = os.getpriority(os.PRIO_PROCESS, tid)
duracao = time.time() - inicio_execucao
print("\nExecução finalizada!")
print(f"Duração: {duracao:.2f}s")
print(f"Nice final: {nice_final}")