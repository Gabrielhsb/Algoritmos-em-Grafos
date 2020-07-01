##########################################

# Gabriel Bernardo 201611485
# Gabriela Rodrigues Zacarias 201820932
# Lucas de Carvalho Felizardo 201810087

#########################################

# Para a resolução deste exercício foi escolhida a busca em profundidade 
# Foi escolhido o DFS pois é uma maneira de verificar se há continuidade entre os vértices,
# além de permitir o teste de ambos os lados, voltando e fazendo a verificação, lendo
# todos os vértices de um lado, e depois novamente para o outro lado, retornando a
# maior sequência encontrada.


grafo = {} # {K:[u, v , cor]}
           #Sendo k a chave de cada dominó,
           #U e V os lados do dominó
           

# Função para fazer a busca em profundidade 
# e assim encontrar a maior sequência possivel
def percorrer(k): 
    global tamSequencia  
    tamSequencia += 1
    grafo[k][2] = 'P' #Marco como preto para saber que aquele domino ja foi usado
                      #Todos os que ja foram percorridos são marcados
    
    # Para cada peça do domino eu testo: 
    # Primeiro: se é braco (Não visitado) 
    # depois, comparo com todas as peças o lado direito da peça(K)  
    # e em seguida faço o mesmo com o lado esquerdo
    for i in grafo:
         if grafo[i][2] == 'B':
             if grafo[i][0] == grafo[k][0]:
                 percorrer(i)
             elif grafo[i][0] == grafo[k][1]:
                 percorrer(i)
             elif grafo[i][1] == grafo[k][0]:
                  percorrer(i)
             elif grafo[i][1] == grafo[k][0]:
                  percorrer(i)



#While criado para programa rodar até achar um final de arquivo
while True:
    try:
        numDominos = int(input()) 
        grafo = {}

        #Cria o grafo com as entradas dadas pelo usuario
        for i in range(numDominos):
            a, b = map(int, input().split())
            grafo[i] = [a,b,"B"]
            
        maior = 0

        # Para cada peça do dominó chamo a função percorrer
        for k in grafo: 
            tamSequencia = 0
            percorrer(k)
            if tamSequencia > maior:
                maior = tamSequencia

        #Por fim printa a maior sequencia possivel
        print(maior)
    except EOFError:
        break