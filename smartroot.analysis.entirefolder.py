#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:55:04 2024

@author: salva013
"""

import os
import pandas as pd

# Set the path to your folder containing the CSV files
folder_path = "/users/salva013/Pictures/Splitroot.NitrogenvsCarbon/0.3mMvs15mM.rep2/smartroot.data"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing {filename}...")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Extract the matrix
        original_matrix = df.values

        # New matrix to store the extracted values
        new_matrix = []
        sum_dict = {}

        # Iterate over each row in the original matrix
        for row in original_matrix:
            if row[9] == 0:
                value_to_extract = row[3]
                col_2_value = row[1]
                string = row[1]
                col_4_value = row[15]

                # Add extracted value to new matrix
                new_matrix.append([col_2_value, value_to_extract, 0, col_4_value])

                # Find rows in original matrix with same string and sum their values
                for orig_row in original_matrix:
                    if orig_row[11] == string:
                        if string not in sum_dict:
                            sum_dict[string] = []
                        sum_dict[string].append(orig_row[3])

        # Calculate sum of values and add to new matrix
        for key, values in sum_dict.items():
            total_sum = sum(values)
            for new_row in new_matrix:
                if new_row[0] == key:
                    new_row[2] = total_sum

        # Add labels to each column
        new_matrix_label = [["root_name", "root_length", "Lateral_root_length", "Lateral_root_number"]] + new_matrix

        # Convert the new matrix to a DataFrame
        result_df = pd.DataFrame(new_matrix_label)

        # Save the result to a new CSV file with "_result" appended to the original filename
        result_filename = filename.replace(".csv", "_result.csv")
        result_path = os.path.join(folder_path, result_filename)
        result_df.to_csv(result_path, index=False, header=False)