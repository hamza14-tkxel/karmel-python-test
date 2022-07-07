from karmel_poc import pandas_dataframe_exercise

def test_irregular_column_length():
   first_dictionary = {
      'Employee Name': ['Haseeb', 'Ali', 'George', 'Omer', 'Micheal'],
      'Age': [35, 22, 50, 60, 44, 30],
   }
   second_dictionary = {
      'Overall Experience': [20, 2, 10, 5, 8, 15],
      'Job Type': ['Permanent', 'Permanent', 'Associate', 'Contract', 'Permanent', 'Permanent'],
   }
   assert pandas_dataframe_exercise(first_dictionary, second_dictionary) == False


def test_if_dictionaries_are_empty():
   first_dictionary = {}
   second_dictionary = {}
   assert pandas_dataframe_exercise(first_dictionary, second_dictionary) == False