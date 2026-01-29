mat1=[
    [1,2,3],
    [4,5,6]
]

res=[
    [0,0],
    [0,0],
    [0,0]
]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        res[j][i]=mat1[i][j]

print(res)