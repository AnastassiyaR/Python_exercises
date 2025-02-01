"""EX01 ATM."""

"""
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))
banknotes = 0

if amount >= 100:
    banknotes += amount // 100
    amount = amount % 100

if 100 > amount >= 50:
    banknotes += amount // 50
    amount = amount % 50

if 50 > amount >= 20:
    banknotes += amount // 20
    amount = amount % 20

if 20 > amount >= 10:
    banknotes += amount // 10
    amount = amount % 10

if 10 > amount >= 5:
    banknotes += amount // 5
    amount = amount % 5

if 5 > amount >= 1:
    banknotes += amount // 1
    amount = amount % 1

print(f"Amount of banknotes needed: {banknotes}")
