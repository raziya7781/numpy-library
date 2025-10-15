import pandas as pd

# Create a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])

print("Pandas Series:")
print(data)

# Convert to Python list
python_list = data.tolist()

print("\nConverted Python List:")
print(python_list)

# Display type
#print("\nType of converted object:", type(python_list))
