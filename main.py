from game import Game
from tkinter import *
import random
from PIL import Image, ImageTk 
# B-sure brand colour -orange #ff6300
root = Tk()
root.title("Multiplayer Card Game")
root.iconbitmap("icon.ico")
root.geometry("1300x1000")
root.configure(bg="#ff6300")

main_frame = Frame(root, bg="#ff6300")
main_frame.pack(pady=30)

def main():
    no_of_players = 6
    cards_per_player = 5
    game_obj = Game(no_of_players,cards_per_player)
    cards = game_obj.deal_cards()
    print(cards)

def get_resized_card(card_path):
    card = Image.open(card_path)
    resized_card = card.resize(75, 109)
    card_image = ImageTk.PhotoImage(resized_card)
    return card_image

def display_cards(cards):
    pass

if __name__ == "__main__":
    main()
