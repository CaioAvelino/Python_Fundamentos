import random
f = open("palavras.txt", "rt")
bank = f.readlines()
palavra = bank[random.randint(0, len(bank))].strip('\n')
print(palavra)
'''string = []
cont = 0
for c in palavra:
    string.append(c)
    cont += 1
print(string)

if 'w' in palavra:
    print('Sim')
else:
    print("Não")
print(cont)
print(len(palavra))
#for i in palavra:
#    print('_', end = ' ')  '''
print(list(palavra))   
'''string[2] = "A"
print(string.index("A"))
print(string)
string1 = string
if string == string1:
    print("YES")'''

palavra_aux = ['-', '-','-', '-','-', '-']
letter = "a"
for i, j in enumerate(palavra):
    if j == letter:
        print(palavra[i])
        palavra_aux[i] = letter
print(palavra_aux)


