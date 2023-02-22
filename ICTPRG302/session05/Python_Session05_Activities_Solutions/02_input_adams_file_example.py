'''
This program will open a text file (addams.txt) and display the contents to the screen
'''

# Pseudocode
# Program input_adams_file_example
#   OPEN "addams.txt" FOR INPUT AS input_file
#
#   FOR EACH line IN input_file
#     OUTPUT line
#   END FOR
#
#   CLOSE input_file
# END


def main():
    # Open the file
    input_file = open("addams.txt", "r")

    # Loop reading the lines of the file,
    # and print each line out
    for line in input_file:
        print(line, end=' ')

    # Now close the file
    input_file.close()


main()
