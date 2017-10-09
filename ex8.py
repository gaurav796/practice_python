"""

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of 
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

"""
import sys


def play_game():
    # get inputs from players
    p1_s = raw_input('Player 1: Rock, paper or scissors (r/p/s) ?')
    p1 = p1_s.strip().lower()[0]
    p2_s = raw_input('Player 2: Rock, paper or scissors (r/p/s) ?')
    p2 = p2_s.strip().lower()[0]

    # determine who is winner

    if p1 == p2: return 'tie'
    elif p1 == 'r':
        if p2 == 'p': return 'P2'
        else : return 'P1'
    elif p1 == 'p':
        if p2 == 'r' : return 'P1'
        else: return 'P2'
    elif p1 == 's':
        if p2 == 'r' : return 'P2'
        else : return 'P1'


def main():
    # get inputs from players
    num= int(raw_input('How many rounds would you like to play'))
    if num < 0:
        sys.exit(0)

    # main execution loop
    i = p1_score = p2_score = 0
    while i < num:
        winner = play_game()
        if winner == 'P1' : p1_score += 1
        elif winner == 'P2' : p2_score += 1
        else : pass
        i += 1

# game over, see if Player wants to play again

    print('Thanks for playing')
    print ("\nFinal score: P1 {} P2 {}\n".format(p1_score, p2_score))
    again = raw_input('Would you like to play again?')
    if 'y' in again.strip().lower()[0]:
        main()
    else:
        sys.exit()


if __name__ == '__main__':
    main()
    
