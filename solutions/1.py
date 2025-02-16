"""
Create 3 variables, assign then numbers and do the following:
1. get the sum of the variables
2. get the product of the variables
3. calculate the mean
4. print the sum, product, and mean to the console
   format sum: the sum, product: the product, mean: the mean
"""

# solution 1
a = 2
b = 4
c = 7

total = a + b + c
product = a * b * c
mean = total/3

print("sum:", total, "product:", product, "mean:", mean)

# solution 2
a, b, c = 2, 4, 7
total = sum([a,b,c])
product = a*b*c
mean = total/3
print(f"Total: {total}, Product: {product}, Mean: {mean}")