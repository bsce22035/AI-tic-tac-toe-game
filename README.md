# Tic Tac Toe AI (Tkinter)

A modern, dark-themed **Tic Tac Toe** game built with Python's **Tkinter** library.  
Play against an AI opponent with three difficulty levels — Easy, Medium, and Hard — powered by the **Minimax algorithm**.

##  Features

- **Single-player mode**: Player vs Computer.
- **3 Difficulty Levels**:
  - Easy → random moves.
  - Medium → mix of random and smart moves.
  - Hard → unbeatable AI using Minimax.
- **Custom Start Option**: Choose whether the player or computer starts first.
- **Score Tracking**: Persistent scores for Player, Computer, and Draws.
- **Winning Highlight**: Highlights the winning combination.
- **Dark Theme UI**: Clean and modern look.
- **Responsive Controls**: Play Again and Reset Scores buttons.

##  Requirements

- Python **3.7+**
- Tkinter (comes pre-installed with most Python distributions)


## How to Play
1. Choose difficulty from the dropdown.
2. Select Player Starts or Computer Starts.
3. Click on a cell to make your move (X).
4. The computer (O) will respond.
5. The first to align 3 marks (horizontally, vertically, or diagonally) wins.
6. Use Play Again to start a new round, or Reset Scores to clear the scoreboard.

## AI Logic
- Easy → Random available move.
- Medium → 50% random moves, 50% Minimax-based.
- Hard → Always uses Minimax algorithm for optimal play.

Minimax: Recursively evaluates all possible moves to choose the best one.
In Hard mode, this makes the AI unbeatable.
