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
    display_cards(cards)

    root.mainloop()

def get_resized_card(card_path):
    card = Image.open(card_path)
    resized_card = card.resize((75, 109))
    card_image = ImageTk.PhotoImage(resized_card)
    return card_image

def create_card_images(card_names):
    card_images = []
    for card_name in card_names:
        card_image = get_resized_card(f'{card_name}.png')
        card_images.append(card_image)
    return card_images

def display_cards(cards):
    # create images
    print(create_card_images(cards[0]))
    # for n, cards_list in enumerate(cards):
    #     player_frame = LabelFrame(main_frame, text=f"Player {n+1}", bd=0)
    #     print(f"Current n: {n}")
    #     for i, card in enumerate(cards_list):
    #         print(f"i = {i} card = {card}")
    #         player_frame.grid(row=i, column=i+1, ipadx=20)
    #         player_label = Label(player_frame, text='')
    #         global player_image
    #         player_image = get_resized_card(f'{card}.png')
    #         player_label.config(image=player_image)
    #         player_label.pack(pady=20)



if __name__ == "__main__":
    main()
