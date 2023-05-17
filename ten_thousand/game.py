from game_logic import GameLogic

class play(GameLogic):
    def play(self):
        print("Welcome to Ten Thousand")
        choice = input("(y)es to play or (n)o to decline\n> ")

        if choice.lower() != "y":
            print("OK. Maybe another time")
            return

        total_score = 0
        round_num = 1

        while True:
            print(f"Starting round {round_num}")
            round_score = 0
            num_dice = 6

            while True:
                print(f"Rolling {num_dice} dice...")
                dice = self.roll_dice(num_dice)
                print("***", " ".join(str(d) for d in dice), "***")

                keep = input("Enter dice to keep, or (q)uit:\n> ")

                if keep.lower() == "q":
                    print(f"Thanks for playing. You earned {total_score} points")
                    return

                try:
                    keep_values = [int(value) for value in keep.split()]
                    keep_dice = tuple(die for die in dice if die in keep_values)

                    round_score += self.calculate_score(keep_dice)
                    num_dice -= len(keep_dice)

                    if num_dice == 0:
                        total_score += round_score
                        print(f"You banked {round_score} points in round {round_num}")
                        print(f"Total score is {total_score} points")
                        round_num += 1
                        break

                    print(f"You have {round_score} unbanked points and {num_dice} dice remaining")
                    choice = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

                    if choice.lower() == "b":
                        total_score += round_score
                        print(f"You banked {round_score} points in round {round_num}")
                        print(f"Total score is {total_score} points")
                        round_num += 1
                        break
                    elif choice.lower() == "q":
                        print(f"Thanks for playing. You earned {total_score} points")
                        return

                except ValueError:
                    print("Invalid input. Please try again.")


if __name__ == "__main__":
    gameR = play()
    gameR.play()