texto = ""
pares = []

# Função principal que verifica se os grafos são vizinhos e retorna seus pares e seu nível
def dfs(visitado, grafo, vertice, nivel, texto, pares):
    if vertice not in visitado:  # Verifica se o vertice ja foi visitado, caso não add ele no set
        visitado.add(vertice)
        for vizinho in grafo[vertice]:
            if(vizinho in visitado):
                aux = [vertice, vizinho]
                repitido = False
                # Verificação se osvértices são vizinhos
                for i in pares:
                    if(i == aux):
                        repitido = True
                if(repitido == False):
                    texto += ' '*nivel + \
                        str(vertice) + "-" + str(vizinho) + "\n"
            else:
                texto += ' '*nivel + str(vertice) + "-" + \
                    str(vizinho) + " pathR(G," + str(vizinho) + ")"+"\n"
                pares += [[vertice, vizinho]]
            texto = dfs(visitado, grafo, vizinho, nivel+2, texto, pares)
    # O texto retorna somente com os pares se for uma repetição de caminho
    return texto


casos = int(input())  # Quantidade de casos

# Recebimento dos input's e verificação de subgrafos
for cas in range(casos):
    pares = []
    n = input().split(" ")
    v = int(n[0])  # Numero de vertices
    e = int(n[1])  # Numero de arestas

    grafo = {}  # Definindo o grafo inicialmente vazio

    for i in range(v): #Alocação de espaço para os grafos
        grafo[i] = []

    for i in range(e):  # Construindo o grafo com as entrada
        m = input().split(" ")
        a = int(m[0])
        b = int(m[1])
        grafo[a].append(b)

    visitado = set()  # Set para todos os vertices visitados
    if(cas != 0):
        texto += "\n"

    texto += "Caso "+str(cas+1)+":"

    # Verifica se já foi percorrido todos os subgrafos
    for i in grafo:
        if(i not in visitado):  # para grafos desconexos
            cont = len(texto.splitlines())
            texto_temp = texto + "\n"
            for v in grafo:
                grafo[v].sort()
            texto_temp = dfs(visitado, grafo, i, 2, texto_temp, pares)
            cont2 = len(texto_temp.splitlines())
            if(cont2 > cont+1):
                texto = texto_temp
print(texto)
