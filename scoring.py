def dice_score(dice_rolls, name):
    #global name, score
    score = 0
    
    dice_counts = {}
    for value in dice_rolls:
        dice_counts[value] = dice_counts.get(value, 0) + 1

    # check for straight flush
    if set(dice_rolls) == {1, 2, 3, 4, 5} or set(dice_rolls) == {2, 3, 4, 5, 6}:
        score += 2500
        print(f"{name}, you got a straight flush! You scored 2500 points.")
    # check for 5 of a kind
    elif any(count == 5 for count in dice_counts.values()):
        value = next(key for key, value in dice_counts.items() if value == 5)
        score += 2 * value
        print(f"{name}, you got five-of-a-kind with {value}s! You scored {2 * value} points.")
    # check for 5 of a kind of 4
    elif 4 in dice_counts and dice_counts[4] == 4:
        score -= 2000
        print(f"{name}, you lost 2000 points for rolling four-of-a-kind with 4s.")
    # check for 5 of a kind of 1
    elif 1 in dice_counts and dice_counts[1] == 5:
        score -= 5000
        print(f"{name}, you lost 5000 points for rolling five-of-a-kind with 1s.")
    else:
        # calculate score based on individual dice values
        for value, count in dice_counts.items():
            if count == 4 and value not in [1, 4]:
                score += 2000
                print(f"{name}, you got a four-of-a-kind with {value}s! You scored 2000 points.")
            elif count == 3 and value not in [1, 4] and any(count == 2 for count in dice_counts.values()):
                score += 1500
                print(f"{name}, you got a three-of-a-kind with {value}s and a pair! You scored 1500 points.")
            elif count == 2:
                pairs = [v for v, c in dice_counts.items() if c == 2 and v not in [1, 4]]
                if len(pairs) == 2:
                    score += 1500
                    print(f"{name}, you got two pairs! You scored 1500 points.")
                elif value in [1, 4]:
                    score -= 500
                    print(f"{name}, you lost 500 points for rolling a pair of {value}s.")

    for dice in dice_rolls:
        if dice == 1:
            score -= 1000
            print(f"{name}, you lost 1000 points for rolling a 1.")
        elif dice == 4:
            score -= 750
            print(f"{name}, you lost 750 points for rolling a 4.")
        elif dice == 2:
            score += 100
            print(f"{name}, you got 100 points for rolling a 2.")
        elif dice == 3:
            score += 200
            print(f"{name}, you got 200 points for rolling a 3.")
        elif dice == 5:
            score += 250
            print(f"{name}, you got 250 points for rolling a 5.")
        elif dice == 6:
            score += 300
            print(f"{name}, you got 300 points for rolling a 6.")

    # display current score
    print(f"{name}, your current score is {score}.")
    return score