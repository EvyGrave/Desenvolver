import threading
import time

# Mesmos dados da versão anterior
dados = list(range(10_000_000))
resultados_parciais = [0, 0]

def soma_parcial(sublista, indice):
    """
    Cada thread executa esta função.
    O 'indice' serve para salvar o valor no local correto da lista de resultados,
    evitando problemas de concorrência direta na mesma variável.
    """
    resultados_parciais[indice] = sum(sublista)

print("--- Execução Multithread (2 Threads) ---")
inicio = time.time()

# 1. DIVISÃO DA TAREFA: Dividindo a lista ao meio
meio = len(dados) // 2
parte1 = dados[:meio]
parte2 = dados[meio:]

# 2. CRIAÇÃO DE THREADS: Instanciando as threads para processar cada parte
t1 = threading.Thread(target=soma_parcial, args=(parte1, 0))
t2 = threading.Thread(target=soma_parcial, args=(parte2, 1))

# Iniciando a execução simultânea
t1.start()
t2.start()

# 3. SINCRONIZAÇÃO: O join() garante que o programa principal espere 
# as threads terminarem antes de prosseguir para o cálculo final.
t1.join()
t2.join()

# 4. COMPARTILHAMENTO DE RECURSOS: Somamos os valores que as threads 
# salvaram na lista compartilhada 'resultados_parciais'.
resultado_final = sum(resultados_parciais)

fim = time.time()
tempo_total_thread = fim - inicio

print(f"Resultado: {resultado_final}")
print(f"Tempo de execução: {tempo_total_thread:.4f} segundos")