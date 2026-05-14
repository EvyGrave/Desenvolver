import time

# Criando uma lista de 10 milhões de números
dados = list(range(10_000_000))

def soma_sequencial(lista):
    total = 0
    for num in lista:
        total += num
    return total

print("--- Execução Sequencial ---")
inicio = time.time()

resultado = soma_sequencial(dados)

fim = time.time()
tempo_total = fim - inicio

print(f"Resultado: {resultado}")
print(f"Tempo de execução: {tempo_total:.4f} segundos\n")