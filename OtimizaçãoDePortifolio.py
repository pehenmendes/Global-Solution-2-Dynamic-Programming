# =====================================================================
# Global Solution – Dynamic Programming
# Problema: Otimização de Portfólio de Projetos (0/1 Knapsack)
# Linguagem: Python
# Alunos: (coloque seu nome e RM aqui)
# =====================================================================

# ---------------------------------------------------------------------
# Dados de exemplo fornecidos no enunciado
# Cada projeto tem: Nome, Valor (V), Horas-Especialista (E)
# ---------------------------------------------------------------------

projects = [
    ("A", 12, 4),
    ("B", 10, 3),
    ("C", 7, 2),
    ("D", 4, 3)
]

CAPACITY = 10


# =====================================================================
# FASE 1 — Estratégia Gulosa (Greedy)
# ---------------------------------------------------------------------
# Regra utilizada:
#     Escolher os projetos com maior razão Valor/Horas (V/E)
# Observação:
#     A solução gulosa NÃO garante o valor ótimo — isso deve aparecer
#     em algum caso de teste.
# =====================================================================

def greedy_solution(projects, capacity):
    """
    Estratégia Gulosa para o problema.
    Seleciona projetos com maior V/E até esgotar a capacidade.

    Retorna:
        valor_total, lista_projetos_escolhidos
    """

    # Ordena pela razão V/E (valor por hora de especialista)
    sorted_projects = sorted(projects, key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0
    total_hours = 0
    chosen = []

    for name, value, hours in sorted_projects:
        if total_hours + hours <= capacity:
            chosen.append(name)
            total_value += value
            total_hours += hours

    return total_value, chosen



# =====================================================================
# FASE 2 — Solução Recursiva Pura
# ---------------------------------------------------------------------
# Implementação direta da fórmula recursiva:
#
# MaxValor(i, c) = max(
#       MaxValor(i-1, c),                                     (não inclui)
#       valor[i] + MaxValor(i-1, c - custo[i])                (inclui)
# )
#
# OBS:
#     Esta versão recalcula subproblemas várias vezes.
#     Complexidade: O(2^n)
# =====================================================================

def knapsack_recursive(i, capacity, projects):
    """
    Solução recursiva pura (sem memoização).
    i: índice do projeto atual (0-based)
    capacity: capacidade restante
    """

    # Caso base 1: sem capacidade restante
    if capacity <= 0:
        return 0

    # Caso base 2: sem projetos restantes
    if i < 0:
        return 0

    name, value, hours = projects[i]

    # Caso 1: não incluir o projeto atual
    option_without = knapsack_recursive(i - 1, capacity, projects)

    # Caso 2: incluir o projeto atual (se couber)
    if hours <= capacity:
        option_with = value + knapsack_recursive(i - 1, capacity - hours, projects)
    else:
        option_with = 0

    return max(option_with, option_without)



# =====================================================================
# FASE 3 — DP TOP-DOWN com Memoização
# ---------------------------------------------------------------------
# Mesma função recursiva da fase anterior, mas agora armazenamos
# resultados de subproblemas para evitar recomputações.
#
# Complexidade: O(n * C)
# =====================================================================

def knapsack_memoization(i, capacity, projects, memo):
    """
    Programação Dinâmica Top-Down (Memoization)
    Armazena resultados no dicionário memo[(i, capacity)].
    """

    # Caso base
    if capacity <= 0:
        return 0
    if i < 0:
        return 0

    # Verifica se já calculamos este subproblema
    if (i, capacity) in memo:
        return memo[(i, capacity)]

    name, value, hours = projects[i]

    # Opção sem incluir
    option_without = knapsack_memoization(i - 1, capacity, projects, memo)

    # Opção incluindo
    if hours <= capacity:
        option_with = value + knapsack_memoization(i - 1, capacity - hours, projects, memo)
    else:
        option_with = 0

    # Guarda o resultado no memo
    memo[(i, capacity)] = max(option_with, option_without)

    return memo[(i, capacity)]



# =====================================================================
# FASE 4 — Programação Dinâmica BOTTOM-UP (Iterativa)
# ---------------------------------------------------------------------
# Construção de uma tabela T onde:
#
# T[i][c] = melhor valor usando os primeiros i projetos com capacidade c
#
# i ∈ [0..N], c ∈ [0..CAPACITY]
#
# Complexidade: O(n * C)
# =====================================================================

def knapsack_bottom_up(projects, capacity):
    """
    DP Iterativa (Bottom-Up)
    Retorna o valor máximo que pode ser obtido.
    """

    n = len(projects)

    # Matriz DP com (n+1) linhas e (capacity+1) colunas
    T = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenche a tabela linha a linha
    for i in range(1, n + 1):

        name, value, hours = projects[i - 1]

        for c in range(1, capacity + 1):

            # Sem incluir o projeto
            option_without = T[i - 1][c]

            # Incluindo o projeto (se couber)
            if hours <= c:
                option_with = value + T[i - 1][c - hours]
            else:
                option_with = 0

            # Melhor das duas
            T[i][c] = max(option_with, option_without)

    return T[n][capacity]



# =====================================================================
# TESTES RÁPIDOS
# =====================================================================

if __name__ == "__main__":
    print("\n=== Fase 1 — Greedy ===")
    v, chosen = greedy_solution(projects, CAPACITY)
    print("Valor obtido:", v)
    print("Projetos escolhidos:", chosen)

    print("\n=== Fase 2 — Recursiva Pura ===")
    v = knapsack_recursive(len(projects) - 1, CAPACITY, projects)
    print("Valor máximo:", v)

    print("\n=== Fase 3 — Memoização ===")
    memo = {}
    v = knapsack_memoization(len(projects) - 1, CAPACITY, projects, memo)
    print("Valor máximo:", v)

    print("\n=== Fase 4 — Bottom-Up ===")
    v = knapsack_bottom_up(projects, CAPACITY)
    print("Valor máximo:", v)
