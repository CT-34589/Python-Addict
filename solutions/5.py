"""
create a function to return the number of appearances of numbers in a list
e.g [1,2,3,4,5,1,2,3,4,1,2,3,1,2,1] -> {1:5, 2:4, 3:3, 4:2, 5:1}
"""

def appearances(lst):
    appearances = {}
    for i in lst:
        if i in appearances:
            appearances[i] += 1
        else:
            appearances[i] = 1
    return appearances



if __name__ == "__main__":
    print(appearances([1, 2, 5, 1, 1, 1, 3, 3, 2, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]))
    print(appearances([1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1]))




"""
Test case -> Expected output
[1, 2, 5, 1, 1, 1, 3, 3, 2, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5] -> {1:6, 2:4, 5:3, 3:4, 7:2, 8:2, 9:2, 4:2, 6:1}
[1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1] -> {1:5, 2:4, 3:3, 4:2, 5:1}
"""