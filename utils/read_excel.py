import pandas as pd


def load_excel(path: str, ext: str) -> pd.DataFrame:
    """
    Returns a dataframe.

    :param: path (str): The path of the excel file.

    :return: dataframe: A dataframe of the excel file.

    Example usage:
    >>> path = 'data/excel.xlsx'
    >>> ext = 'xlsx'
    >>> df = load_excel(path, ext)
    """

    if ext == 'xlsx':
        return pd.read_excel(path)
    elif ext == 'csv':
        return pd.read_csv(path)
