# relies on import pandas as pd

def print_all_columns(df):
    return HTML('<br />'.join(str(y) for y in df.columns))

def describe_data(df):
    print("Data Types:")
    print(df.dtypes)
    print("Rows and Columns:")
    print(df.shape)
    print("Column Names:")
    print(df.columns)
    print("Null Values:")
    print(df.apply(lambda x: sum(x.isnull()) / len(df)))

def dict_to_df(d, col0_name='col0', col1_name='col1'):
    return pd.DataFrame({col0_name: list(d.keys()), col1_name: list(d.values())})