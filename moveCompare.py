print("Hello")
playerIn = "a"
computerIn = "c"
result = 1
print(result)

def movecompare(playerM,computerM) :
    '''asd
    asd'''
    print("funRun")
    if playerM == "a" :
     if computerM == "a" : 
        result = 1
     elif computerM == "b" :
        result = 2
     else :
        result = 3
    elif playerM == "b" :
        if computerM == "b" :
            result = 1
        elif computerM == "c" :
            result = 2
        else :
            result = 3
    else :
      if computerM == "c" :
        result = 1
      elif computerM == "a" :
        result = 2
      else :
        result = 3
    return(result)
result = movecompare(playerIn,computerIn)
print(result)