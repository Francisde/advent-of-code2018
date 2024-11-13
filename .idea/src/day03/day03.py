from util.util import print2D

def solvePartOne(inputFabric, inputClaims):
    for claim in claims:
        claim = claim.replace("#", "")
        claim = claim.replace("@ ", "")
        claim = claim.replace(",", " ")
        claim = claim.replace("x", " ")
        claim = claim.replace(":", "")
        claimValues = claim.split(" ")
        for i in range(int(claimValues[2]), int(claimValues[2]) + int(claimValues[4])):
            for j in range(int(claimValues[1]), int(claimValues[1]) + int(claimValues[3])):
                if inputFabric[i][j] == ".":
                    inputFabric[i][j] = claimValues[0]
                else:
                    inputFabric[i][j] = "X"
    result = 0
    for row in inputFabric:
        for entry in row:
            if entry == "X":
                result += 1
    return result

def solvePartTwo(inputFabric, inputClaims):
    for claim in claims:
        claim = claim.replace("#", "")
        claim = claim.replace("@ ", "")
        claim = claim.replace(",", " ")
        claim = claim.replace("x", " ")
        claim = claim.replace(":", "")
        claimValues = claim.split(" ")
        intact = True
        for i in range(int(claimValues[2]), int(claimValues[2]) + int(claimValues[4])):
            for j in range(int(claimValues[1]), int(claimValues[1]) + int(claimValues[3])):
                if inputFabric[i][j] == claimValues[0]:
                    pass
                else:
                    intact = False
        if intact:
            return claimValues[0]


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

claims = []

for line in Lines:
    input_line= line.strip()
    claims.append(input_line)

fabricDimension = 1001
fabric = [["." for i in range(fabricDimension)] for j in range(fabricDimension)]


print("TASK 1 - solution: {}".format(solvePartOne(fabric, claims)))


print("TASK 2 - solution: {}".format(solvePartTwo(fabric, claims)))
