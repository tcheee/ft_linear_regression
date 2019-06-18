import pandas as pd
from functions import estimatePrice
from functions import normalize_data
from graphic import print_graph
###############################################################################################################################################################################
data = pd.read_csv('data.csv', delimiter=",", dtype="float")
P_raw = data["price"].values
K_raw = data["km"].values
lr = 0.2
iteration = 700
m = len(P_raw)
P = normalize_data(P_raw)
K = normalize_data(K_raw)

tmp0 = 0
tmp1 = 0
for step in range(iteration):
    sum_t0 = 0
    sum_t1 = 0
    for i in range(m):
        sum_t0 += estimatePrice(K[i], tmp0, tmp1) - P[i]
        sum_t1 += (estimatePrice(K[i], tmp0, tmp1) - P[i]) * K[i]
    tmp0 = tmp0 - (lr/m) * sum_t0
    tmp1 = tmp1 - (lr/m) * sum_t1 

##############################################################################################################################################################################
#Create teta file with t0 and t1
f = open("theta.txt", "w")
f.write(str(tmp0) + "\n" + str(tmp1) + "\n")

ans = input('Do you want a graph to visualize the data, yes/no? : ')
if (ans == "yes"):
    print_graph(K_raw, P_raw, tmp0, tmp1)