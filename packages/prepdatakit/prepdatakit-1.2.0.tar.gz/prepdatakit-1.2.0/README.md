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
import prepdatakit

# Read a CSV file
data = prepdatakit.read_file('data.csv')

# Get summary statistics
summary = prepdatakit.get_summary(data)
print(summary)

# Handle missing values
clean_data = prepdatakit.handle_missing_values(data, strategy='remove')

# Encode categorical data
encoded_data = prepdatakit.one_hot_encode(clean_data, columns=['category'])

```
