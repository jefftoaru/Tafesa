# assign constants
TAX_RATE = 0.25

# input
gross_pay = float(input("Enter gross pay: "))  # enter the grossPay as a decimal value

# processing
tax_payable = gross_pay * TAX_RATE
nett_pay = gross_pay - tax_payable

# output
print("The tax payable is $", tax_payable)
print("The nett pay is $", nett_pay)
