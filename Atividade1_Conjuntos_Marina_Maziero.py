#Aluna: Marina Althoff Maziero

#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas.

#Transformando cada linha do txt em um elemento do vetor:
with open("EX1.txt","r") as text:
    txt = text.readline()
    txt = [x.rstrip('\n') for x in text]

#Criando contadores
tamanho = len(txt)/3
cont = 1

#Laço para realizar as operações:
while (tamanho > 0):

    #vetores são reescritos a cada volta do laço
    vet1 = txt[cont].split(", ")
    vet2 = txt[cont+1].split(", ")
    vet3 = []

    #união:
    if (txt[cont-1] == "U" or txt[cont-1] == "u"):

        for i in range(0,len(vet1)):
            vet3.append(vet1[i])

        for i in range(0,len(vet2)):
            vet3.append(vet2[i])

        print("União: conjunto 1 ",vet1,", conjunto 2 ", vet2,". Resultado: ",vet3)

    #interseção:
    elif (txt[cont-1] == "I" or txt[cont-1] == "i"):

        for i in range (0,len(vet1)):

            for n in range (0,len(vet2)):

                if (vet1[i] == vet2[n]):
                    vet3.append(vet1[i])

        print("Interseção: conjunto 1 ",vet1, ", conjunto 2 ",vet2,". Resultado: ",vet3)

    #diferença:
    elif (txt[cont-1] == "D" or txt[cont-1] == "d"):

        for i in range (0,len(vet1)):

           if (vet1[i] not in vet2):
               vet3.append(vet1[i])

        for i in range (0,len(vet2)):

            if (vet2[i] not in vet1):
                vet3.append(vet2[i])

        print("Diferença: conjunto 1 ",vet1,", conjunto 2 ",vet2,". Resultado: ",vet3)

    #produto cartesiano:
    elif (txt[cont-1] == "C" or txt[cont-1] == "c"):

        for i in range (0,len(vet1)):

            for n in range (0,len(vet2)):

                if (vet1[i] != vet2[n]):
                    vet3.append((vet1[i],vet2[n]))

        print("Produto cartesiano: conjunto 1 ",vet1,", conjunto 2 ",vet2,". Resultado: ",vet3)


    tamanho = tamanho - 1
    cont = cont + 3