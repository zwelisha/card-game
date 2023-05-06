from game import Game
from tkinter import *
import random
from PIL import Image, ImageTk
# B-sure brand colour -orange #ff6300
root = Tk()
root.title("Multiplayer Card Game")
# root.iconbitmap(ImageTk.PhotoImage(Image.open("icon.ico")))
root.geometry("1300x1000")
# root.configure(bg="#ff6300")

info_frame = Frame(root)
info_frame.pack(pady=10)
info_label = Label(info_frame, text="EACH ROW REPRESENTS CARDS FOR PLAYER 1-6")
info_label.pack()

winner_label = Label(info_frame, text='Winner: ')

main_frame = Frame(root)
main_frame.pack(pady=10)



global no_of_players
global cards_per_player
global cards
def main():
    no_of_players = 6
    cards_per_player = 5
    game_obj = Game(no_of_players,cards_per_player)
    cards = game_obj.deal_cards()
    display_cards(cards)
    replay_btn = Button(root, text='REPLAY', command = lambda: display_cards(game_obj.deal_cards()))
    replay_btn.pack()
    quit_btn = Button(root, text="QUIT", command=root.destroy)
    quit_btn.pack()
    winner_label.pack()

    #calculate points and display winner
    root.mainloop()

def get_resized_card(card_path):
    card = Image.open(card_path)
    resized_card = card.resize((57, 74)) #75 109
    card_image = ImageTk.PhotoImage(resized_card)
    return card_image

def create_card_images(card_names):
    card_images = []
    for card_name in card_names:
        card_image = get_resized_card(f'{card_name}.png')
        card_images.append(card_image)
    return card_images


def display_cards(all_cards):
    cards = all_cards
    print(cards)
    row = 0
    col = 0
    image_list = []
    for card_list in cards:
        images = create_card_images(card_list)
        for i in range(len(images)):
            global image
            image = images[i]
            image_list.append(image)


    for card_image in image_list:
        label = Label(main_frame,image=card_image)
        label.image = card_image
        label.grid(row=row,column=col,padx=5,pady=10)
        col+=1
        if col >=5:
            row+=1
            col = 0
    
if __name__ == "__main__":
    main()
