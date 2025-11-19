# 📘 Global Solution – Dynamic Programming  
## Otimização de Portfólio de Projetos (0/1 Knapsack Problem)


## 👥 Integrantes do Grupo

- Pedro Henrique Mendes dos Santos – RM555332  
- Kayky Silva Stiliano – RM555148 ;;

---

# 📌 Sobre o Projeto

Este projeto implementa um sistema de **Otimização de Portfólio de Projetos**, inspirado no clássico **Problema da Mochila 0/1 (0/1 Knapsack Problem)**, utilizando quatro abordagens:

1. **Algoritmo Guloso (Greedy)**
2. **Recursão Pura**
3. **Programação Dinâmica Top-Down (Memoização)**
4. **Programação Dinâmica Bottom-Up (Iterativa)**

O objetivo é maximizar o **valor total entregável** dentro de uma capacidade limitada de **Horas-Especialista**, recurso crítico em consultorias e empresas de tecnologia.

---

# 🎯 Problema Proposto

Uma empresa de consultoria possui uma quantidade limitada de **Horas-Especialista** para o próximo trimestre. Cada projeto disponível exige um número de horas e entrega um valor estratégico ou financeiro.

Seu objetivo é selecionar os projetos que **maximizam o valor total**, sem exceder a capacidade total disponível.

---

## 📥 Dados de Exemplo

Capacidade total:  
```python
C = 10 horas-especialista
```


Projetos:

| Projeto | Valor (V) | Horas (E) |
|---------|-----------|------------|
| A       | 12        | 4          |
| B       | 10        | 3          |
| C       | 7         | 2          |
| D       | 4         | 3          |

---

# 🧠 Estratégias Implementadas

## 🟦 **Fase 1 – Estratégia Gulosa (Greedy)**  
Seleciona projetos com maior relação `Valor/Horas`.  
**Não garante solução ótima.** É usada para demonstrar a falha de heurísticas simples.

---

## 🟨 **Fase 2 – Solução Recursiva Pura**  
Implementa diretamente a fórmula recursiva:
```py
Max(i, c) = max(
Max(i-1, c), # não incluir
V[i] + Max(i-1, c - E[i]) # incluir
)
```
Não utiliza memoização, resultando em **repetição massiva de cálculos**.

---

## 🟩 **Fase 3 – Programação Dinâmica Top-Down (Memoização)**  
A mesma recursão da Fase 2, porém com armazenamento em cache:  
```py
memo[(i, c)]
```
Diminui a complexidade de exponencial para **O(n · C)**.

---

## 🟧 **Fase 4 – Programação Dinâmica Bottom-Up (Iterativa)**  
Constrói uma tabela:
```py
T[i][c] = melhor valor possível usando i projetos com capacidade c
```
É a forma mais eficiente e mais utilizada na prática para o Knapsack.

---

# 🧪 Casos de Teste

Testamos o sistema com os dados fornecidos e outros cenários adicionais.

### ✔ Resultado para o caso oficial da GS (C = 10):

| Abordagem | Valor Máximo Obtido |
|-----------|----------------------|
| Greedy    | Pode falhar (ex.: 29) |
| Recursiva | 29 |
| Memoização | 29 |
| Bottom-Up  | 29 |

---

## ⚠ Demonstração da falha do Greedy

Greedy seleciona pela razão **Valor/Horas (V/E)**.

Ordenação por V/E:
1. C = 3.5  
2. A = 3.0  
3. B = 3.33  
4. D = 1.33  

Greedy tende a pegar C → B → A, mas pode ficar sem incluir a combinação ótima.

> **Solução ótima:**  
C (7,2) + A (12,4) + B (10,3) = **29 valor, 9 horas**

Greedy, dependendo da ordem, pode escolher outra combinação subótima.

---

# ▶ Como Executar

### 📌 Pré-requisitos
- Python 3.8+
- Nenhuma biblioteca adicional

### 📥 Baixando os Arquivos
```bash
git clone https://github.com/pehenmendes/Global-Solution-2-Dynamic-Programming.git
```

### ▶️ Execução
```bash
python OtimizçãoDePortifolio.py
```
