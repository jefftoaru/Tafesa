'''
This program will read and output the student scores from the text file Scores.txt.
It will also calculate the total and average of all scores and
output the number of scores and average to the screen.
'''

# Pseudocode
# Program payroll_file_calc
#
#   total = 0
#   counter = 0
#
#   OPEN "Scores.txt" FOR INPUT AS input_file
#
#   OUTPUT heading
#
#   FOR EACH line IN input_file
#       scores = line
#       total = total + scores
#       counter = counter + 1
#       OUTPUT scores
#   END FOR
#
#   CLOSE input_file
#
#   average = total / counter
#   OUTPUT counter, average
# END

import datetime

def main():

   total = 0
   counter = 0

   my_date = datetime.datetime.today()
   todays_date = my_date.strftime('%d-%b-%Y')

   print(f"Date: {todays_date:s}\n")

   input_file = open("Scores.txt", "r")

   print('{:>5}' .format('Scores'))

   for line in input_file:
      score = float(line)
      total = total + score
      counter = counter + 1
      print(f"{score:5.2f}")

   input_file.close()

   average = total / counter
   print(f"The average score for these {counter:d} scores is {average:5.2f}")

main()
# print(f"The average score for these {counter:d} scores is {average:5.2f}")