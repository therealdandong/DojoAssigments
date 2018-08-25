"""
random and score
"""
import random


def display():

    for i in range(10):
        score = random.randrange(60, 100)
        if 60 <= score <= 69:
            grade = "D"
        if 70 <= score <= 79:
            grade = "C"
        if 80 <= score <= 89:
            grade = "B"
        if 90 <= score <= 100:
            grade = "A"
        print("score", score, "your grade", grade)


display()
