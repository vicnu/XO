cell_1 = '1'
cell_2 = '2'
cell_3 = '3'
cell_4 = '4'
cell_5 = '5'
cell_6 = '6'
cell_7 = '7'
cell_8 = '8'
cell_9 = '9'

print(f"{cell_1} {cell_2} {cell_3}\n"
      f"{cell_4} {cell_5} {cell_6}\n"
      f"{cell_7} {cell_8} {cell_9}\n")
count_number = 0
player_symbol = "X"
bot_symbol = "O"
winner = "*"
turn = "X"

for i in range(9):
    while True:
        choice = str(input("enter number of cell : "))
        if choice == cell_1:
            cell_1 = turn
            break
        elif choice == cell_2:
            cell_2 = turn
            break
        elif choice == cell_3:
            cell_3 = turn
            break
        elif choice == cell_4:
            cell_4 = turn
            break
        elif choice == cell_5:
            cell_5 = turn
            break
        elif choice == cell_6:
            cell_6 = turn
            break
        elif choice == cell_7:
            cell_7 = turn
        elif choice == cell_8:
            cell_8 = turn
            break
        elif choice == cell_9:
            cell_9 = turn
            break
    count_number = count_number + 1
    if count_number >= 9:
        break
    elif winner != '*':
        break

    print(f"{cell_1} {cell_2} {cell_3}\n"
          f"{cell_4} {cell_5} {cell_6}\n"
          f"{cell_7} {cell_8} {cell_9}\n")
    count_number = count_number + 1
    if turn =="X":
        turn ="O"
    else:
        turn ="X"

        import random
        while True:
            choice = str(random.randint(1,9))
            if choice == cell_1:
                cell_1 = turn
                break
            elif choice == cell_2:
                cell_2 = turn
                break
            elif choice == cell_3:
                cell_3 = turn
                break
            elif choice == cell_4:
                cell_4 = turn
                break
            elif choice == cell_5:
                cell_5 = turn
                break
            elif choice == cell_6:
                cell_6 = turn
                break
            elif choice == cell_7:
                cell_7 = turn
            elif choice == cell_8:
                cell_8 = turn
                break
            elif choice == cell_9:
                cell_9 = turn
                break

    if cell_1 != '1':
        if cell_1 == cell_2 == cell_3:
            winner = cell_1
        elif cell_1 == cell_4 == cell_7:
            winner = cell_1
        elif cell_1 == cell_5 == cell_9:
            winner = cell_1
    if cell_2 != '2':
        if cell_2 == cell_5 == cell_8:
            winner = cell_2
    if cell_3 != '3':
        if cell_3 == cell_5 == cell_7:
            winner = cell_3
        elif cell_3 == cell_6 == cell_9:
            winner = cell_3
    if cell_4 != '4':
        if cell_4 == cell_5 == cell_6:
            winner = cell_4
    if cell_7 != '7':
        if cell_7 == cell_8 == cell_9:
            winner = cell_7
        count_number = count_number+1

        if count_number>=9:
            break

        print(f"{cell_1} {cell_2} {cell_3}\n"
              f"{cell_4} {cell_5} {cell_6}\n"
              f"{cell_7} {cell_8} {cell_9}\n")

        if cell_1 != '1':
            if cell_1 == cell_2 == cell_3:
                winner = cell_1
            elif cell_1 == cell_4 == cell_7:
                winner = cell_1
            elif cell_1 == cell_5 == cell_9:
                winner = cell_1
        if cell_2 != '2':
            if cell_2 == cell_5 == cell_8:
                winner = cell_2
        if cell_3 != '3':
            if cell_3 == cell_5 == cell_7:
                winner = cell_3
            elif cell_3 == cell_6 == cell_9:
                winner = cell_3
        if cell_4 != '4':
            if cell_4 == cell_5 == cell_6:
                winner = cell_4
        if cell_7 != '7':
            if cell_7 == cell_8 == cell_9:
                winner = cell_7
if winner == "*":
    print("toe")
else:
    print(f" {winner} win game")