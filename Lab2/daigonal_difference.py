def diagonalDifference(arr):
    # Write your code here
    main = [arr[i][i] for i in range(len(arr))]
    anti = [arr[len(arr)-1-i][i] for i in range(len(arr))]
    print(main)
    print(anti)
    return abs(sum(main)-sum(anti))

