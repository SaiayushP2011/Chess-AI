#list a bunch of variables that store a string that is either nothing or a piece
#when the program needs to move something, it checks whether or not there is something within the variable.
#use For loops to check for the piece that will move and the square to move it into

#Black AI to be coded. Original version checks for all legal moves and then randomly selects one. Future versions will use a more sophisticated algorithm to select the best move.

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

#sets piece values for evaluation function. In a more sophisticated version, this could be expanded to include positional values and other factors.
piece_values = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
    "K": 1000,
}

#Piece representation: first character is color (b or w), second character is type (R, N, B, Q, K, P)
bR = "bR"
bN = "bN"
bB = "bB"
bQ = "bQ"
bK = "bK"
bP = "bP"

wR = "wR"
wN = "wN"
wB = "wB"
wQ = "wQ"
wK = "wK"
wP = "wP"


#function to retrieve the piece value for a given place
def piece_value(piece):
    return piece_values.get(piece[1], 0) if piece else 0


#Board setup.
a = [bR, bP, "", "", "", "", wP, wR]
b = [bN, bP, "", "", "", "", wP, wN]
c = [bB, bP, "", "", "", "", wP, wB]
d = [bQ, bP, "", "", "", "", wP, wQ]
e = [bK, bP, "", "", "", "", wP, wK]
f = [bB, bP, "", "", "", "", wP, wB]
g = [bN, bP, "", "", "", "", wP, wN]
h = [bR, bP, "", "", "", "", wP, wR]

#Dictionary for chessboard, with keys as the files.
chessboard = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
}

#Loop for the entire algorithm. In a more sophisticated version, this would include checks for check, checkmate, stalemate, and other game-ending conditions.
while True:
    move = input("Enter your move (or 'mode both' / 'mode white' / quit): ")
    if move == "quit":
        break
    # allow switching control mode: human controls white only (default) or both sides
    if move.startswith("mode "):
        mode = move.split()[1].lower()
        if mode in ("both", "white"):
            human_mode = mode
            print(f"Human mode set to: {human_mode}")
            continue
        else:
            print("Unknown mode. Use 'mode both' or 'mode white'.")
            continue

    # Function to evaluate the board position based on material count for both sides.
    def evaluate_board():
        white_value = 0
        black_value = 0
        for file in chessboard:
            for rank in range(8):
                piece = chessboard[file][rank]
                if piece:
                    value = piece_value(piece)
                    if piece.startswith("w"):
                        white_value += value
                    else:
                        black_value += value
        return white_value - black_value

    before_eval = evaluate_board()

    # ensure human_mode exists (default to white)
    if 'human_mode' not in globals():
        human_mode = 'white'
    if len(move) != 4 or move[0] not in letters or move[2] not in letters or not move[1].isdigit() or not move[3].isdigit():
        print("Invalid move format. Use a format like e2e4.")
        continue
    
    #variables with the file and rank of the piece to move and the destination square
    from_file = move[0]
    to_file = move[2]
    from_rank = 8 - int(move[1])
    to_rank = 8 - int(move[3])

    #Checking for validity of the move input. In a more sophisticated version, this would also check for move legality based on piece movement rules and game state.
    if from_rank < 0 or from_rank > 7 or to_rank < 0 or to_rank > 7:
        print("Invalid rank. Use ranks 1 through 8.")
        continue

    if chessboard[from_file][from_rank] == "":
        print("No piece at the source square!")
        continue

    # enforce human mode: if human_mode is 'white' disallow moving black pieces
    piece_at_source = chessboard[from_file][from_rank]
    if human_mode == 'white' and piece_at_source.startswith('b'):
        print("You are controlling White only. Use 'mode both' to control Black as well.")
        continue

    destination_piece = chessboard[to_file][to_rank]

    if destination_piece != "":
        if destination_piece[0] == piece_at_source[0]:
            print("Illegal move! You cannot capture your own piece.")
            continue
    
    #Needed for piece movement. In a more sophisticated version, this would include checks for specific piece movement rules, checks, pins, and other tactical considerations.
    chessboard[to_file][to_rank] = chessboard[from_file][from_rank]
    chessboard[from_file][from_rank] = ""

    #Evaluate the board after the move and compare it to the evaluation before the move to detect blunders and mistakes. In a more sophisticated version, this could include more advanced evaluation metrics and thresholds for blunder/mistake detection.
    after_eval = evaluate_board()
    change = after_eval - before_eval

    print(f"Before eval: {before_eval}")
    print(f"After eval: {after_eval}")
    print(f"Change: {change}")
    # Will detect a blunder if the move results in a change less than or equal to -3, and a mistake if the change is less than or equal to -1. These thresholds are arbitrary and could be adjusted based on testing and tuning.
    if change <= -3:
        print("Blunder detected!")
    elif change <= -1:
        print("Mistake detected!")
    else:
        print("Move looks fine.")

    # If human is only white, make a simple random black move now
    if human_mode == 'white':
        # collect all black pieces and possible empty destinations (move generation is very basic and does not check for legal moves, checks, pins, etc. In a more sophisticated version, this would be replaced with proper move generation and selection logic.)
        black_moves = []
        for f in letters:
            for r in range(8):
                p = chessboard[f][r]
                if p and p.startswith('b'):
                    for tf in letters:
                        for tr in range(8):
                            if chessboard[tf][tr] == "" or chessboard[tf][tr].startswith("w"):
                                black_moves.append((f, r, tf, tr))
        # randomly select a move from the list of possible black moves
        if black_moves:
            bf, br, tf, tr = random.choice(black_moves)
            chessboard[tf][tr] = chessboard[bf][br]
            chessboard[bf][br] = ""
            print(f"Black AI moved {bf}{8-br} to {tf}{8-tr}")



    print(chessboard["a"])
    print(chessboard["b"])
    print(chessboard["c"])
    print(chessboard["d"])
    print(chessboard["e"])
    print(chessboard["f"])
    print(chessboard["g"])
    print(chessboard["h"])
