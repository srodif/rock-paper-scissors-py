def moveCheck(move) :
    """Checks if the user did input rock paper or scissors"""
    if move == "rock" :
        return("a")
    elif move == "paper" :
        return("b")
    elif move == "scissors" :
        return("c")
    else :
        print("Please provide a valid move next time.")
        print("Rock has been selected as a default")
        return("a")