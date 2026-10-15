# Rock, Paper, Scissor Game

import random

choices = ["rock", "paper", "scissor"]

while True:

    # Main Menu
    print("""
╔══════════════════════════════════════╗
║       ROCK, PAPER AND SCISSOR        ║
╠══════════════════════════════════════╣
║                                      ║
║   🪨   1. Play Game                   ║
║   🏆  2. Challenge Mode              ║
║   📜  3. Rules                       ║
║   🚪  4. Exit                        ║
║                                      ║
╚══════════════════════════════════════╝
""")

    choice = int(input("Enter Your Choice: "))


    # Play Game
    if choice == 1:

        print("""
╔══════════════════════════════════════╗
║             🎮 PLAY GAME             ║
╚══════════════════════════════════════╝
""")

        # Ask again until valid input
        while True:

            player = input(
                "\nEnter anyone rock, paper or scissor: "
            ).lower()

            if player in choices:
                break
            else:
                print(
                    "❌ Invalid choice! "
                    "Please enter rock, paper or scissor."
                )

        computer = random.choice(choices)

        print("\n╔══════════════════════════════════════╗")
        print(f"║  🧑 Player   : {player:<18}      ║")
        print(f"║  🤖 Computer : {computer:<18}      ║")
        print("╚══════════════════════════════════════╝")

        if player == computer:

            print("""
╔══════════════════════════════════════╗
║             🤝 MATCH TIE             ║
╚══════════════════════════════════════╝
""")

        elif ((player == "rock" and computer == "scissor") or
              (player == "scissor" and computer == "paper") or
              (player == "paper" and computer == "rock")):

            print("""
╔══════════════════════════════════════╗
║          🎉 PLAYER WINS! 🎉          ║
╚══════════════════════════════════════╝
""")

        else:

            print("""
╔══════════════════════════════════════╗
║         🤖 COMPUTER WINS!            ║
╚══════════════════════════════════════╝
""")


    # Challenge Mode
    elif choice == 2:

        count_c = 0
        count_p = 0

        print("""
╔══════════════════════════════════════╗
║          🏆 CHALLENGE MODE           ║
║            BEST OF 3                 ║
╚══════════════════════════════════════╝
""")

        for round in range(3):

            print(f"""
╔══════════════════════════════════════╗
║              ROUND {round + 1}                 ║
╚══════════════════════════════════════╝
""")

            # Ask again until valid input
            while True:

                player = input(
                    "Enter your choice (rock, paper or scissor): "
                ).lower()

                if player in choices:
                    break
                else:
                    print(
                        "❌ Invalid choice! "
                        "Please enter rock, paper or scissor."
                    )

            computer = random.choice(choices)

            print("\n╔══════════════════════════════════════╗")
            print(f"║  🧑 Player   : {player:<18} ║")
            print(f"║  🤖 Computer : {computer:<18} ║")
            print("╚══════════════════════════════════════╝")

            if player == computer:

                print("🤝 No points given to both.")

            elif ((player == "rock" and computer == "scissor") or
                  (player == "scissor" and computer == "paper") or
                  (player == "paper" and computer == "rock")):

                count_p = count_p + 1
                print("🎉 Player wins this round!")

            else:

                count_c = count_c + 1
                print("🤖 Computer wins this round!")

            # Scoreboard
            print("\n╔════════════════════════════╗")
            print("║          🏆 SCORE          ║")
            print("╠════════════════════════════╣")
            print(f"║   🧑 Player   : {count_p:<8}   ║")
            print(f"║   🤖 Computer : {count_c:<8}   ║")
            print("╚════════════════════════════╝")


        # Final Result
        if count_c > count_p:

            print("""
╔══════════════════════════════════════╗
║      🤖 COMPUTER WINS CHALLENGE!     ║
╚══════════════════════════════════════╝
""")

        elif count_p > count_c:

            print("""
╔══════════════════════════════════════╗
║        🎉 PLAYER WINS CHALLENGE!     ║
╚══════════════════════════════════════╝
""")

        else:

            print("""
╔══════════════════════════════════════╗
║             🤝 MATCH TIE             ║
╚══════════════════════════════════════╝
""")


    # Rules
    elif choice == 3:

        print("""
╔══════════════════════════════════════╗
║              📜 RULES                ║
╠══════════════════════════════════════╣
║                                      ║
║   📄 Paper beats Rock                ║
║   🪨 Rock beats Scissor               ║
║   ✂️  Scissor beats Paper             ║
║                                      ║
╚══════════════════════════════════════╝
""")


    # Exit
    elif choice == 4:

        print("""
╔══════════════════════════════════════╗
║       👋 THANK YOU FOR PLAYING!      ║
╚══════════════════════════════════════╝
""")
        break


    else:

        print("""
╔══════════════════════════════════════╗
║        ❌ INVALID CHOICE!            ║
║      Please choose 1, 2, 3 or 4.     ║
╚══════════════════════════════════════╝
""")