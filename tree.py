# i=16
# row=63
# column=49

# 1st line: |

# grid[62,49]=1
# grid[61,49]=1
# grid[60,49]=1
# grid[59,49]=1
# grid[58,49]=1
# grid[57,49]=1
# grid[56,49]=1
# grid[55,49]=1
# grid[54,49]=1
# grid[53,49]=1
# grid[52,49]=1
# grid[51,49]=1
# grid[50,49]=1
# grid[49,49]=1
# grid[48,49]=1
# grid[47,49]=1

# grid[47,49]=1
# grid[48,49]=1
# grid[49,49]=1
# grid[50,49]=1
# grid[51,49]=1
# grid[52,49]=1
# grid[53,49]=1
# grid[54,49]=1
# grid[55,49]=1
# grid[56,49]=1
# grid[57,49]=1
# grid[58,49]=1
# grid[59,49]=1
# grid[60,49]=1
# grid[61,49]=1
# grid[62,49]=1

# 2nd line: \ /

# for row=row-length:

#     \

#     grid[46,48]=1
#     grid[45,47]=1
#     grid[44,46]=1
#     grid[43,45]=1
#     grid[42,44]=1
#     grid[41,43]=1
#     grid[40,42]=1
#     grid[39,41]=1
#     grid[38,40]=1
#     grid[37,39]=1
#     grid[36,38]=1
#     grid[35,37]=1
#     grid[34,36]=1
#     grid[33,35]=1
#     grid[32,34]=1
#     grid[31,33]=1

# grid[31,33]=1
# grid[32,34]=1
# grid[33,35]=1
# grid[34,36]=1
# grid[35,37]=1
# grid[36,38]=1
# grid[37,39]=1
# grid[38,40]=1
# grid[39,41]=1
# grid[40,42]=1
# grid[41,43]=1
# grid[42,44]=1
# grid[43,45]=1
# grid[44,46]=1
# grid[45,47]=1
# grid[46,48]=1

#     /

#     grid[46,50]=1
#     grid[45,51]=1
#     grid[44,52]=1
#     grid[43,53]=1
#     grid[42,54]=1
#     grid[41,55]=1
#     grid[40,56]=1
#     grid[39,57]=1
#     grid[38,58]=1
#     grid[37,59]=1
#     grid[36,60]=1
#     grid[35,61]=1
#     grid[34,62]=1
#     grid[33,63]=1
#     grid[32,64]=1
#     grid[31,65]=1

# grid[31,65]=1
# grid[32,64]=1
# grid[33,63]=1
# grid[34,62]=1
# grid[35,61]=1
# grid[36,60]=1
# grid[37,59]=1
# grid[38,58]=1
# grid[39,57]=1
# grid[40,56]=1
# grid[41,55]=1
# grid[42,54]=1
# grid[43,53]=1
# grid[44,52]=1
# grid[45,51]=1
# grid[46,50]=1

# 3rd and more:

#         |

# later:

#     \        /





# The tree function is a recursive function that takes in four arguments: depth, length, row, and column. 
# Depth represents the recursion depth, and length, row, and column represent the starting length, row position, and column position of the triangle.

# The function starts by checking if depth is zero. If it is, the function returns and the recursion ends. 
# Otherwise, the function uses a nested loop to fill in the positions in the grid dictionary corresponding to the current triangle. 
# The first loop fills in the top row of the triangle, and the second loop fills in the two bottom corners.

# After filling in the positions for the current triangle, the function recursively calls itself twice with depth decremented by one and length halved. 
# The first call calculates the position of the left triangle, and the second call calculates the position of the right triangle.

# The print_grid function takes in two arguments: row and all_columns. 
# It prints out the grid dictionary by looping through each position and printing either a 1 or _ depending on whether the position is filled or not.

# The main code reads in a value for n and calls the tree function with the starting parameters depth=n, length=16, row=63, and column=49. 
# Then, it calls the print_grid function with the parameters row=63 and all_columns=100 to print out the resulting tree.


grid = {}

def tree(depth, length, row, column):
    if depth == 0:
        return

    for i in range(length, 0, -1):
        grid[(row-i, column)] = 1

    row -= length

    for i in range(length, 0, -1):
        grid[(row-i, column-i)] = 1
        grid[(row-i, column+i)] = 1

    tree(depth-1, length//2, row-length, column-length)
    tree(depth-1, length//2, row-length, column+length)

def print_grid(row, all_columns):
    for i in range(row):
        for j in range(all_columns):
            if (i,j) in grid:
                print(1, end="")
            else:
                print("_", end="")
        print()

n = int(input())
tree(n, 16, 63, 49)
print_grid(63, 100)


