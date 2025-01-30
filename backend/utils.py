import random

adjectives = [
    "cpu", "ram", "bit", "nan", "io", "api", "bot", "net", "cli", "gpu"
]

nouns = [
    "bug", "exe", "log", "bit", "hash", "zip", "cod", "bit", "api", "lan"
]


def generate_insult():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    word = adjective + noun
    return word
