import random


"""
toss coin for 5000 times.
"""


def tosscoin(numb):
    i = 1
    coin_sum = 0
    coin_up = 0
    coin_down = 0
    word = ""
    while i <= numb:
        coin = random.randint(0, 1)
        if coin == 0:
            coin_sum += 1
            coin_up += 1
            word = "head"
        elif coin == 1:
            coin_sum += 1
            coin_down += 1
            word = "down"
        i += 1
        print("Attempt #", coin_sum, ": Throwing a coin... It's a ", word,
              "! ... Got", coin_up, " head(s) so far and ", coin_down, " tail(s) so far")

tosscoin(5000)