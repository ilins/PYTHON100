def sequence_001():
    n = 10
    list = [1,1]
    for i in range(2,n):
        list.append(list[-1] + list[-2])
    return  list[3]

print(sequence_001())
##################################################
def sequence_002():
    n = 10
    list = [1,1,1]
    for i in range(3,n):
        list.append(list[-1] + list[-2] + list[-3])
    return list[3]

print(sequence_002())
###################################################
def sequence_003():
    print('Input natural number: ')
    n = int(input())
    l = []
    result = [i ** 2 for i in range(1, n + 1, 2)]
    return  result

print(sequence_003())
###################################################
def allegrova_004():
    print('The function allegrova will give you the frame 9*12: ')
    for i in range(9):
        if i == 0 or i == 8:
            for j in range(12):
                print('*', end='')
        else:
            print('*', end='')
            for j in range(1,11):
                print(' ', end='')
            print('*', end='')
        print()
    return
allegrova_004()
###################################################