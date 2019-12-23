def database_query_to_df(conn_str, query):
    import pyodbc
    conn =  pyodbc.connect(conn_str)
    df = pd.read_sql(query,conn)
    conn.cursor().close()
    conn.close()     #<--- Close the connection
    return df

conn_str_cherwell_homologacao = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER=10.0.0.9,1234;DATABASE=myDB;UID=myUser;PWD=somePass'
query = """
select * from xy
"""