INF = 1000000

# Este código é uma variação do código de Prim, porém nela não foi necessária a utilização do elemento "pai"
# Função de busca do menor caminho
def shortest_path(graph, the_tree, part_of_the_tree):
    shortest_path = INF

    # Será utlizada uma matriz para verificação, então são chamadas as linhas e colunas com um valor negativo,
    #  para ser incrementado
    line_helper = -1
    column = -1

    # Criação da matriz de incidência, verificando o menor caminho
    for line in the_tree:
        for reading in graph[line]:
            if (graph[line][reading] < shortest_path and (not part_of_the_tree[reading])):
                shortest_path = graph[line][reading]
                column = reading
                line_helper = line

    
    part_of_the_tree[column] = True
    the_tree.append(column)

    # A matriz criada é deletada para evitar muito uso de memória
    del graph[column][line_helper]
    del graph[line_helper][column]
    return(shortest_path)

# Execução principal
# Criação de um input geral
data = input()
run = True

while run:
    try:
        # Leitura dos vértices e arestas, podendo ser lidas em uma mesma linha, devido ao 'split'
        reading_v, reading_e = data.split(' ')
        vertices = int(reading_v)
        edges = int(reading_e)

        # Criação do Grafo e da Árvore
        graph = {i: {} for i in range(vertices)}
        in_the_tree = [False for i in range(vertices)]
        the_tree = [0]

        # Processamento dos valores na matriz, adicionando os respectivos 'pesos', que neste caso
        # são os valores para a contrução dos caminhos, que tembem podem ser recebidos na mesma linha
        for reading in range(edges):
            line, column, weight = input().split(' ')
            line = int(line) - 1
            column = int(column) - 1
            weight = int(weight)
            # Atribuição dos pesos ao Grafo
            graph[line][column] = weight
            graph[column][line] = weight
        
        # Eliminação por grafo desconexo
        if(edges < vertices-1):
            print('impossivel')

        # Calculo do caminho minimo usando a função de busca
        else:
            weight_value_found = 0
            for i in range(vertices-1):
                peso = shortest_path(graph, the_tree, in_the_tree)
                weight_value_found += peso
            
            print(weight_value_found)

        # Atualização do caso de teste
        data = input()
        
    # Inserção de uma exceção para que o programa possa ser finalizado
    except EOFError:
        run = False