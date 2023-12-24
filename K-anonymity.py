import pandas as pd
import numpy as np

# Create DataFrame from provided data
data = {
    'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Name': ['Amber', 'Bill', 'Carol', 'David', 'Elaena', 'Frank', 'Garry', 'Hendrik', 'Immanuel', 'Jim', 'Kimberly', 'Ken', 'Mike', 'Merry', 'Nancy'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female'],
    'Postcode': [57678, 57678, 57678, 57905, 57909, 57906, 57605, 57673, 57607, 57607, 57906, 57907, 57908, 57678, 57678],
    'Age': [29, 22, 27, 43, 52, 47, 30, 36, 32, 42, 27, 23, 37, 54, 57],
    'Disease': ['Cardiac', 'Cardiac', 'Cardiac', 'Pulmonary', 'Pulmonary', 'Pulmonary', 'Cardiac', 'Cancer', 'Cancer', 'Pulmonary', 'Cardiac', 'Cardiac', 'Cancer', 'Pulmonary', 'Pulmonary']
}

df = pd.DataFrame(data)

def anonymize_data(df, k=3):
    # Group by Disease and Gender
    grouped = df.groupby(['Disease', 'Gender'])

    # Initialize an empty DataFrame for anonymized data
    anonymized_df = pd.DataFrame(columns=df.columns)

    # Iterate through each group
    for _, group_df in grouped:
        # Ensure each group has at least k records
        if len(group_df) >= k:
            # Select k records from the group
            sampled_group = group_df.sample(k)

            # Replace 'Name' and 'Postcode' with null values
            sampled_group['Name'] = "Null"
            sampled_group['Postcode'] = "Null"
            sampled_group['Patient_ID']= "Null"
            
            # Round 'Age' to the nearest 10 and create age ranges
            sampled_group['Age'] = ((sampled_group['Age'] - 1) // 10 * 10).astype(str) + ' to ' + (((sampled_group['Age'] - 1) // 10 * 10) + 10).astype(str)

            # Append to the anonymized DataFrame
            anonymized_df = pd.concat([anonymized_df, sampled_group])
    
    anonymized_df = anonymized_df.sort_values(by=['Patient_ID'])
    return anonymized_df

# Display the original and anonymized data
print("Original Data:")
print(df.to_string(index=False))

# Suppressing the data
anonymized_data = anonymize_data(df, k=3)

print("\nTable after Suppressing and Genralization Data:")
print(anonymized_data.to_string(index=False))