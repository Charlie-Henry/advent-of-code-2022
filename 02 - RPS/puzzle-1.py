import pandas as pd

# A = Rock
# B = Paper
# C = Scissors

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

# Conversion for player moves
ENCRYPTED_KEYS = {"X": "A", "Y": "B", "Z": "C"}

strategy_guide = pd.read_csv("input.txt", sep=" ", header=None)

strategy_guide = strategy_guide.rename(columns={0: "Opponent", 1: "Player"})


def score_game(row):
    # Convert strategy guide
    player_move = ENCRYPTED_KEYS[row["Player"]]

    # return score
    return RULES[(row["Opponent"], player_move)]


strategy_guide["score"] = strategy_guide.apply(score_game, axis=1)

# Part one answer = 14,069
print(sum(strategy_guide["score"]))
