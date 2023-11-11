def get_winner(p1,p2):
    if p1 == p2:
        return "It's a tie!"
    elif p1 == 'rock':
        if p2 == 'scissors':
            return "Firsts player wins!"
        else:
            return "Second player wins!"
    elif p1 == 'scissors':
        if p2 == 'paper' :
            return "First player wins!"
        else:
            return "Second player wins!"
    elif p1 == 'paper':
        if p2 == 'rock':
            return "Frist player wins!"
        else:
            return "Second player wins!"
    else:
        return "Invlaid input!"
player1 = input("Fisrt player: rock, paper or scissors: ")
player2 = input("Second player: rock, player or scissors: ")
print(get_winner(player1,player2))    