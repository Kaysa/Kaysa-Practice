def foo(temp):
    if temp > 25:
        return "Hot"
    elif 25 >= temp >= 15:
        return "Warm"
    else :
        return "Cold"

print(foo(46))

def foo(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

def foo(pass):
    if len(pass) >= 8:
        return True
    else:
        return False