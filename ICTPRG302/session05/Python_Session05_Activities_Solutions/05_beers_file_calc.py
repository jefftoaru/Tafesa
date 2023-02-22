'''
This program will open a text file (beers.txt) and display the contents to the screen. It will then request a beer name
and append this name back to the file
'''

# Pseudocode
# Program beers_file_calc
#   OPEN "Beers.txt" FOR INPUT AS input_file
#
#   FOR EACH line IN input_file
#     OUTPUT line
#   END FOR
#
#   CLOSE input_file
#
#   INPUT new_beer
#   OPEN "Beers.txt" FOR APPEND AS output_file
#   write new_beer TO output_file
#   CLOSE output_file
# END

import datetime

def main():
    input_file = open("Beers.txt", "r")

    my_date= datetime.datetime.today()
    todays_date = my_date.strftime('%A %B %d, %Y')

    print(f"Date: {todays_date:s}\n")

    for line in input_file:
        print(line, end='')

    input_file.close()

    new_name = input("\nEnter your new beer:")
    output_file = open("Beers.txt", "a")
    output_file.write(new_name)
    output_file.write("\n")
    output_file.close()


main()
