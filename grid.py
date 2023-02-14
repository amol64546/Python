
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for row in grid:
#     for num in row:
#         print(num)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j],end="")