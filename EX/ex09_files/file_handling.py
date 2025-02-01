"""Files."""

import csv


def mesh_two_list_to_csv_file(list1: list, list2: list, filename: str):
    """
    Merge two lists together into a CSV file, as if one list is on the left side and other on the right.

    Both lists have the same number of rows. Make two lists into one without disarranging any row or column.
    """
    combined_rows = zip(list1, list2)  # два в один
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(combined_rows)


def replace_vowels_in_file(input_file: str, output_file: str):
    """
    Replace all vowels in the text with an asterisk (*).

    This function finds all vowels (AEIOUaeiou) in the input text and replaces them with an asterisk (*).
    """
    vowels = "AEIOUaeiou"

    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)

        with open(output_file, 'w', newline='') as new_file:
            for line in reader:  # line and reader are lists!!!
                for word in line:  # поэтому еще в sõna
                    result = ''.join(map(lambda char: '*' if char in vowels else char, word))
                    new_file.write(result)  # write() argument must be str, not list


def reverse_rows_in_csv_file(input_file: str, output_file: str):
    """
    Reverse the order of rows in a CSV file.

    This function reads the content of an input CSV file and writes it to an
    output CSV file with the rows in reverse order.
    """
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))  # типо выглядит [ [..], [...] ]

        with open(output_file, 'w', newline='') as newfile:
            writer = csv.writer(newfile)
            for row in reader[::-1]:
                writer.writerow(row)  # if write() you will get 456123


def swap_header_and_row_in_csv_file(header: list, row: list):
    """
    Swap the header row with a data row in a CSV file.

    This function takes a header row and a data row, swaps their positions,
    and writes them to a CSV file. If the data row is longer, it pads the header
    row with empty strings to match the length. The name of the output file should be "swapped_file.csv".
    """
    max_length = max(len(header), len(row))
    header.extend([''] * (max_length - len(header)))

    # result = [row, header] другой вариант

    with open('swapped_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerows(result)  это другой вариант
        writer.writerow(row)
        writer.writerow(header)


if __name__ == '__main__':
    mesh_two_list_to_csv_file(['data1', 'data2'], ['data3', 'data4'], 'mesh_two_list_to_csv_file.csv')

    with open('mesh_two_list_to_csv_file.csv', 'r') as file:
        reader = csv.reader(file)
        output = [row for row in reader]
        for row in output:
            print(','.join(row))
    # data1,data3
    # data2,data4
    print('\n')

    with open('replace_vowels_in_file_input.txt', 'w') as file:
        file.write('Hello World')

    replace_vowels_in_file('replace_vowels_in_file_input.txt', 'replace_vowels_in_file_output.txt')

    with open('replace_vowels_in_file_output.txt', 'r') as file:
        print(file.read() + "\n")
    # "H*ll* W*rld"

    with open('reverse_rows_in_csv_file_input.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['1', '2', '3'])
        writer.writerow(['4', '5', '6'])

    reverse_rows_in_csv_file('reverse_rows_in_csv_file_input.csv', 'reverse_rows_in_csv_file_output.csv')
    with open('reverse_rows_in_csv_file_output.csv', 'r') as file:
        print(file.read())
    # 4,5,6
    # 1,2,3

    swap_header_and_row_in_csv_file(['A', 'B', 'C'], [1, 2, 3, 4])
    with open('swapped_file.csv', 'r') as file:
        print(file.read())
    # 1,2,3,4
    # A,B,C,
    import os

    os.remove('mesh_two_list_to_csv_file.csv')
    os.remove('replace_vowels_in_file_input.txt')
    os.remove('replace_vowels_in_file_output.txt')
    os.remove('reverse_rows_in_csv_file_input.csv')
    os.remove('reverse_rows_in_csv_file_output.csv')
    os.remove('swapped_file.csv')
