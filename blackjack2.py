
import random

while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    card_3 = random.choice(cards)
    card_4 = random.choice(cards)
    player_1 = int(card_1) + int(card_2)
    player_2 = int(card_3) + int(card_4)

    print(f"Your cards: [{card_1}] [{card_2}]\n[{player_1}]")
    print(f"Dealers cards: [{card_3}] [?]")
    if player_1 == 21:
        print("$$$Winner Winner Chicken Dinner$$$")
        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("Goodbye")
            break
        
    while player_1 < 21:
        hit_stay = input("Hit[1] or stay[2]? ")
        if hit_stay == "1":
            amount = random.choice(cards)
            print("+" + "[" + str(amount) + "]")
            if player_1 > 10 and amount == 11:       
                amount = 1
            player_1 += amount
            print("Your Score: " +  "[" + str(player_1) + "]")
            if player_1 <= 21:
                continue
            elif player_1 > 21:
                print("Dealer Wins")
                pass
        elif hit_stay == "2":
            break
    if player_1 > 21:
        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("Goodbye")
        break
    print(f"Dealers cards: [{card_3}] [{card_4}]\n[{player_2}]")
    while player_2 <= 16:
        if player_2 > player_1:
            break
        else: 
            amount = random.choice(cards)
            print("+" + "[" + str(amount) + "]")
            if player_2 > 10 and amount == 11:       
                amount = 1
            player_2 += amount
            print(f"Dealers Score: [{player_2}]")
    if player_2 > 21:
        print("Player Wins")
    elif player_2 > player_1:
        print("Dealer Wins")
    elif player_2 < player_1 and not player_1 > 21:
        print("Player Wins")
    else:
        print("Draw")
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
    break
              


