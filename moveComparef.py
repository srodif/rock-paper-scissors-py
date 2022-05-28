def movecompare(playerM,computerM) :
    """Compares the moves of player and computer
    to declare a winner"""
    print("The comparison has started!")
    if playerM == "a" :
     if computerM == "a" : 
        result = "Draw!"
     elif computerM == "b" :
        result = "Computer wins!"
     else :
        result = "Player wins!"
    elif playerM == "b" :
        if computerM == "b" :
            result = "Draw!"
        elif computerM == "c" :
            result = "Computer wins!"
        else :
            result = "Player wins!"
    else :
      if computerM == "c" :
        result = "Draw!"
      elif computerM == "a" :
        result = "Computer wins!"
      else :
        result = "Player wins!"
    return(result)