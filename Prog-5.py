import pandas as pd
import numpy as np

# Sample dictionary data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'Suresh', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

# Index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:\n")
print(df)

# Insert new column 'age'
df['age'] = [21, 23, 22, 20, 21, 24, 23, 22, 20, 25]

print("\nDataFrame after inserting new column:\n")
print(df)
