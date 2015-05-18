#Created on 2014-21-03
#edited 2014-04-28
#Author: Monica Tsang 
#Use:  To test the number of lines from a file

# Reference:
# Ahmad & Dey (2007) - A k-Means Clustering Algorithm for Mixed Numerical and Categorical Data

import numpy as np
import math
#import Tkinter, tkFileDialog
import random

#root = Tkinter.Tk()
#root.withdraw()
"""
    x    y
a    1    1
b    5    6
c    5    4
d    2    2
e    2    1
f    6    5
g    1    2
h    7    4
"""

myArray= [["a","a","a","a","a","a"],
          ["a","a","a","a","b","b"],
          ["a","a","a","a","b","c"],
          ["b","b","a","a","b","c"],
          ["b","b","a","a","d","e"]]

'''def hamming_seed(myArray,k):
'''    

def hamming_dist(list1,list2):
    
    hamm_dist = 0
    
    ham_dim = len(list1)
    
    #for each dimension 
    for x in range (0, ham_dim):
        # if not the same, increase Hamming Distance 
        if list1[x] != list2[x]:
            hamm_dist += 1
            
    return hamm_dist

def hamming_centroid(myArray):
    
    hamm_centroid = []
    
    num_ppl = len(myArray)
    ham_dim = len(myArray[0])
    
    
    for x in range (0, ham_dim): # columns
        # create associative array
        hamm_dict  = {} 
        
        # key_freq_max
        key_freq_max = 0
        
        # key_freq_num
        key_freq_num = 0
        
        # initialising keys 
        for y in range (0, num_ppl): # rows
            hamm_dict [myArray[y][x]] = 0 # gets all key to use for dictionary           (because each key is unique, only one)
        
            
        # compare existing to keys, add 1 
        for y in range (0, num_ppl):
            key = myArray[y][x]
            hamm_dict[key] += 1 
            #keep track
            
            if hamm_dict[key] > key_freq_num:
                key_freq_num = hamm_dict[key]
                key_freq_max = key
            
        hamm_centroid.append(key_freq_max)    

    return hamm_centroid
        #assign associative arrays
            
jason = hamming_centroid(myArray)

print(jason)

print(myArray)

print(hamming_dist(myArray[0],myArray[4]))
# check the number of types of items in each category

# for each new category in the file, assign 


# assign letter to each 