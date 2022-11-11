import sys
from simplepygamemenus.menu import Menu
import pygame

# d = pygame.Surface(size=(1000,800))
main = Menu()
main.add_text(text="SIMPLE PYGAME MENUS", x=250, y=30, size=25)
b_menu = Menu(main=main, title="other menu", showESCKEYhint=True)
main.add_button(label="WHATS THIS?", x=250, y=250, fontsize=30, function=b_menu.run_menu)
b_menu.add_button(label="exit", x=250, y=250, fontsize=30, function=sys.exit)

next_menu = Menu(title="NEXT",main=b_menu)
b_menu.add_button(label="next menu", x=250, y=400, fontsize=30, basecolor=(0,255,0), hovercolor=(255,255,255), function=next_menu.run_menu)


main.run_menu()