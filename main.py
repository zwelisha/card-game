from tkinter import *
import random
from PIL import Image, ImageTk 
# B-sure brand colour -orange #ff6300
root = Tk()
root.title("Multiplayer Card Game")
root.iconbitmap("icon.ico")
root.geometry("1300x1000")
root.configure(background="#ff6300")

from game import Game;
game_obj = Game(6,5)

cards = game_obj.deal_cards()
print(cards)
