import flet as ft

CARD_WIDTH = 70  # largura da carta
CARD_HEIGHT = 100  # altura da carta
CARD_OFFSET = 20  # espaço entre cartas empilhadas no mesmo slot
DROP_PROXIMITY = 30  # distância máxima pra carta encaixar no slot


# Carta. GestureDetector = controle que detecta o mouse (arrastar e soltar).
class Card(ft.GestureDetector):

    # Cria a carta, liga os eventos de arraste e coloca a imagem
    def __init__(self, solitaire, imagem):
        super().__init__()
        self.mouse_cursor = ft.MouseCursor.MOVE  # cursor de "mover"
        self.drag_interval = 5  # atualiza o arraste a cada 5 ms
        self.on_pan_start = self.start_drag  # começou a arrastar
        self.on_pan_update = self.drag  # arrastando
        self.on_pan_end = self.drop  # soltou
        self.left = None  # posição X na mesa (definida no place)
        self.top = None  # posição Y na mesa (definida no place)
        self.solitaire = solitaire  # mesa do jogo
        self.slot = None  # slot onde a carta está
        self.draggable_pile = [self]  # cartas que se movem no arraste
        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            border_radius=ft.BorderRadius.all(6),
            content=ft.Image(src=imagem),  # imagem da carta do BTS
        )

    # Arrasta só a carta pega, em qualquer posição da pilha (no tutorial, levava as de cima junto)
    def get_draggable_pile(self):
        self.draggable_pile = [self]

    # Traz a carta pra frente: no Stack, o último da lista fica por cima
    def move_on_top(self):
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    # Volta a carta pro slot de onde saiu
    def bounce_back(self):
        for card in self.draggable_pile:
            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            card.left = card.slot.left
        self.solitaire.update()

    # Coloca a carta num slot
    def place(self, slot):
        for card in self.draggable_pile:
            # tira do slot antigo e reorganiza as que ficaram (sem buraco)
            if card.slot is not None:
                card.slot.pile.remove(card)
                for i, outra in enumerate(card.slot.pile):
                    outra.top = card.slot.top + i * CARD_OFFSET

            # posiciona embaixo das cartas que já estão no slot novo
            card.top = slot.top + len(slot.pile) * CARD_OFFSET
            card.left = slot.left

            # salva a carta no slot novo
            card.slot = slot
            slot.pile.append(card)

        self.solitaire.update()

    # 1) Início do arraste: escolhe a carta e traz pra frente
    def start_drag(self, e: ft.DragStartEvent):
        self.get_draggable_pile()
        self.move_on_top()

    # 2) Durante o arraste: soma o movimento do mouse (local_delta) na posição
    #    max(0, ...) não deixa a carta sair da mesa
    def drag(self, e: ft.DragUpdateEvent):
        for card in self.draggable_pile:
            card.top = (
                max(0, self.top + e.local_delta.y)
                + self.draggable_pile.index(card) * CARD_OFFSET
            )
            card.left = max(0, self.left + e.local_delta.x)
            self.solitaire.update()

    # 3) Soltou: se estiver perto de um slot, encaixa; senão, volta
    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET))
                < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return
        self.bounce_back()
