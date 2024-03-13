# DataPrepKitz

DataPrepKitz is a Python package that provides a convenient set of functions for data preprocessing tasks. It simplifies the process of reading data from various file formats, generating data summaries, handling missing values, and encoding categorical data.

## Features

- **Data Reading**: Read data from CSV, Excel (XLS, XLSX), and JSON files.
- **Data Summary**: Generate key statistical summaries, including information about data types, missing values, and categorical value counts.
- **Handling Missing Values**: Impute missing values with the column mean or replace them with zeros.
- **Categorical Data Encoding**: Encode categorical data using techniques like label encoding, ordinal encoding, and one-hot encoding.

## Installation

You can install DataPrepKitz using pip:
pip install DataPrepKitz
## Usage

Here's a basic example of how to use the DataPrepKitz:

```python
from data_prep_kit import DataPrepKitz

# Create a DataPrepKitz instance with the file path
data_prep = DataPrepKitz('path/to/your/data/file.csv')

# Summarize the data
data_prep.summarize()

# Drop duplicates
data_prep.drop_duplicates()

# Drop empty columns
data_prep.drop_empty_columns()

# Impute missing values with column mean
data_prep.impute_avg()

# Encode categorical columns using one-hot encoding
data_prep.encode_categorical(['category_col'], 'one-hot')
```
## Usage
DataPrepKitz relies on the following Python packages:

pandas
numpy
scikit-learn
These dependencies will be installed automatically when you install DataPrepKitz.

License
DataPrepKitz is released under the MIT License.

This README.md file provides an overview of the DataPrepKitz package, including its features, installation instructions, a basic usage example, information about dependencies. You can customize it further by adding more details or examples as needed.