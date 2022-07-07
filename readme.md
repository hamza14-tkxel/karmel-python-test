# Setup guide for Pandas's POC

### What does this POC do?
- ***pandas_dataframe_exercise()*** takes two dictionaries as parameter, convert these dictionaries to dataframes and then append the second dataframe into the first dataframe as a new column.

### Testing Environment
- Ubuntu 20.04

### Pre-requisites
- Pandas
- Pytest

### How to run the POC?
- Make sure the Pre-requisites are fulfilled.
- Call the ***pandas_dataframe_exercise()*** function and pass two valid dictionaries as parameter.
- All the columns' length should be same for a dictionary.
- Example of valid dictionary: dic1 = {'Name': ['Haseeb', 'George', 'Micheal'], 'Age': [40, 60, 25]}
- Example of invalid dictionary: dic1 = {'Name': ['Haseeb', 'George', 'Micheal'], 'Age': [40, 60]}

### How to run the unit tests?
- In your working directory, run the pytest command: **pytest -v**
