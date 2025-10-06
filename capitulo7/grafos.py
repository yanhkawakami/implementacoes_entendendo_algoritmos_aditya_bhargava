# Dijkstra
# Definição: Algoritmo para encontrar o caminho mais curto entre nós em um grafo ponderado.
# Aplicações: Navegação, roteamento de redes, jogos, planejamento de rotas.
# Respostas: o caminho mais curto e o custo associado entre dois nós.
# Estrutura de Dados Utilizada: Tabela de custos, tabela de pais, lista de nós processados.
# Tempo de execução: O((V + E) log V) onde V é o número de vértices e E é o número de arestas no grafo.

# Criando o grafo ponderado
grafo = {}
grafo["inicio"]  = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

print(grafo["inicio"].keys())  # dict_keys(['a', 'b'])
print(grafo["inicio"]["a"])  # 6
print(grafo["inicio"]["b"])  # 2

grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

# Inicializando a tabela de custos
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# Inicializando a tabela de pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# Lista de nós processados
processados = []