#DESAFIO:

#O desafio da sua equipe será a criação de um ranking dos restaurantes próximo ao endereço de entrega, por meio dos critérios de avaliação do restaurante e a menor distância.
#Analisando a figura extraída do site do iFood, que conta com seis restaurantes, o primeiro do ranking deveria ser o 
# - “Lamen Kazu”,seguido pelo “Mr. Pretzels” que está à frente do “Brigaderia”, pois dentre os restaurantes com nota 4.7, 
# ele tem a menor distância. Já o “We Coffee”, será o quarto colocado, seguido por “Amor aos Pedaços” e por último “O Mineiro”.

#A avaliação é o determinante para o ranking, ou seja, a maior avaliação ficará no topo da lista o desempate ocorrerá pela distância. Para resolver o desafio utilize apenas o conteúdo estudado durante a fase.

print('*********************************')
print('***Enterprise Connection-iFood***')
print('*********************************')

#Variável do tipo lista, contendo todos os restaurantes e suas características.
restaurantes = [['O Mineiro', 4.3, 'Brasileira', 1.7, '30-40 min', 'gratis'], ['Mr. Pritzels', 4.7, 'Lanches', 1.5, '30-40 min', 'R$ 4.99'],
                ['Lamen Kazu - Liberdade', 4.8, 'Japonesa', 0.7, '31-41 min', 'R$ 6.99'], ['Amor Aos Pedaços', 4.3, 'Doces e Bolos', 1.3, '46-56 min', 'R$ 5.99'],
                ['Amor Aos Pedaços', 4.3, 'Doces e Bolos', 1.2, '46-56 min', 'R$ 5.99'], ['Brigadeiro Shopping Paulista', 4.4, 'Doces e Bolos', 1.2, '41-51 min', 'R$ 5.99'],
                ['Mr. Pritzels', 4.7, 'Lanches', 1.3, '30-40 min', 'R$ 4.99'],
                ['We Coffee', 4.5, 'Cafeteria', 0.5, '45-55 min', 'R$ 4.49'],
                ['Brigadeiro Shopping Paulista', 4.7, 'Doces e Bolos', 1.2, '41-51 min', 'R$ 5.99'], ['We Coffee', 4.1, 'Cafeteria', 0.5, '45-55 min', 'R$ 4.49']]

print('\n')

#Informação solicitada pelo sistema que será preenchida pelo usuário
print('Você gostaria de escolher o restaurante por Nome(1), Nota(2), Distância(3) ou Categoria(4)?')

escolha = int(input('Digite a opção desejada?\n Resposta: '))

print('\n')

#Se o usuário digitar "1" ele está escolhendo ordenar a lista por nome. 
if escolha == 1:

    restaurantes.sort()#Ordenando a lista em ordem alfabética (considerando a posição [X][0]), usando o comando "sort"

    #Variaveis incrementais.
    indice1 = 0 #Alterar o índice de verificação
    indice2 = 1 #Alterar o índice de verificação
    contagem = 0 #Auxiliar para alteração dos índices
    
    for menor_distancia in restaurantes: #Repetição que será realizada de acordo com o tamanho da lista "restaurantes"

        while indice1 < len(restaurantes): #Repetição que será realizada enquanto a variável "indice1" for menor que o tamanho da lista "restaurantes"

            if indice2 == len(restaurantes): #A variável "indice2" terá seu valor zerado no momento que "indice2" for igual ao tamanho da lista "restaurantes"
                indice2 = 0

            #Se as notas forem iguais, distancia menor e os nomes dos restaurantes forem os mesmos.
            if restaurantes[indice1][1] == restaurantes[indice2][1] and restaurantes[indice1][3] < restaurantes[indice2][3] and restaurantes[indice1][0] == restaurantes[indice2][0]:

                #Se a condição for verdadeira:
                restaurantes.append(restaurantes[indice1]) #O valor contido na posição será [x] será adicionado ao final da lista
                restaurantes [indice1] = restaurantes[indice2] #A posição [X] irá assumir o valor da posição [Y]
                restaurantes [indice2] = restaurantes.pop() # A posição [y] irá assumir o valor X

            #Se a nota for maior e se os nomes forem os mesmos.
            elif restaurantes[indice1][1] > restaurantes[indice2][1] and restaurantes[indice1][0] == restaurantes[indice2][0]:

                #Se a condição for verdadeira:
                restaurantes.append(restaurantes[indice1]) #O valor contido na posição será [x] será adicionado ao final da lista
                restaurantes [indice1] = restaurantes[indice2] #A posição [X] irá assumir o valor da posição [Y]
                restaurantes [indice2] = restaurantes.pop() # A posição [y] irá assumir o valor X

            if indice2 < len(restaurantes):  #Enquanto o valor da variável "indice2" for menor que o tamanho da lista "restaurantes" ele será incrementado em 1
                indice2 = indice2 + 1
    
            contagem = contagem + 1 #Variável incremental para auxiliar no incremento da variável "indice1" em +1

            if contagem == len(restaurantes):  #A variável "indice1" só será incrementado em +1 quando a variável contagem tiver o mesmo valor que o tamanho da lista "restaurante"
                indice1 = indice1 + 1
                contagem = 0
    
    # A váriavel nome assume o valor da nova lista "nome_ordenado" e printa na tela a partir do comando de repetição "for".
    for nome in restaurantes:
        print('Restaurante: {}'.format(nome[0]))
        print('Nota: {}'.format(nome[1]))
        print('Distância: {}'.format(nome[3])),
        print('Categoria: {}'.format(nome[2]))
        print('Preço: {}'.format(nome[5]))
        print('*********************************')

#Se o usuário digitar "1" ele está escolhendo ordenar a lista por nota.
elif escolha == 2:

    linha = 0 #Variavel incremental, para alterar o indice de verificação da lista restaurante.

    for x in restaurantes: #Troca de posição entre o nome do restaurante e sua nota.

        troca_nome = restaurantes[linha][0] #Armazenando o valor nome da linha "X" dentro da variavel "troca_nome"
        troca_nota = restaurantes[linha][1] #Armazenando o valor nota da linha "X" dentro da variavel "troca_nota"

        restaurantes[linha][0] = troca_nota #Atribuindo na posição [X][0] o valor da variável troca_nota
        restaurantes[linha][1] = troca_nome #Atribuindo na posição [X][0] o valor da variável troca_nome

        #ANTES: ['O Mineiro', 4.3, 'Brasileira', 1.7, '30-40 min', 'gratis']
        #DEPOIS: ['4.3', 'O Mineiro', 'Brasileira', 1.7, '30-40 min', 'gratis']

        linha = linha + 1 #Somando "1" a variável  "linha"

    restaurantes.sort(reverse=True) #Usando o comando "sort + reverse = True" para ordenar em ordem crescente, usando a nota como base.

    linha = 0 #Zerando a variável incremental 

    for x in restaurantes: #Desfazendo a troca feita acima

        troca_nome = restaurantes[linha][1]
        troca_nota = restaurantes[linha][0]

        restaurantes[linha][1] = troca_nota
        restaurantes[linha][0] = troca_nome
        linha = linha + 1
    
        #ANTES: ['4.3', 'O Mineiro', 'Brasileira', 1.7, '30-40 min', 'gratis']
        #DEPOIS: ['O Mineiro', 4.3, 'Brasileira', 1.7, '30-40 min', 'gratis']

    #Variaveis incrementais.
    indice1 = 0 #Alterar o índice de verificação
    indice2 = 1 #Alterar o índice de verificação
    contagem = 0 #Auxiliar para alteração dos índices
    
    for nota_ordenata in restaurantes: #Repetição que será realizada de acordo com o tamanho da lista "restaurantes"

        while indice1 < len(restaurantes): #Repetição que será realizada enquanto a variável "indice1" for menor que o tamanho da lista "restaurantes"

            if indice2 == len(restaurantes): #A variável "indice2" terá seu valor zerado no momento que "indice2" for igual ao tamanho da lista "restaurantes"
                indice2 = 0

            #Verificando se as notas são iguais e se a distancia é menor, para usar como critério de desempate e ordenação
            if restaurantes[indice1][1] == restaurantes[indice2][1] and restaurantes[indice1][3] < restaurantes[indice2][3]:
                
                #Se a condição for verdadeira:
                restaurantes.append(restaurantes[indice1]) #O valor contido na posição será [x] será adicionado ao final da lista
                restaurantes [indice1] = restaurantes[indice2] #A posição [X] irá assumir o valor da posição [Y]
                restaurantes [indice2] = restaurantes.pop() # A posição [y] irá assumir o valor X

            if indice2 < len(restaurantes): #Enquanto o valor da variável "indice2" for menor que o tamanho da lista "restaurantes" ele será incrementado em 1
                indice2 = indice2 + 1
    
            contagem = contagem + 1 #Variável incremental para auxiliar no incremento da variável "indice1" em +1

            if contagem == len(restaurantes): #A variável "indice1" só será incrementado em +1 quando a variável contagem tiver o mesmo valor que o tamanho da lista "restaurante"
                indice1 = indice1 + 1
                contagem = 0

    for nota_ordenada in restaurantes:
        print('Restaurante: {}'.format(nota_ordenada[0]))
        print('Nota: {}'.format(nota_ordenada[1]))
        print('Distância: {}'.format(nota_ordenada[3])),
        print('Categoria: {}'.format(nota_ordenada[2]))
        print('Preço: {}'.format(nota_ordenada[5]))
        print('*********************************')

elif escolha == 3:

    linha = 0

    for x in restaurantes:

        troca_nome = restaurantes[linha][0]
        troca_distancia = restaurantes[linha][3]

        restaurantes[linha][0] = troca_distancia
        restaurantes[linha][3] = troca_nome
        linha = linha + 1

    restaurantes.sort()

    linha = 0

    for x in restaurantes:

        troca_nome = restaurantes[linha][3]
        troca_distancia = restaurantes[linha][0]
        
        restaurantes[linha][3] = troca_distancia
        restaurantes[linha][0] = troca_nome
        linha = linha + 1

    indice1 = 0
    indice2 = 1
    contagem = 0
    
    for menor_distancia in restaurantes:

        while indice1 < len(restaurantes):

            if indice2 == len(restaurantes):
                indice2 = 0

            if restaurantes[indice1][3] == restaurantes[indice2][3] and restaurantes[indice1][1] > restaurantes[indice2][1]:

                restaurantes.append(restaurantes[indice1])
                restaurantes [indice1] = restaurantes[indice2]
                restaurantes [indice2] = restaurantes.pop()

            if indice2 < len(restaurantes):
                indice2 = indice2 + 1
    
            contagem = contagem + 1 

            if contagem == len(restaurantes):
                indice1 = indice1 + 1
                contagem = 0

    for distancia in restaurantes:
        print('Restaurante: {}'.format(distancia[0]))
        print('Nota: {}'.format(distancia[1]))
        print('Distância: {}'.format(distancia[3])),
        print('Categoria: {}'.format(distancia[2]))
        print('Preço: {}'.format(distancia[5]))
        print('*********************************')

elif escolha == 4:

    linha = 0

    for x in restaurantes:

        troca_categoria = restaurantes[linha][2]
        troca_nome = restaurantes[linha][0]

        restaurantes[linha][0] = troca_categoria
        restaurantes[linha][2] = troca_nome
        linha = linha + 1

    restaurantes.sort()

    linha = 0

    for x in restaurantes:

        troca_categoria = restaurantes[linha][0]
        troca_nome = restaurantes[linha][2]

        restaurantes[linha][2] = troca_categoria
        restaurantes[linha][0] = troca_nome
        linha = linha + 1

    indice1 = 0
    indice2 = 1
    contagem = 0
    
    for menor_distancia in restaurantes:

        while indice1 < len(restaurantes):

            if indice2 == len(restaurantes):
                indice2 = 0

            if restaurantes[indice1][1] == restaurantes[indice2][1] and restaurantes[indice1][3] < restaurantes[indice2][3] and restaurantes[indice1][2] == restaurantes[indice2][2]:

                restaurantes.append(restaurantes[indice1])
                restaurantes [indice1] = restaurantes[indice2]
                restaurantes [indice2] = restaurantes.pop()

            elif restaurantes[indice1][1] > restaurantes[indice2][1] and restaurantes[indice1][2] == restaurantes[indice2][2]:

                restaurantes.append(restaurantes[indice1])
                restaurantes [indice1] = restaurantes[indice2]
                restaurantes [indice2] = restaurantes.pop()

            if indice2 < len(restaurantes):
                indice2 = indice2 + 1
    
            contagem = contagem + 1 

            if contagem == len(restaurantes):
                indice1 = indice1 + 1
                contagem = 0

    for categoria in restaurantes:
        print('Restaurante: {}'.format(categoria[0]))
        print('Nota: {}'.format(categoria[1]))
        print('Distância: {}'.format(categoria[3])),
        print('Categoria: {}'.format(categoria[2]))
        print('Preço: {}'.format(categoria[5]))
        print('*********************************')

else:
    print('Opção inválida!')