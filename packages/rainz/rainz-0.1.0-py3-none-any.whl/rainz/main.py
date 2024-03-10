import random
import time

# Define the alphabet string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Infinite loop to keep printing
while True:
    # Get a random alphabet
    letter = random.choice(alphabet)

    # Print the letter at a random position
    print(" " * random.randint(0, 60) + letter)

    # Sleep for a short duration to create the rain effect
    time.sleep(0.1)
