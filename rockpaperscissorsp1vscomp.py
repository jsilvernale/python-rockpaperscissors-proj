import random

def playerVsComp():
    while True: 
        print("pick one of the 3 choicse.")
        player = input("rock, paper, scissors shoot! type quit if you'd like to stop ")
        plays = ['rock', 'paper', 'scissors']
        computer_play = random.choice(plays)
        print(f'You chose {player} and computer picks {computer_play}.')      
        if player.lower() == 'rock' and computer_play == 'rock':
            print("It's a tie!!")
        elif player.lower() == 'paper' and computer_play == 'paper':
            print("It's a tie!!")
        elif player.lower() == 'scissors' and computer_play == 'scissors':
            print("It's a tie!!")
        elif player.lower() == 'paper' and computer_play == 'rock':
            print("Player wins!!")
        elif player.lower() == 'paper' and computer_play == 'scissors':
            print("Computer wins!!")
        elif player.lower() == 'rock' and computer_play == 'paper':
            print("Computer wins!!")
        elif player.lower() == 'rock' and computer_play == 'scissors':
            print("Player wins!!")
        elif player.lower() == 'scissors' and computer_play == 'paper':
            print("Player wins!!")
        elif player.lower() == 'scissors' and computer_play == 'rock':
            print("Computer wins!!")
        elif player.lower() == 'quit':
            break
        else:
            print("thats not part of rock paper scissors!!! try again.")

playerVsComp()
