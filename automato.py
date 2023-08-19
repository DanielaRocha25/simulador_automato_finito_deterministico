import re
from numpy import append

def lerArquivo():
    arquivo = open('file.txt')
    automato = []
    for linha in arquivo:
        linha = linha.replace("\n", "")
        automato.append(linha)
    arquivo.close()
    return automato

def getEstadoInicial(automato):
    estadoInicial = automato[0]
    print('Estado inicial:',estadoInicial)
    return estadoInicial

def getAlfabeto(automato):
    alfabeto = re.split(" ", automato[1]) 
    alfabeto = set(alfabeto)
    print("Símbolos do alfabeto:",alfabeto)
    return alfabeto

def getEstados(automato):
    estados = re.split(" ", automato[2]) 
    print("Conjunto de Estados: ",estados)
    return estados

def getEstadosFinais(automato):
    estadoFinal = re.split(" ", automato[3])
    print("Estados finais",estadoFinal)
    return estadoFinal

def getTransicao(automato):
    transicoes = {}
    for i in range(4, len(automato)):
        items = automato[i].split(" ") 
        index = items[0] + " " + items[2] 
        transicoes[index] = items[1]
    print("Transições: ",transicoes)
    return transicoes

def checaPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra):
    validacao = False
    estadoAtual = estadoInicial
    for letra in palavra:
        if letra in alfabeto:
            estadoAtual = transicoes[estadoAtual + " " + letra]
        else:
            return -1
    if estadoAtual in estadosFinais:
        validacao = True
    return validacao

def validar(validacao, palavra):
    if validacao == True:
       print(f"A palavra {palavra} foi ACEITA")
    elif validacao == False:
        print(f"A palavra {palavra} foi REJEITADA")
    else:
        print("Erro")

def principal():
    automato = lerArquivo()
    estadoInicial = getEstadoInicial(automato)
    alfabeto = getAlfabeto(automato)
    estados = getEstados(automato)
    estadosFinais = getEstadosFinais(automato)
    transicoes = getTransicao(automato)
    palavra = input("Informe uma palavra: ")
    validacao =  checaPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra)
    validar(validacao, palavra)

principal()
