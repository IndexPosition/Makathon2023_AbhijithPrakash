n, m = map(int, input().split())

c = (n-1)+(m-1)
"""
So when we take: 
    n , m as 3, 3 
    We cut the paper in 4 pieces to get the 1x1 squares.
Like wise when we take:
    n , m as 2, 2
    We cut the paper in 2 pieces to get the 1x1 squares.
Similarly:
    n , m as 5, 3
    We cut the paper in 6 pieces to get the 1x1 squares.

So to find the number of cuts needed we have to subtract 1 from each of the numbers, and then add them. Because the shape getting cut 2 times to get 3 pices, and 4 times to get 5 pieces. THere the formula (n-1)+(m-1)
"""
print(c)
