import pandas as pd

###############################################################################################################################################################################

def estimatePrice(mileage, t0, t1):
    result = float(t0 + (mileage * t1))
    return (result)

###############################################################################################################################################################################

data = pd.read_csv('data.csv', delimiter=",", dtype="float")
#print(data.shape)
#print(data.head)

P = data["price"].values
K = data["km"].values
lr = 0.00000001
iteration = 100
m = len(P)


tmp0 = 0
tmp1 = 0
for step in range(iteration):
    sum_t0 = 0
    sum_t1 = 0
    for i in range(m):
        sum_t0 += estimatePrice(K[i], tmp0, tmp1) - P[i]
        sum_t1 += (estimatePrice(K[i], tmp0, tmp1) - P[i]) * K[i]
    tmp0 = tmp0 + lr * (sum_t0 / m)
    tmp1 = tmp0 + lr * (sum_t1 / m)


t0 = tmp0
t1 = tmp1

print("t0: ", t0)
print("t1: ", t1)

##############################################################################################################################################################################
'''
Create teta file with t0 and t1
'''
#f = open("teta.txt", "w")
#f.write(str(t0) + "\n" + str(t1) + "\n")