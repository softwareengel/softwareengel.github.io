def minimum_aus_3_zahlen(x1,x2,x3):
    if x2< x3:
        if x1<x2:
            return x1
        else:
            return x2
    else:
        if x1 < x3:
            return x1
        else:
            return x3

minimum = minimum_aus_3_zahlen (12,32,2) 
