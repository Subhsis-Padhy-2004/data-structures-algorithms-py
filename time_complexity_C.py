n = int(input("Enter the value of I --->"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(i,j)

        # time complexity
        # N(N+1)/2-->O(n^2)