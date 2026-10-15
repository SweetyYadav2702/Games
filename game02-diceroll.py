import random as rand

while True:
    print("\n\n<---DIE ROLL GAME--->")
    print("\n1. One Player")
    print("2. Two Players")
    print("3. Rules")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            while True:
                # One player
                p_score = 0
                c_score = 0
                limit=0
                score = int(input("\nSet a score: "))

                while p_score < score and c_score < score:
                    while True:
                        # Player's turn
                        input("\nPress Enter to roll the dice...")
                        player = rand.randint(1, 6)
                        print("You rolled:", player)
                        p_score = p_score + player
                        
                        if player == 6:
                            limit=limit+1
                            if limit == 3:
                                break
                            continue
                        else:
                            limit=0
                            break
                        
                    while True:
                        # Computer's turn
                        computer = rand.randint(1, 6)
                        print("Computer rolled:", computer)
                        c_score = c_score + computer
                        if computer == 6:
                            limit=limit+1
                            if limit == 3:
                                break
                            continue
                        else:
                            limit=0
                            break

                print("\n\nFinal Scores:")
                print("Player:", p_score)
                print("Computer:", c_score)

                if p_score > c_score:
                    print("\nPlayer Wins! 🎉")
                else:
                    print("\nComputer Wins! 🤖")
                    
                br = False
                while True:
                    again=input("Press y if you want to play again or press n:  ")
                    if again.lower() == 'y':
                        break
                    elif again.lower() == 'n':
                        br = True
                        break
                    else:
                        print("Invalid character.....")
                        print("Please press either y or n.")
                        continue
                
                if br:
                    break

        case 2:
            while True:
                p1_score = 0
                p2_score = 0
                limit=0
                score = int(input("\nSet a score: "))
                
                while p1_score < score and p2_score < score:
                    while True:
                        # Player-1's turn
                        input("\nPress Enter to roll the dice for player-1...")
                        player1 = rand.randint(1, 6)
                        print("Player-1 rolled:", player1)
                        p1_score = p1_score + player1
                        if player1 == 6:
                            limit=limit+1
                            if limit ==3:
                                break
                            continue
                        else:
                            limit=0
                            break
                        
                    while True:   
                        # Player-2's turn
                        input("\nPress Enter to roll the dice for player-2...")
                        player2 = rand.randint(1, 6)
                        print("Player-2 rolled:", player2)
                        p2_score = p2_score + player2
                        if player2 == 6:
                            limit=limit+1
                            if limit == 3:
                                break
                            continue
                        else:
                            limit=0
                            break
                
                print("\n\nFinal Scores:")
                print("Player-1: ", p1_score)
                print("Player-2: ", p2_score)
                
                if p1_score > p2_score:
                    print("Player-1 Wins! 🎉")
                else:
                    print("Player-2 Wins! 🎉")

                again=input("Press y if you want to play again or press n:  ")
                if again.lower() == 'y':
                    continue
                elif again.lower() == 'n':
                    break
                else:
                    print("Invalid character.....")
                    print("Please press either y or n.")
                    
                
        case 3:
            print("\nRules: ")
            print("1. Three 6s Rule: If any player gets three 6s, they will lose their turn, and the turn will automatically go to the other player.")
            #print("2. Rolling a 1: If a player rolls 1, their total score will reset to 0, and their turn will end.")

        case 4:
            print(" 👋 THANK YOU FOR PLAYING!  ")
            break
        case _:
            print("Invalid choice!")
            print("Please choose 1, 2, or 3.")