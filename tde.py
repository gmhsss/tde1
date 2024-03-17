# Nome completo: Rafaella Guerra Marinel Hurtado Somoza

# Define a função (formata) para formatar um conjunto como uma string entre as ""
def formata(s):
    return "{" + ", ".join(str(e) for e in s) + "}"

# Define a função para calcular(calcula_operacao) e imprime o resultado 
def calcula_operacao(operacao, A, B):
    # Verifica o tipo de operação (se é: U, I, D, C) e calcula o resultado
    if operacao == "U":
        resultado = set(A) | set(B)  # União de A e B
        print(f"União: conjunto 1 {formata(set(A))}, conjunto 2 {formata(set(B))}. Resultado: {formata(resultado)}")
    elif operacao == "I":
        resultado = set(A) & set(B)  # Interseção de A e B
        print(f"Interseção: conjunto 1 {formata(set(A))}, conjunto 2 {formata(set(B))}. Resultado: {formata(resultado)}")
    elif operacao == "D":
        resultado = set(A) - set(B)  # Diferença de A e B
        print(f"Diferença: conjunto 1 {formata(set(A))}, conjunto 2 {formata(set(B))}. Resultado: {formata(resultado)}")
    elif operacao == "C":
        resultado = [(a, b) for a in A for b in B]  # Produto cartesiano de A e B
        print(f"Produto Cartesiano: conjunto 1 {formata(set(A))}, conjunto 2 {formata(set(B))}. Resultado: {resultado}")

# Lendo o arquivo em modo leitura
with open('output.txt', 'r') as arquivo:
    num_operacoes = int(arquivo.readline().strip())  # Lê o número de operações do arquivo

    # Para cada operação no arquivo, lê os conjuntos A e B e calcula a operação
    for _ in range(num_operacoes):
        operacao = arquivo.readline().strip()  # Lê a operação (U, I, D, C)
        A = arquivo.readline().strip().split(', ')  # Lê o conjunto A como uma lista de elementos
        B = arquivo.readline().strip().split(', ')  # Lê o conjunto B como uma lista de elementos

        calcula_operacao(operacao, A, B)  # Chama a função(calcula_operacao) para calcular a operação
