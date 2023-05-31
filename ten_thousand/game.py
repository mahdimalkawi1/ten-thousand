try:
    from ten_thousand.game_logic import GameLogic
except:
        from game_logic import GameLogic



#
class Game(GameLogic):
    def play(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        choice = input("> ")

        if choice.lower() != "y":
            print("OK. Maybe another time")
            return

        total_score = 0
        round_num = 1

        while True:
            print(f"Starting round {round_num}")
            round_score = 0
            num_dice = 6
            cheater = False  # Initialize cheater status to False

            while True:
                if not cheater:
                    print(f"Rolling {num_dice} dice...")
                    dice = self.roll_dice(num_dice)

                str1 = str(" ".join(str(d) for d in dice))
                print(f"*** {str1} ***")
                print("Enter dice to keep, or (q)uit:")
                keep = input("> ")

                if keep.lower() == "q" or round_num > 20:
                    print(f"Thanks for playing. You earned {total_score} points")
                    return

                try:
                    keep_values = [int(value) for value in keep]
                    keep_dice = tuple(die for die in dice if die in keep_values)
                    if len(keep_values) != len(keep_dice):
                        raise ValueError("Cheater!!! Invalid input")

                    cheater = False  # Reset cheater status if input is valid
                    round_score += self.calculate_score(keep_dice)
                    num_dice -= len(keep_dice)

                    if num_dice == 0:
                        total_score += round_score
                        print(f"You banked {round_score} points in round {round_num}")
                        print(f"Total score is {total_score} points")
                        round_num += 1
                        break

                    print(
                        f"You have {round_score} unbanked points and {num_dice} dice remaining"
                    )
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    choice = input("> ")

                    if choice.lower() == "b":
                        total_score += round_score
                        print(f"You banked {round_score} points in round {round_num}")
                        print(f"Total score is {total_score} points")
                        round_num += 1
                        break
                    elif choice.lower() == "q" or round_num > 20:
                        print(f"Thanks for playing. You earned {total_score} points")
                        return
                    # Check for "Zilch"
                    elif self.calculate_score(dice) == 0:
                        print("*" * 40)
                        print("**        Zilch!!! Round over         **")
                        print("*" * 40)
                        print(f"You banked 0 points in round {round_num}")
                        print(f"Total score is {total_score} points")
                        round_num += 1
                        break

                except ValueError as e:
                    print(str(e))
                    cheater = True  # Set cheater status to True


if __name__ == "__main__":
    gameR = Game()
    gameR.play()