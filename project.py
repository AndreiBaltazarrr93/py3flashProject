import random
import scoring

# welcome message
print("Welcome to DICER, the thrilling game that combines the excitement of poker and the chance of rolling the dice! In this game, you will use five dice to score points and reach your limit.")
print("What sets DICER apart is its unique scoring system, which offers a variety of ways to earn points. And just like in poker, you'll have the chance to make classic combinations like full-house, straight-flush, and two-pair.")
print("But beware, if you score below the limit, you'll end up in the negative, with a minimum of -1000 points. So, you'll need to use your skill and luck to avoid losing big.")
print("Get ready to roll the dice and test your luck in DICER!")

# get player's name
#global name, score 
name = input("What is your name? ")
limit = int(input("What is the desired Limit of your score?"))
while True:
    # initialize score and loop until user reaches goal or goes below negative limit
    score = 0
    rounds = 1
    while -1000 <= score < limit:
        # roll dice
        dice_rolls = [random.randint(1, 6) for _ in range(5)]
        
        # display dice rolls
        print(f"Round {rounds}")
        print("Your dice rolls: ", dice_rolls)
        
        # ask which dice to keep
        keep_dice_str = input("Which dice do you want to keep (enter space-separated indices, starting from 1)? ")
        keep_dice = [int(idx) - 1 for idx in keep_dice_str.split()]
        kept_dice = [dice_rolls[idx] for idx in keep_dice]

        # roll remaining dice
        remaining_dice = [dice_rolls[idx] for idx in range(5) if idx not in keep_dice]
        new_dice_rolls = [random.randint(1, 6) for _ in range(len(remaining_dice))]
        dice_rolls = kept_dice + new_dice_rolls

        # display new dice rolls
        print("Your new dice rolls: ", dice_rolls)
        score = scoring.dice_score(dice_rolls, name, limit)
        rounds += 1
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "n":
        break
        
    
