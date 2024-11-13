def solvePartOne(frequencyList):
    result = 0
    for freq in frequencyList:
        result += int(freq)
    return result

def solvePartTwo(frequencyList):
    resultList = []
    result = 0
    while True:
        for freq in frequencyList:
            result += int(freq)
            if result in resultList:
                return result
            else:
                resultList.append(result)

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

frequencys = []

for line in Lines:
    input_line= line.strip()
    frequencys.append(input_line)


print("TASK 1 - frequency: {}".format(solvePartOne(frequencys)))

print("TASK 2 - frequency: {}".format(solvePartTwo(frequencys)))
