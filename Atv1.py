#Tópico 1: Estruturas Condicionais (if / else)

#Exercício resolvido pelo Professor
#Problema: Crie um programa que pergunte a idade do usuário e imprima se ele é "Maior de idade"
#(18 anos ou mais) ou "Menor de idade".

#Resolução pelos Alunos
#Sua vez: Escreva um programa que peça ao usuário para digitar um número inteiro. O programa
#deve verificar e imprimir se o número é POSITIVO ou NEGATIVO (considere o zero como positivo
#para este exercício).

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade  ")
else:
    print("Menor de idade  ")
    
    
n = int(input("Digite um número inteiro: "))
if n >= 0:
    print("O número é POSITIVO")    
else:
    print("O número é NEGATIVO")