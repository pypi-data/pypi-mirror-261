# PrepDataKit

PrepDataKit is a Python package that provides a toolkit for preprocessing datasets. It offers various functions to assist in reading data from different file formats, summarizing datasets, handling missing values, and encoding categorical data.

## Installation

You can install PrepDataKit using pip:

```python 
pip install prepdatakit
```
                    
## Sample Data
| Category | Price | In Stock | Description |
|---|---|---|---|
| Fruit | 2.50 | True | Ripe and delicious |
| Animal | None | False | Needs more data |
| Color | 1.99 |  | Vivid and bright |
| Tool | 9.99 | True | Heavy duty and reliable (Maybe) |


[<a href="data:text/csv;charset=utf-8,category,price,in_stock,description%0AFruit,2.50,True,Ripe%20and%20delicious%0AAnimal,None,False,Needs%20more%20data%0AColor,1.99,,Vivid%20and%20bright%0ATool,9.99,True,Heavy%20duty%20and%20reliable%20(Maybe)%0A)"> Download CSV</a>](data:text/csv;charset=utf-8,category,price,in_stock,description%0AFruit,2.50,True,Ripe%20and%20delicious%0AAnimal,None,False,Needs%20more%20data%0AColor,1.99,,Vivid%20and%20bright%0ATool,9.99,True,Heavy%20duty%20and%20reliable%20(Maybe)%0A)



## Usage

Here's an example of how to use PrepDataKit:

```python
from prepdatakit import prepdatakit
import time

# Read a CSV file
data = prepdatakit.read_file('data.csv')
print("Start after loading the file, summary")

# Get summary statistics
summary = prepdatakit.get_summary(data)
print(summary)
print("Finish summary")
time.sleep(0.5)

# Handle missing values
print("Start clean_data")
clean_data = prepdatakit.handle_missing_values(data, strategy='remove')
print(clean_data)
print("Finish clean_data")
time.sleep(0.5)

# Encode categorical data
print("Start encoded_data")
encoded_data = prepdatakit.one_hot_encode(clean_data, columns=['category'])
print("End encoded_data")
time.sleep(0.5)
```
