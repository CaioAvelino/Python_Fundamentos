# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

option = int(input("\n\nSelecione o número da operação desejada: \n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite sua opção (1/2/3/4): "))
primeiro = int(input("\n\nDigite o primeiro número: "))
segundo = int(input("\n\nDigite o segundo número: "))

if(option not in [1,2,3,4] or (option == 4 and segundo == 0)):
    print("\n\nOpção inválida!")
elif(option == 1):
    soma = primeiro + segundo
    print("\n\nSoma: %d + %d = %d" %(primeiro, segundo, soma))
elif(option == 2):
    sub = primeiro - segundo
    print("\n\nSubtração: %d - %d = %d" %(primeiro, segundo, sub))
elif(option == 3):
    mult = primeiro * segundo
    print("\n\nMultiplicação: %d * %d = %d" %(primeiro, segundo, mult))
elif(option == 4 and segundo != 0):
    div = float(primeiro / segundo)
    print("\n\nDivisão: %d / %d = %f" %(primeiro, segundo, div))
 
