def runner_001():
    d = 1
    su = 0
    while su < 1000:
        sut=2**d
        d +=1
        su +=sut
    return d

print(runner_001())
#############################################
def runner_002():
    s = 10
    d = 0
    itogo = 0
    while d <= 30:
        d +=1
        if d % 2:
            itogo += s +0.15*s
        else:
            itogo +=s
    return itogo

print(runner_003())
#############################################
def runner_004():
    s = 10
    d = 0
    itogo = 0
    while itogo <=100:
        d += 1
        itogo += s
        s += s*0.1
    return d

print(runner_004())
#############################################
def runner_005():
    s = 10
    d = 0
    while s <= 100:
        d += 1
        s += s*0.1
    return d

print(runner_005())