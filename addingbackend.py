def get_sumOfMatrices(matA, matB):
    matSum = []
    for i in range(len(matA)):
        rowSum = []
        for j in range(len(matA[0])):
            element_sum = int(matA[i][j]) + int(matB[i][j])
            rowSum.append(element_sum)
        matSum.append(rowSum)
    return matSum