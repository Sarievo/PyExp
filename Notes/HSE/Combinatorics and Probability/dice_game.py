def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    dice1_wins = 0
    for i in range(6):
        for j in range(6):
            if dice1[i] > dice2[j]:
                dice1_wins += 1
            elif dice2[j] > dice1[i]:
                dice2_wins += 1

    return dice1_wins, dice2_wins


# print(count_wins([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))
# print(count_wins([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9]))

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    n = len(dices)

    for i in range(n):
        score_table = []
        win_table = []

        for j in range(n):
            if i != j:
                dice1_wins, dice2_wins = count_wins(dices[i], dices[j])
                score_table.append([dice1_wins, dice2_wins])

        for roll in score_table:
            if roll[0] > roll[1]:
                win_table.append(1)
            elif roll[0] == roll[1]:
                win_table.append(0)
            else:
                win_table.append(-1)

        # print("D[" + str(i) + "]'s score table: " + str(score_table) + " or " + str(win_table))

        is_win = True
        for win in win_table:
            if win == -1 or win == 0:
                is_win = False
                break
        if is_win:
            return i

    return - 1


# print(find_the_best_dice([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]))
# print(find_the_best_dice([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]))

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()

    prime_dice = find_the_best_dice(dices)
    if prime_dice == -1:
        strategy["choose_first"] = False

        n = len(dices)
        sub_dice = -1
        for i in range(n):
            max_win = 0
            for j in range(n):
                if i != j:
                    dice1_wins, dice2_wins = count_wins(dices[i], dices[j])
                    if dice2_wins - dice1_wins > max_win:
                        max_win = dice2_wins - dice1_wins
                        sub_dice = j

            strategy[i] = sub_dice if sub_dice != -1 else (i + 1) % len(dices)
    else:
        strategy["choose_first"] = True
        strategy["first_dice"] = prime_dice

    return strategy


# print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
# print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))
