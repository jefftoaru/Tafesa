'''
This program will read in 5 employees’ hours of work (integers) from the text file EmpHours.txt.
It will calculate the employees pay as the hours multiplied by the pay rate of $27.50 per hour and
output the hours and pay to the screen.
'''

# Pseudocode
# Program payroll_file_calc
#
#   PAY_RATE = 27.5
#
#   OPEN "EmpHours.txt" FOR INPUT AS input_file
#
#   OUTPUT heading
#
#   FOR EACH line IN input_file
#       hours = line
#       pay = hours * PAY_RATE
#       OUTPUT hours, pay
#   END FOR
#
#   CLOSE input_file
#

# END

def main():
   PAY_RATE = 27.5

   input_file = open("EmpHours.txt", "r")

   print('{:>5}{:>10}' .format('Hours','Pay')) # this allocates 5 positions for the
                        # first heading and 10 positions for the
                        # second heading and right aligns them(>)

   for line in input_file:
      hours = int(line)
      pay = hours * PAY_RATE
      print(f"{hours:5d}{pay:10.2f}")

   input_file.close()

main()
# print (PAY_RATE) # Cannot access PAY_RATE here as it is only in scope inside main()