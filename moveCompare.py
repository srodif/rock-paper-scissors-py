print("Hello")
playerM = "a"
computerM = "b"
result = 1
print(result)
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

print(result)