import random


class GameLogic:
    @staticmethod
    def get_scorers(dice):
        # dice= tuple(dice)
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scorers.append(val)
        return tuple(scorers)
    
    @staticmethod
    def roll_dice(num_dice):
        if num_dice < 1 or num_dice > 6:
            raise ValueError("Number of dice must be between 1 and 6.")

        values = tuple(random.randint(1, 6) for _ in range(num_dice))
        return values

    @staticmethod
    def calculate_score(dice):
        score = 0
        counts = [0] * 7

        for die in dice:
            counts[die] += 1

        # for the 3 pairs HOT DICE
        if counts[1] != 2 and sum(count == 2 for count in counts[2:]) == 3:
            score = 1500
            return score

        # for the triple ones and above
        if counts[1] >= 3:
            score += 1000 * (counts[1] - 2)
            counts[1] = 0

        for i in range(2, 7):
            if counts[i] >= 3:
                score += i * 100 * (counts[i] - 2)
                counts[i] = 0

        if set(dice) == set([1, 2, 3, 4, 5, 6]):
            score = 1500
        elif set(counts[2:]) == {2} and counts[1] == 0:
            score = 1500
        elif (
            all(count in {2, 3, 4, 5, 6} for count in counts[1:])
            and len(set(counts[1:])) == 1
        ):
            score = 3000
        else:
            score += counts[1] * 100
            score += counts[5] * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        if len(keepers) > len(roll):
            return False

        roll_counts = [0] * 7
        keepers_counts = [0] * 7

        for die in roll:
            roll_counts[die] += 1

        for die in keepers:
            keepers_counts[die] += 1

        for i in range(1, 7):
            if keepers_counts[i] > roll_counts[i]:
                return False

        return True

if __name__ == "__main__":
    gameR = GameLogic()
    