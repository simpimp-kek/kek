import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': [28, 24, 32, 35, 29],
    'Salary': [50000, 55000, 70000, 65000, 60000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
}

df = pd.DataFrame(data)

# Exercise 1: Basic DataFrame operations
print(df.head())
print(df.describe())

# Exercise 2: Filtering and sorting
it_employees = df[df['Department'] == 'IT'].sort_values('Salary', ascending=False)
print(it_employees)

# Exercise 3: Grouping and aggregation
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)

# Exercise 4: Working with numpy
ages = df['Age'].values
average_age = np.mean(ages)
max_age = np.max(ages)
min_age = np.min(ages)

print(f"Average age: {average_age:.2f}")
print(f"Max age: {max_age}")
print(f"Min age: {min_age}")

# Exercise 5: Adding a new column
df['Bonus'] = df['Salary'] * 0.1
print(df)
