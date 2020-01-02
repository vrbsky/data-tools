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

# from https://www.gitmemory.com/issue/mkleehammer/pyodbc/612/523442670
# This works:
import cx_Oracle
connection = cx_Oracle.connect("system", "my_pwd", "175.201.160.29/ORCLPDB1")
# …connection cursors work as expected, all good

# But none of this works:
import pyodbc  # version 4.0.26
conn_params = [
    {'server': '175.201.160.29:1521', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'server': '175.201.160.29:1521/ORCLCDB', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'server': '175.201.160.29:1521/ORCLPDB1', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'dbq': '175.201.160.29:1521', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'dbq': '175.201.160.29:1521/ORCLCDB', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'dbq': '175.201.160.29:1521/ORCLPDB1', 'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
    {'server': '175.201.160.29', 'sid': 'ORCLPDB1',  'uid': 'system', 'pwd': 'my_pwd', 'driver': "Oracle 19 ODBC driver"},
]
for attempt in conn_params:
    try:
        conn = pyodbc.connect(**attempt)
        print('SUCCESS!')
    except Exception:
        print('failed with', attempt)

# The error is always Error: ('IM004', "[IM004] [unixODBC][Driver Manager]Driver's SQLAllocHandle on SQL_HANDLE_HENV failed (0) (SQLDriverConnect)").

# Yeah, it seems to work now just with the dbq parameter, at least for Oracle 12c.
