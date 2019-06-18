import numpy as np
import matplotlib.pyplot as plt
from functions import unnormalise_value, estimatePrice

def print_graph(X, Y, t0, t1):  
    # plotting points as a scatter plot 
    plt.scatter(X, Y, label= "Raw Values", color= "blue", marker= "o", s=30) 
    
    # getting the good data to plot the line
    x = np.linspace(22000, 250000, 10) 
    val = (np.linspace(22000, 250000, 10) - X.mean()) / (X.max() - X.min())
    y = Y.mean() + (t0 + val * t1) * (Y.max() - Y.min())
    
    # plotting line 
    plt.plot(x, y, '-r', label="Linear Regression")

    # x-axis label 
    plt.xlabel('Mileage') 
    # frequency label 
    plt.ylabel('Price') 
    # plot title 
    plt.title('Prices by mileage - Linear Regression') 
    # showing legend 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 
