# relies on import pandas as pd

# Recommended column separator
# - Hadoop: \u0001 (maybe also \001) - ^A character
# - CSV: \u001f - Unit Separator

def print_all_columns(df):
    return HTML('<br />'.join(str(y) for y in df.columns))

def describe_data(df):
    print(f"""\
- Data Types:
{df.dtypes}

- Rows and Columns:
{df.shape}

- Column Names:
{df.columns}

- Null Values [%]:
{df.apply(lambda x: sum(x.isnull()) / len(df))}\
""")

def dict_to_df(d, col0_name='col0', col1_name='col1'):
    return pd.DataFrame({col0_name: list(d.keys()), col1_name: list(d.values())})