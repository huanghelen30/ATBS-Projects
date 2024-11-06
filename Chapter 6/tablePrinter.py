# Display a given list of list of strings in a right-justified table

def printTable(tableData):
    # Calculate the maximum width of each column
    colWidths = [0] * len(tableData)  # Create a list to store the width of each column

    # Determine the maximum width for each column
    for i in range(len(tableData)):
        for item in tableData[i]:
            colWidths[i] = max(colWidths[i], len(item))  # Update the width for the current column

    # Print each row of the table
    for row in range(len(tableData[0])):  # Iterate through the rows
        for col in range(len(tableData)):  # Iterate through the columns
            # Print the right-justified string for each item in the row
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()  # Move to the next line after printing each row

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
