# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

tentativa = 0


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letter = None
        self.palavra_aux = []
        self.certas = []
        self.erradas = []
        self.todas_letras = []
        self.board = board
        self.tentativa = tentativa
        for self.i in self.word:
            self.palavra_aux.append('_')

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        if (self.letter in self.word) and (self.letter not in self.todas_letras):
            self.certas.append(self.letter)
            self.todas_letras.append(self.letter)
            for self.index, self.value in enumerate(self.word):
                if self.value == self.letter:
                    self.palavra_aux[self.index] = self.letter
            return True
        elif self.letter not in self.word and self.letter not in self.todas_letras:
            self.erradas.append(self.letter)
            self.tentativa += 1
            self.todas_letras.append(self.letter)
            return False
        else:
            self.todas_letras.append(self.letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.tentativa == 6 or self.hangman_won() is True:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.palavra_aux == list(self.word) and self.tentativa <= 6:
            return True
        else:
            return False

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print("%s\n" % self.board[self.tentativa])
        print('Palavra: ', end=' ')
        for self.i in self.palavra_aux:
            print(self.i, end=' ')
        print("\n\nLetras erradas:")
        for self.i in self.erradas:
            print("%c" % self.i)
        print("\nLetras corretas:")
        for self.i in self.certas:
            print("%c" % self.i)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip('\n')


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while game.hangman_over() is False:
        game.print_game_status()
        game.guess(input("\nDigite uma letra: "))
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won() is True:
        print('Parabéns! Você venceu!! :)')
    else:
        print('\nGame over! Você perdeu! :(')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você!\n')


# Executa o programa		
if __name__ == "__main__":
    main()
