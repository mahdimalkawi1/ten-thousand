>Driver :husam hasan obeidat <br>
>Navigators: Mahdi Malkawi & Sakher Shteyat


# Ten-Thousand Game

This is a simple dice game implemented in Python. The `GameLogic` class provides methods to roll the dice and calculate the score based on the dice roll.

## Usage

1. Run the script `dice_game.py` to play the game.
2. The `GameLogic.roll_dice(num_dice)` method can be used to roll the dice. It takes the number of dice to be rolled as an argument and returns the values as a tuple.
3. The `GameLogic.calculate_score(roll)` method can be used to calculate the score for a given dice roll. It takes the dice roll as an argument (a tuple of dice values) and returns the score based on the rules of the game.

## Score Rules

The score rules for the game are as follows:

- A single 1 is worth 100 points.
- A single 5 is worth 50 points.
- Three of a kind (except for 1s) are worth 100 times the number (e.g., three 4s are worth 400 points).
- Three 1s are worth 1000 points.
- Additional 1s in a three of a kind group are worth 100 points each.
- Additional 5s in a three of a kind group are worth 50 points each.

## Examples

```python
import random

# Roll the dice
dice_roll = GameLogic.roll_dice(6)
print(f"Dice Roll: {dice_roll}")

# Calculate the score
score = GameLogic.calculate_score(dice_roll)
print(f"Score: {score}")