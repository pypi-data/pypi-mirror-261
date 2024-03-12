# PrepDataKit

PrepDataKit is a Python package that provides a toolkit for preprocessing datasets. It offers various functions to assist in reading data from different file formats, summarizing datasets, handling missing values, and encoding categorical data.

## Installation

You can install PrepDataKit using pip:

```python 
pip install prepdatakit
```
                    

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
