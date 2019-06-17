#############################################################################################################################################################################################################################################

mileage = input("So you want a price of your car, please enter a mileage:\n")

try:
   val = int(mileage)
except ValueError:
   print("Please, enter a valid mileage if you want the algorithm to work ...")
   exit()

try: 
    f = open("teta.txt","r")
    t0 = f.readline()
    t1 = f.readline()
    if (mileage < 40000 or mileage > 250000):
        print("We do not have good data to train for that mileage, the price will be more than approximative")
except Exception as e:
    print("The data set was not trained, think about training it!\n")
    t0 = 0
    t1 = 0

price = t0 + t1 * int(mileage)

print("For " + str(mileage) + " km, the price is around: " + str(price))