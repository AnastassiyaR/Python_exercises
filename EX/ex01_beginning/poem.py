"""EX01 Poem."""

"""
Ask for user's inputs and print out a poem in one line using f string and newline (\n)

Example input:
color = "red"
objects = "violets"
activity = "code"

Example output:
Roses are red,
violets are blue,
I love to code
And so will you!
"""
color = input("What is your favorite color? ")
objects = input("What is your favorite objects? ")
activity = input("What is your favorite activity? ")
print(f"Roses are {color},")
print(f"{objects} are blue,")
print(f"I love to {activity}")
print("And so will you!")
