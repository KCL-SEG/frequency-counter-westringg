"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        items[i] = str(items[i])
    print(items)

    for item in items:
        isExist = False
        for key in frequencies.keys():
            if item == key:
                isExist = True
                curCount = frequencies[item]
                frequencies.update({item:curCount+1})
                #print('curCount', curCount)
        if not isExist:
            frequencies.update({item:1})
        
    return frequencies

#print(frequencies([100, 'Hello', '100', '100', 100]))