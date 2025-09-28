# Busca em Largura
# Definição: Algoritmo para percorrer ou buscar elementos em uma estrutura de dados em forma de grafo ou árvore, explorando todos os vizinhos de um nó antes de avançar para os próximos níveis.
# Aplicações: Encontrar o caminho mais curto em grafos não ponderados, redes sociais, jogos, inteligência artificial.
# Respostas: se há um caminho entre dois nós, o caminho mais curto em termos de número de arestas.
# Estrutura de Dados Utilizada: Fila (FIFO - First In, First Out).
# Tempo de execução: O(V + E) onde V é o número de vértices e E é o número de arestas no grafo.
from collections import deque
import grafos


def busca_largura():
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafos.grafo["voce"]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafos.grafo[pessoa]
                verificadas.append(pessoa)
    return False

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

busca_largura()