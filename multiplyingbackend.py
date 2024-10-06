def get_productOfMatrices(matA, matB):
    matProduct = []
    for i in range(len(matA)):
        rowProduct = []
        for j in range(len(matB[0])):
            element_product = 0
            for k in range(len(matA[0])):
                element_product += int(matA[i][k]) * int(matB[k][j])
            rowProduct.append(element_product)
        matProduct.append(rowProduct)
    return matProduct
