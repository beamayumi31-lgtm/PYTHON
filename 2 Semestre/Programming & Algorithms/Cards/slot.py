import flet as ft

SLOT_WIDTH = 70  # mesmo tamanho da carta
SLOT_HEIGHT = 100


# Slot = lugar onde as cartas ficam. Container = caixa com borda e posição.
class Slot(ft.Container):

    # Cria o slot na posição (top, left)
    def __init__(self, solitaire, top, left, border):
        super().__init__()
        self.pile = []  # cartas dentro do slot
        self.width = SLOT_WIDTH
        self.height = SLOT_HEIGHT
        self.left = left  # posição X
        self.top = top  # posição Y
        self.border = border
        self.border_radius = ft.BorderRadius.all(6)
        self.solitaire = solitaire  # mesa do jogo
