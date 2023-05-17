from game import Game
from tkinter import Tk, Frame, Label, Button
import random
from PIL import Image, ImageTk
import logging

# B-sure brand colour -orange #ff6300
root = Tk()
root.title("Multiplayer Card Game")
root.geometry("1300x1000")

info_frame = Frame(root)
info_frame.pack(pady=5)
info_label = Label(info_frame, text="EACH ROW REPRESENT CARDS FOR PLAYER 1-6")
info_label.pack()

winner_label = Label(info_frame, text="Winner: ")


main_frame = Frame(root)
main_frame.pack(pady=5)


global no_of_players
global cards_per_player
global cards
global scores
global tied
scores = dict(player1=0, player2=0, player3=0, player4=0, player5=0, player6=0)

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="cardgamelogger.log", level=logging.DEBUG, format=LOG_FORMAT, filemode="w"
)
logger = logging.getLogger()


logger.info("Multiplayer Card Game Logs")


def main():
    tied = False
    no_of_players = 6
    cards_per_player = 5
    game_obj = Game(no_of_players, cards_per_player)
    cards = game_obj.deal_cards()
    display_cards(cards)
    replay_btn = Button(
        root, text="DEAL CARDS", command=lambda: display_cards(game_obj.deal_cards())
    )

    replay_btn.pack()
    quit_btn = Button(root, text="QUIT", command=root.destroy)
    quit_btn.pack()
    winner_label.pack()

    root.mainloop()


def get_resized_card(card_path):
    """Resizes card image
    Args:
        card_path: the absolute path of the card
    """
    card = Image.open(card_path)
    resized_card = card.resize((57, 74))

    card_image = ImageTk.PhotoImage(resized_card)
    return card_image


def create_card_images(card_names: list) -> list:
    """Creates card images list from a list of card names
    Args:
        card_names: a list of strings with all card names
    Returns:
        list: a list with all card images
    """
    card_images = []
    for card_name in card_names:
        card_image = get_resized_card(f"{card_name}.png")
        card_images.append(card_image)
    return card_images


def calculate_player_score(player_cards: list) -> int:
    """Calculate individual player score from their cards
    Args:
        player_cards: a list of cards received by the player
    Returns:
        int: a score for the player
    """
    score = 0
    for card in player_cards:
        point = int(card.split("_")[0])
        if point == 14:
            point = 11
        score = score + point
    return score


def calculate_suit_score(player_cards: list) -> int:
    """Calculates the suit score for given player cards
    Args:
        player_cards:
    """
    score = 1
    for card in player_cards:
        suit_name = card.split("_")[-1]
        if suit_name == "diamonds":
            score = score * 1
        elif suit_name == "hearts":
            score = score * 2
        elif suit_name == "spades":
            score = score * 3
        else:
            score = score * 4
    return score


def calculate_scores(cards: list) -> None:
    """Calculates the score for each player given as input
    Args:
        cards: a 2D list with each row representing the cards for each player
    Returns:
        None
    """
    size = len(cards)
    for i in range(size):
        score = calculate_player_score(cards[i])
        scores[f"player{i+1}"] = score


def get_highest_score(score_dict: dict) -> int:
    """Calculates the highest score from the given dictionary object
    Args:
        score_dict: a dictionary object with scores for each player
    Returns:
        int: the highest score
    """
    d_keys = list(score_dict.keys())
    highest = score_dict[d_keys[0]]
    size = len(d_keys)
    for i in range(size):
        k = d_keys[i]
        if score_dict[k] >= highest:
            highest = score_dict[k]
    return highest


def highest_score_string(score_dict: dict) -> str:
    """Generates the highest score string
    Args:
        score_dict: a dictionary object representing scores for all players
    Returns:
        str: a string with winner or winners (in case the tie can not be broken) keys and scores
    """
    highest = get_highest_score(score_dict)
    score_string = " "
    score_keys = list(score_dict.keys())
    winners = []
    for score_key in score_keys:
        if score_dict[score_key] == highest:
            winners.append(score_key)
    total = len(winners)
    if total == 1:
        score_string = winners[0]
    else:
        i = 0
        while i <= total - 2:
            score_string = score_string + winners[i] + " "
            i = i + 1
        score_string = f"{score_string} and {winners[total - 1]}"
    return score_string


def count_occurence(n: int, score_dict: dict) -> int:
    """Counts how many times n appears in score_dict
    Args:
        n: an integer
        score_dict: a dictionary object representing scores
    Returns:
        int: count of scores with the value n, heps with checking a tie
    """
    count = 0
    k = list(score_dict.keys())
    size = len(score_dict)
    for i in range(size):
        if score_dict[k[i]] == n:
            count = count + 1
    return count


def break_tie(game_cards):
    """In case there are players who are tied, the tie is broken by calculating the suit score for those tied players and the scores are updated
    Args:
        game_cards: a list with all cards for each player. A 2D list
    Returns:
        None
    """
    tied_players = []
    score_keys = list(scores.keys())
    for score_key in score_keys:
        if count_occurence(scores[score_key], scores) >= 2:
            tied_players.append(score_key)

    if len(tied_players) >= 2:
        tied = True
        for player_key in tied_players:
            player_cards = game_cards[int(player_key[-1]) - 1]
            suit_score = calculate_suit_score(player_cards)
            scores[player_key] = suit_score
        logger.info(f"Tied players: {tied_players}")


def update_winner_label():
    """Updates the winner label by first generating the scores and winner strings
    Args:
        None
    Returns:
        None
    """
    scores_string = " "
    score_keys = list(scores.keys())
    for score_key in score_keys:
        scores_string = f"{scores_string} {score_key} : {scores[score_key]}"
    winner = highest_score_string(scores)
    winner_label.configure(
        text=f"SCORES: {scores_string.upper()} \n\n WINNER: {winner.upper()}"
    )
    winner_label.configure(font=("Tekton Pro", 14), fg="#ff6300")


def display_cards(all_cards):
    cards = all_cards
    calculate_scores(cards)
    for n, player_cards in enumerate(cards):
        logger.info(f"player {n+1} cards: {player_cards}")
    logger.info(f"Initial scores: {scores}")
    break_tie(cards)
    update_winner_label()
    logger.info(f"Final scores: {scores}")

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
        label = Label(main_frame, image=card_image)
        label.image = card_image
        label.grid(row=row, column=col, padx=5, pady=10)
        col = col + 1
        if col >= 5:
            row = row + 1
            col = 0


if __name__ == "__main__":
    main()
