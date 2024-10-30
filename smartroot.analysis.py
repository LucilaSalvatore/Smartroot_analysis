#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:08:31 2024

@author: salva013
"""

import pandas as pd


# Read the CSV file into a DataFrame
df = pd.read_csv('LNLN.15mm.5.csv') #here you should change every time you are going to use with the name of the file you want python to open

# Extract the matrix
original_matrix = df.values

print(original_matrix)



# New matrix to store the extracted values
new_matrix = []

# Create a dictionary to store summed values
sum_dict = {}

# Iterate over each row in the original matrix
for row in original_matrix:
    if row[9] == 0: #this numer indicates the column where the 1/0 is (so the role of lateral or primary you should modify this)
        value_to_extract = row[3] #(this 2 should indicate the numeber where the length of the root is)
        col_2_value = row[1] #(this should be replace for the column where the name of the primary root is)
        string = row[1] #the same than before
        col_4_value = row[15] #This should be the number of the column where the number of LR of the parental is
        

        # Add extracted value to new matrix
        new_matrix.append([col_2_value, value_to_extract, 0, col_4_value])
        
        # Find rows in original matrix with same string and sum their values
        for orig_row in original_matrix:
            if orig_row[11] == string: #this should be the number of the column where the name of the parental root is in the ones that are LR
                if string not in sum_dict:
                    sum_dict[string] = []
                sum_dict[string].append(orig_row[3]) #This two is for the length of the root 

# Calculate sum of values and add to new matrix
for key, values in sum_dict.items():
    total_sum = sum(values)
    for new_row in new_matrix:
        if new_row[0] == key:
            new_row[2] = total_sum
            
#add labels to each column

new_matrix_label = [["root_name", "root_length", "Lateral_root_length", "Lateral_root_numer"]] + new_matrix



# Print the new matrix
for row in new_matrix_label:
    print(row)
    
df = pd.DataFrame(new_matrix_label)
csv_file = "LNLN.15mm.5.result.csv" #here you should change everytime with the name of the result file you want this to be saved.
df.to_csv(csv_file, index=False, header=False)