from numpy.ma.core import minimum_fill_value


def solvePartOne(boxesList):
    boxesWithTwoRep = 0
    boxesWithThreeRep = 0
    for item in boxesList:
        res = getLetterCount(item)
        if res[0]:
            boxesWithTwoRep += 1
        if res[1]:
            boxesWithThreeRep += 1
    return boxesWithTwoRep * boxesWithThreeRep

def getLetterCount(inputString):
    letters = set(list(inputString))
    two = False
    three = False
    for letter in letters:
        if inputString.count(letter) == 2:
            two = True
        elif inputString.count(letter) == 3:
            three = True
    return (two, three)

def solvePartTwo(boxesList):
    minValue = 100
    minBox1 = None
    minBox2 = None
    for box1 in boxesList:
        for box2 in boxesList:
            if box1 != box2:
                diff = getLetterDif(box1, box2)
                if diff < minValue:
                    minValue = diff
                    minBox1 = box1
                    minBox2 = box2
    result = ""
    for i in range(len(minBox1)):
        if minBox1[i] == minBox2[i]:
            result += minBox1[i]
    return result

def getLetterDif(box1, box2):
    diff = 0
    for i in range(len(box1)):
        if box1[i] != box2[i]:
            diff += 1
    return diff




file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

boxes = []

for line in Lines:
    input_line= line.strip()
    boxes.append(input_line)



print("TASK 1 - checksum: {}".format(solvePartOne(boxes)))

print("TASK 2 - common letters: {}".format(solvePartTwo(boxes)))
