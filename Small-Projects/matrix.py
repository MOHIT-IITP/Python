rows=int(input("Enter the number of rows :"))
cols = int(input("Enter the number of cols: "))
matrix = []
def matrix_input(rows, cols):
    for i in range(rows):
        row=[]
        for j in range(cols):
            element = int(input("Enter the elements : "))
            row.append(element)
        matrix.append(row)
    print(matrix)
matrix_input(rows,cols)

            