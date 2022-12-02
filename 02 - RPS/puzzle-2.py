import pandas as pd

# A = Rock
# B = Paper
# C = Scissors

# Conversion for needed result
ENCRYPTED_KEYS = {"X": "Lose", "Y": "Draw", "Z": "Win"}

# (Opponent move, Needed Result): Player Move
NEEDED_MOVE = {
    ("A", "Lose"): "C",
    ("A", "Draw"): "A",
    ("A", "Win"): "B",
    ("B", "Lose"): "A",
    ("B", "Draw"): "B",
    ("B", "Win"): "C",
    ("C", "Lose"): "B",
    ("C", "Draw"): "C",
    ("C", "Win"): "A",
}

# Hash table
# (Opponent move, Player move): Score
RULES = {
    ("A", "A"): 1 + 3,
    ("B", "B"): 2 + 3,
    ("C", "C"): 3 + 3,
    ("A", "B"): 2 + 6,
    ("A", "C"): 3 + 0,
    ("B", "A"): 1 + 0,
    ("B", "C"): 3 + 6,
    ("C", "A"): 1 + 6,
    ("C", "B"): 2 + 0,
}


strategy_guide = pd.read_csv("input.txt", sep=" ", header=None)

strategy_guide = strategy_guide.rename(columns={0: "Opponent", 1: "Player"})


def score_game(row):
    # Convert strategy guide
    needed_result = ENCRYPTED_KEYS[row["Player"]]

    # Lookup the move we need to make
    player_move = NEEDED_MOVE[(row["Opponent"], needed_result)]

    # return score
    return RULES[(row["Opponent"], player_move)]


strategy_guide["score"] = strategy_guide.apply(score_game, axis=1)

# Part two answer = 12,411
print(sum(strategy_guide["score"]))
