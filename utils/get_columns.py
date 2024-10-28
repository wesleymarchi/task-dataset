import pandas as pd


def get_columns(df: pd.DataFrame) -> list:
    """
    Returns a list of column names from a DataFrame.

    :param: df (pd.DataFrame): The DataFrame from which columns will be extracted.

    :return: list: A list containing the names of the DataFrame's columns.

    Example usage:
    >>> df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    >>> get_columns(df)
    ['A', 'B']
    """
    return list(df.columns)
