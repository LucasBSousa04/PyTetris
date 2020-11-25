import pygame
import random



pygame.font.init()

#Tamanhos

largura_tela = 800
altura_tela = 700
largura_jogo = 300
altura_jogo = 600
tamanho_peca = 30

pos_x = (largura_tela - largura_jogo) // 2
pos_y = altura_tela - largura_jogo

#Formatos das peças

S = [['.....',
     '.....',
     '..00.',
     '.00..',
     '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
       '0000.',
       '.....',
       '.....',
       '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..00.',
       '..0..',
       '..0..',
       '.....'],
       ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
       ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..0..',
       '..0..',
       '..00.',
       '.....'],
      ['.....',
       '.....',
       '.000.',
       '.0...',
       '.....']
       ['.00..',
        '..0..',
        '..0..',
        '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
      ['.....',
       '..0..',
       '..00.',
       '..0..',
       '.....'],
       ['.....',
        '.000.',
        '..0..',
        '.....',
        '.....'],
       ['.....',
         '..0..',
         '.00..',
         '..0..',
         '.....']]
#cores
vermelho = (255, 0, 0)
roxo = (148, 0, 211)
azul_claro = (0, 191, 255)
azul_escuro = (0, 0, 255)
amarelo = (255, 255, 0)
rosa = (255, 20, 147)
verde = (0, 255, 0)

formatos = [S, Z, I, O, J, L, T]
cores_pecas = [vermelho, roxo, azul_claro, azul_escuro, amarelo, rosa, verde]

class Pecas(objeto):
    def __init__(self, x, y, formato):
        self.x = x
        self.y = y
        self.formato = formato
        self.cor = cores_pecas[formatos.index(formato)]
        self.rotation = 0
def


pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pytetris')

pygame.display.update()

pygame.quit()
