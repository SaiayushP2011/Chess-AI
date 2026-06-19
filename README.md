# Chess Blunder Detector/ Chess AI

A Python-based chess analysis tool that detects material blunders by comparing board evaluations before and after each move.

The program uses a custom chessboard representation, assigns values to pieces, and classifies moves as "good", "mistakes", or "blunders" based on material loss.

## How It Works

The player enters a move using standard notation (example: `e2e4`). The program evaluates the board before and after the move by counting the material value of all pieces. It then compares the change in evaluation to determine if the move caused a mistake or blunder. Afterward, the Black AI makes a random move.

## Features

* Custom chessboard system
* Move input using notation (`e2e4`)
* Material-based evaluation
* Blunder and mistake detection
* Basic random Black AI

## Future Improvements

* Piece-specific legal move validation
* Stronger Black AI
* Positional and tactical evaluation

## Built With

* Python
* Random module

## Purpose

Built to improve my understanding of chess programming, board evaluation, and AI algorithmic decision-making.
