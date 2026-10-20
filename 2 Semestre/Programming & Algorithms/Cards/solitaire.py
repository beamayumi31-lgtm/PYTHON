import flet as ft

from card import Card
from slot import Slot

SOLITAIRE_WIDTH = 1000  # largura da mesa
SOLITAIRE_HEIGHT = 500  # altura da mesa


# Mesa do jogo. Stack = permite posicionar cada item por top/left, um sobre o outro.
class Solitaire(ft.Stack):

    # Cria a mesa vazia
    def __init__(self):
        super().__init__()
        self.controls = []  # tudo que aparece na mesa
        self.slots = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    # Roda sozinho quando a mesa entra na página; só então dá pra montar o jogo
    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    # Cria as 3 cartas do BTS (imagens em assets/images)
    def create_card_deck(self):
        self.cards = [
            Card(self, imagem="/images/bts_jimin.svg"),
            Card(self, imagem="/images/bts_v.svg"),
            Card(self, imagem="/images/bts_jin.svg"),
        ]

    # Cria os 2 slots: esquerda e direita
    def create_slots(self):
        self.slots.append(Slot(self, top=100, left=100, border=ft.Border.all(1)))  # esquerda
        self.slots.append(Slot(self, top=100, left=400, border=ft.Border.all(1)))  # direita
        self.controls.extend(self.slots)
        self.update()

    # Põe as cartas na mesa, todas no slot da esquerda
    def deal_cards(self):
        self.controls.extend(self.cards)
        for card in self.cards:
            card.place(self.slots[0])
        self.update()
