def print_csv_table(filename):
    """
    Reads a CSV file and prints the data in a formatted table.

    Args:
    filename: name of the CSV file

    Returns:
    None
    """

    # Open the CSV file for reading
    with open(filename, 'r') as f:

        # Read the header row and store the column names
        header = f.readline().strip().split(',')

        # Read the remaining rows and store the data in a list of dictionaries
        data = []
        for line in f:
            values = line.strip().split(',')
            row = {}
            for i in range(len(header)):
                row[header[i]] = values[i]
            data.append(row)

    # Determine the maximum width for each column
    col_widths = {}
    for row in data:
        for col_name in header:
            col_widths[col_name] = max(col_widths.get(col_name, 0), len(row.get(col_name, '')))

    # Print the header row
    print('+' + '-' * (sum(col_widths.values()) + len(col_widths) - 1) + '+')
    print('| ' + ' | '.join([col_name.ljust(col_widths[col_name]) for col_name in header]) + ' |')
    print('+' + '-' * (sum(col_widths.values()) + len(col_widths) - 1) + '+')

    # Print the data rows
    for row in data:
        print('| ' + ' | '.join([str(row.get(col_name, '')).ljust(col_widths[col_name]) for col_name in header]) + ' |')

    # Print the bottom border
    print('+' + '-' * (sum(col_widths.values()) + len(col_widths) - 1) + '+')

print_csv_table('data.csv')
