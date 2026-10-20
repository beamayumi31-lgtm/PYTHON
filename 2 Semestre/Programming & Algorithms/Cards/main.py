import flet as ft

from solitaire import Solitaire


# Cria a mesa e coloca na janela
def main(page: ft.Page):
    solitaire = Solitaire()
    page.add(solitaire)


# Abre o app; as imagens ficam na pasta "assets"
ft.run(main, assets_dir="assets")
