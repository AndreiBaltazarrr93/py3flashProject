import random
import scoring

# get player's name
#global name, score 
name = input("What is your name? ")

# initialize score and loop until user reaches goal or goes below negative limit
score = 0
rounds = 1
while -1000 <= score < 10000:
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
    score = scoring.dice_score(dice_rolls, name)
    rounds += 1
    

