'''
Grupo:
    Gabriel Bernardo            201611485
    Gabriela Rodrigues Zacarias 201820932
    Lucas de Carvalho Felizardo 201810087

Algoritmo:
    BFS - Busca em Largura

Funcionamento:
        Foi escolhido o algoritmo de BDF pois ele percorre o grafo em níveis a partir
    de um vértice inicial.
    
        A ideia foi a de percorrer todo o labirinto e quando encotramos um '.' execu-
    tamos a BFS a partir deste vértice, a maior distância será o ultimo nível possível.
    Comparamos a distância achada com a maior distâcia já encontrada em outros vértices,
    caso seja maior, atualizados a maior distância no labirinto. O programa termina
    quando já realizamos a busca em largura em todos os vértces do labirinto/grafo.
'''


labirintos = []
maiorDist = 0

def PRINCIPAL():
    lerLabirintos() # Entrada de dados

    for labirinto in labirintos: # Para todos os labririntos do problema
        maiorDist = 0
        numLinhas = len(labirinto)
        numColunas = len(labirinto[0])

        # Percorre todo o labirinto, caso o vertice seja '.' realiza a busca em largura
        for i in range(numLinhas):
            for j in range(numLinhas):
                if(labirinto[i][j] == '.'):
                    labirinto, distancia = BFS(labirinto, numLinhas, numColunas, (i,j))
                    if maiorDist < distancia:
                        maiorDist = distancia
        print(maiorDist)


def lerLabirintos(): # Entrada de dados
    N, M = map(int, input().split())
    while N != 0 and M != 0:
        labirinto = []
        
        for i in range(N):
            linha = input()
            labirinto.append(linha)
        
        labirintos.append(labirinto)
        N, M = map(int, input().split())


# BFS alterada para pegar a maior distância 
def BFS(labirinto, numLinhas, numColunas, pos):
    lin, col = pos
    numLinhas = len(labirinto)
    numColunas = len(labirinto)

    cor = []
    dist = []
    pai = []
    for i in range(numLinhas): # Inicializa as listas auxiliares
        linhaCor = ['B' for j in range(numColunas)]
        linhaDist = [-1 for j in range(numColunas)]
        linhaPai = [-1 for j in range(numColunas)]
        cor.append(linhaCor)
        dist.append(linhaDist)
        pai.append(linhaPai)

# Define as características do vertice atual
    cor[lin][col] = 'B'
    dist[lin][col] = 0
    
    distancia = 0

    Q = []
    Q.append(pos)

    while(Q != []):
        posicao = Q.pop(0)
        l, c = posicao

    # Verfica os vizinhos(caminhos) posíveis
        '''
        Validação do vizinho:
        - Não está na estremidade do labirinto
        - O possível vizinho é '.'
        - Ainda não percorreu o caminho, ou seja, é 'B'
        '''
        cima = (l > 0) and (labirinto[l-1][c] == '.') and (cor[l-1][c] == 'B') 
        baixo = (l < len(labirinto)-1) and (labirinto[l+1][c] == '.') and (cor[l+1][c] == 'B')
        esq = (c > 0) and (labirinto[l][c-1] == '.') and (cor[l][c-1] == 'B')
        dir = (c < len(labirinto[0])-1) and (labirinto[l][c+1] == '.') and (cor[l][c+1] == 'B')

    # Adiciona o vizinho a fila Q caso seja um caminho possível e define suas características                                                                      
        if cima:
            if(cor[l-1][c] == 'B'):
                cor[l-1][c] = 'C'
                dist[l-1][c] = dist[l][c] + 1
                if dist[l-1][c] > distancia:
                    distancia = dist[l-1][c]
                Q.append((l-1,c))
        if baixo:
            if(cor[l+1][c] == 'B'):
                cor[l+1][c] = 'C'
                dist[l+1][c] = dist[l][c] + 1
                if dist[l+1][c] > distancia:
                    distancia = dist[l+1][c]
                Q.append((l+1,c))
        if esq:
            if(cor[l][c-1] == 'B'):
                cor[l][c-1] = 'C'
                dist[l][c-1] = dist[l][c] + 1
                if dist[l][c-1] > distancia:
                    distancia = dist[l][c-1]
                Q.append((l,c-1))
        if dir:
            if(cor[l][c+1] == 'B'):
                cor[l][c+1] = 'C'
                dist[l][c+1] = dist[l][c] + 1
                if dist[l][c+1] > distancia:
                    distancia = dist[l][c+1]
                Q.append((l,c+1))

    # Fecha o vértice atual
        cor[l][c] = 'P'

    return (labirinto, distancia)

PRINCIPAL()