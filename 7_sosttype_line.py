def stringn_001():
    print('Input natural number: ')
    a = int(input())
    print('Input string: ')
    s = str(input())
    return s*a
print(stringn_001())
#################################
def stairs_002():
    print('Input natural number: ')
    n = int(input())
    c = str('=')
    for i in range(1,n+1):
        print(c*i)
    return

stairs_002()
# ##############################################
def count_003():
    s = str('asdqasqwe')
    d = {}
    a = sorted(set(s))
    for i in sorted(set(s)):
        d[str(i)] = s.count(i)
    return d
print(count_003())
# ###########################################
def words_004():
    print('Enter a few words separated by spaces: ')
    s = input(str())
    d={}
    for i in s.split():
        k = 'words with ' + str(len(i)) + ' symbols'
        if k in d.keys():
            d[k]+=1
        else:
            d[k] = 1
    return d
print(words_004())
###############################################