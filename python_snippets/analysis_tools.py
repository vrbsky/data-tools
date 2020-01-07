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

def read_xlsb(filepath):
    """This might not work so well as it was not previously used as a function"""
    df = []
    with open_xlsb(filepath) as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                df.append([item.v for item in row])

    df = pd.DataFrame(df[1:], columns=df[0])
    
    # uncomment only if you made the necessary alterations
    # return df

def load_if_example():
    filepath = dataPath / 'abcd.csv' 
    sep = '\u0001'
    if not Path.exists(filepath):
        df = database_query_to_df(conn_str, query_abcd)
        df.to_csv(filepath, sep=sep, index=False)
    else:
        df = pd.read_csv(filepath, sep=sep)

def database_query_to_df_older_version(conn_str, query):
    import pyodbc
    conn =  pyodbc.connect(conn_str)
    df = pd.read_sql(query,conn)
    conn.cursor().close()
    conn.close()     #<--- Close the connection
    return df

def database_query_to_df(conn_str, query):
    import pyodbc
    conn =  pyodbc.connect(conn_str)
    try:
        df = pd.read_sql(query,conn)
    except Error as err:
        print(err)
    finally:
        conn.cursor().close()
        conn.close()     #<--- Close the connection
    return df

def database_query_to_df_Oracle(conn_str, query):
    import cx_Oracle
    #conn = cx_Oracle.connect("usrname", "password", "servicename")
    dsn_tns = cx_Oracle.makedsn('0.0.0.0', '1234', service_name='servicename') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'usrname', password=r'password', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    
    df = pd.read_sql(query, con=conn)
    
    #c = conn.cursor()
    #c.execute(query) # use triple quotes if you want to spread your query across multiple lines
    #for row in c:
    #    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    conn.cursor().close()
    conn.close()
    return df

conn_str_cherwell_homologacao = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER=1.0.0.0,1433;DATABASE=db_name;UID=username;PWD=pass'
# para Oracle é testado uso do método de cima. Caso isso não der certo, pode ser usado talvez um dos seguintes strings
conn_str_oracle_CAT12C = 'DRIVER={Microsoft ODBC Driver for Oracle};SERVER=1.0.0.0,1521;DATABASE=db_name;UID=username;PWD=pass'
conn_str_oracle_CAT12C = 'DRIVER={Microsoft ODBC for Oracle};SERVER=1.0.0.0,1521;DATABASE=db_name;UID=username;PWD=pass'
conn_str_oracle_CAT12C = 'DRIVER={Oracle in OraClient12Home1_32bit};SERVER=1.0.0.0,1521;DATABASE=db_name;UID=username;PWD=pass'
conn_str_oracle_CAT12C = 'DRIVER={Oracle 19 ODBC driver};SERVER=1.0.0.0,1521;DATABASE=db_name;UID=username;PWD=pass'

