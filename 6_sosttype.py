def sosttype_001(n):
    result = [i for i in range(1,9)]
    return result
print(sosttype_001(8))
#################################################
def sosttype_002(n):
    result = [i+1 for i in sosttype_001(8)]
    return result
print(sosttype_002(8))
#################################################
def sosttype_003(n):
    full = sosttype_001(8) + sosttype_002(8)
    cp_full = full.copy()
    cp_full.sort()
    secmaxelement = cp_full[-2]
    ind = cp_full.index(secmaxelement)
    result = full[ind:-1]
    return result
print(sosttype_003(sosttype_001(8)+sosttype_002(8)))
#################################################
def sosttype_004(n):
    full = sosttype_001(8) + sosttype_002(8)
    result = [i for i in full if i % 3 == 1]
    return result
print(sosttype_004(sosttype_001(8) + sosttype_002(8)))
#################################################
def sosttype_005(n):
    full = sosttype_001(8) + sosttype_002(8)
    full_new = full[2:5]
    result = [round(i/3) for i in full_new]
    return result
print(sosttype_005(sosttype_001(8) + sosttype_002(8)))