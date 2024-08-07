#lista
cobras = ['Sucuri','Piton','Mamba Negra','Naja']

#exibir lista original
for cobra in cobras:
    print(cobra)

#usuario informa o nome da nova cobra
nova_cobra = input('\nInforme o nome da nova cobra: ')

#inserir a nova cobra na lista
cobras.append(nova_cobra)

#ele vai inserir o nome da nova variavel na cobra
#append é para inserir um novo item no final da lista, sempre no final****
#lista pode ser pilha ou fila
#pilha é empilhar o dado em cima do outro, o ultimo item que entrou é o primeiro que sai
#fila: o ultimo que entrou é ultimo que sai

#exibe a nova lista
for cobra in cobras:
    print(cobra)

#ordenar lista
cobras.sort()
print('\nLista em ordem alfabetica:\n')
#ordena a lista

#exibe a lista ordenada
for cobra in cobras:
    print(cobra)
