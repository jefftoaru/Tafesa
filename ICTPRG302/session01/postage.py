# constants
POSTAGE_RATE = 1.5

# input
weight = float(input("Enter the weight of the parcel: "))
# processing
postage_cost = weight * POSTAGE_RATE
# output
print("The postage cost is $",postage_cost)