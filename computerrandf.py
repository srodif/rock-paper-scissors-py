def computerRand(rand) :
    """Define the computer move through 
    the result of a simple pseudorandom function"""
    if rand <= 0.334 :
        print("Computer uses rock!")
        return("a")
    elif rand <= 0.667 :
        print("Computer uses paper!")
        return("b")
    else :
        print("Computer uses scissors")
        return("c")
