def addNumToDict(d,num):
    '''

    :param d: Dictionary
    :param num: num to add
    :return: None
    '''
    if d.get(num) == None:
        d[num] = 1
    else: d[num] +=1


numCount = 0
multiCount = 0
numSet = set()
usrInput = 0
numDict = {}

while True:
    usrInput = int(input("Please enter a number: "))
    if usrInput == -1:
        break
    if usrInput in numSet:
        multiCount += 1
    numSet.add(usrInput)
    numCount += 1
    addNumToDict(numDict, usrInput)

print(f'The user entered {numCount} numbers in total, has entered an existing number {multiCount} times.')
print(f'The numbers entered were: {numSet}')
for num in sorted(list(numDict.keys())):
    print(f'The number {num} was entered {numDict[num]} times' )
