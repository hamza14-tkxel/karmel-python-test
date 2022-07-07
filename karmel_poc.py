import pandas as pd


def pandas_dataframe_exercise(first_dictionary=dict, second_dictionary=dict):

    # Check if each dictionary's columns have same length
    columns_have_same_length = False if len(set({key: len(value) for key, value in first_dictionary.items()}.values())) > 1 else True
    if not columns_have_same_length:
        return False

    columns_have_same_length = False if len(set({key: len(value) for key, value in second_dictionary.items()}.values())) > 1 else True
    if not columns_have_same_length:
        return False

    # Check if both dictionaries are empty
    if not first_dictionary and not second_dictionary:
        return False

    # Convert python dictionary to dataframe
    first_dataframe = pd.DataFrame(first_dictionary)
    second_dataframe = pd.DataFrame(second_dictionary)

    # Append second dataframe to first dataframe as a column
    new_dataframe_after_append = first_dataframe.join(second_dataframe)
    print(new_dataframe_after_append)
