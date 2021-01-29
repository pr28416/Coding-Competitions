def sumSmallestInVisitedCells(rows_cols, array1, array2, array3):

    # Note: Was receiving error for test case 7 for getting input
    # for rows_cols with a space at the end, so I had to strip
    # spaces. The input should probably be rechecked by ACSL.
    r, c = map(int, rows_cols.strip(" ").split(" "))

    line = list(map(int, array1.split(" ")))
    array1 = [line[c*i:c*(i+1)] for i in range(r)]
    line = list(map(int, array2.split(" ")))
    array2 = [line[c*i:c*(i+1)] for i in range(r)]
    line = list(map(int, array3.split(" ")))
    array3 = [line[c*i:c*(i+1)] for i in range(r)]

    r = c = 0
    s = 0
    while True:
        s += min(array1[r][c], array2[r][c], array3[r][c])

        if not (r < len(array1)-1 and c < len(array1[0])-1):
            break

        points = [
            (array1[r+1][c], r+1, c),
            (array1[r][c+1], r, c+1),
            (array2[r+1][c], r+1, c),
            (array2[r][c+1], r, c+1),
            (array3[r+1][c], r+1, c),
            (array3[r][c+1], r, c+1),
        ]

        points.sort(key=lambda x: -x[0])

        if points[0][0] == points[1][0]:
            r += 1
            c += 1
        else:
            r, c = points[0][1], points[0][2]

    return s
        
rows_cols = "3 4"
array1 = "1 2 3 4 7 7 8 9 5 6 7 8"
array2 = "6 8 6 4 4 5 3 2 8 3 1 9"
array3 = "3 6 7 3 4 6 2 1 3 2 5 5"

result = sumSmallestInVisitedCells(rows_cols, array1, array2, array3)
print(result)