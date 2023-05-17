# Multiplayer Card Game

## Game Details
- 6 players are dealt 5 cards from two 52 card decks, and the winner is the one with the highest score.The score for each player is calculated by adding up all 5 card values for each player, where the number cards have their face value, J = 11, Q = 12, K = 13 and A = 11 (not 1).
- In the event of a tie, the scores are recalculated for only the tied players by calculating a "suit score" for:
    - Each player to see if the tie can be broken (it may not).
    - Each card is given a score based on its suit, with diamonds = 1, hearts = 2, spades = 3 and clubs = 4, and the player's score is the multiplication of all 5 suit value.

    ### You are required to write an application using a stack of your choice that needs to do the following:
    - Run on Windows.
    - Randomly generate the 5 cards that each player will receive. Show the cards that each player received, the winner(s) and the score for each player.

## Getting Started

### Requirements

1. Python3
2. Pip3
3. Text editor (Recommended: VSCode or SublimeText or Atom)
4. Black
5. unittest
6. pillow
7. Tkinter


### Installation

#### 1. Python3

The installation differs from one operating system to the other, but the documentation which can be found [here](https://www.python.org/downloads/) have clear instructions for each operating system.

#### 2. Pip3

Pip3 is distributed with latest Python versions - which means when you download Python3 you automatically get Pip3 installed on your machine.

#### 3. Text Editor
Any text editor of your choice can be used. However Visual Studio Code and Atom are highly recommended.

#### 4. Black
Run ```pip3 install black```

#### 5. Unittest

Run ```pip3 install unittest```

#### 6. Pillow
Run ```pip3 install Pillow

#### 7. Tkinter
Run ```pip3 install tk```

#### Folder Structure

There is one folder for this project: `card-game`. The folder contains all the files to run this game. I did this on purpose because Python can be very finicky with paths. 

```
card-game
    .gitignore
    cardgamelogger.log
    game.py
    icon.ico
    icon.png
    README.md
    main.py
    test_game.py
```

### Formatting The Code

Use Black for consistency, it takes away the pain of memorising all the PEP8 coding standards and rules.
#### formatting a file example
Run ```black filename.extension``` for example ```black main.py``` will format the main script.


### Running The Project

#### 1. Clone the project
```
git clone https://github.com/zwelisha/card-game.git
```

#### 2. Change Directory (To the root folder of the project)

Change directory to the project `cd card-game`.
There you will see the folder structure detailed above.



Then to run this game run the following command

```
python3 main.py
```

### Testing The Project

```
Run python3 test_game.py
```
Have fun!

#### Authors

[Zweli Mthethwa](https://www.linkedin.com/in/zweli-mthethwa-244b45a8/)