import pandas as pd
from functions import normalize_value, unnormalise_value, get_r2_precision, get_estimatePrice
#############################################################################################################################################################################################################################################

mileage = input("So you want the price of your car, please enter a mileage:\n")
data = pd.read_csv('data.csv', delimiter=",", dtype="float")
P_raw = data["price"].values
K_raw = data["km"].values

try:
   miles = int(mileage)
   if (miles < 0): 
      print("Please, enter a valid mileage if you want the algorithm to work...")
      exit()
except ValueError:
   print("Please, enter a valid mileage if you want the algorithm to work...")
   exit()

try:
    f = open("theta.txt","r")
    t0 = float(f.readline())
    t1 = float(f.readline())
    if (miles < 20000 or miles > 250000):
        print("\n /!\ We do not have good data to train for that mileage, the price will be more than approximative /!\ ")
    price = int(get_estimatePrice(normalize_value(miles, K_raw), t0, t1, P_raw))
    r2 = get_r2_precision(P_raw, K_raw, t0, t1)
    boo = 1
    if (price < 0):
        price = 0
except Exception as e:
    print("\n/!\ The algorithm was not trained, think about training it!\n")
    t0 = 0
    t1 = 0
    boo = 0
    price = t0 + t1 * miles

print("\nFor " + str(mileage) + "km, the price is around: " + str(price) + "$")
if (boo == 1):
    print("\nPrecision:")
    print("R^2 = " + str(r2) + "%")

###############################################################################################################################################################################################################################################