import pyodbc
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, sql
import urllib
from sqlalchemy import event
import numpy as np

def run1():
    df = pd.read_csv("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv", sep=',')
    print(df.head())

    params = urllib.parse.quote_plus(r'Driver={SQL Server};Server=wkdummydb.database.windows.net,1433;Database=dummydb;Uid=myname;Pwd=Ingrity@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    # cnxn = pyodbc.connect(params)
    # cursor = cnxn.cursor()
    # cursor.fast_executemany = True
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str)

    connection = engine.connect()
    employees = connection.execute(sql.text("select * from dbo.dummy"))
    for employee in employees:
        print(employee)

    # employees = connection.execute(sql.text("select * from dbo.pace_table"))
    # for employee in employees:
    #     logging.info(employee)

    @event.listens_for(engine, "before_cursor_execute")
    def receive_before_cursor_execute(
       conn, cursor, statement, params, context, executemany
        ):
            if executemany:
                cursor.fast_executemany = True

    def write_df_to_sql(df, **kwargs):

        chunks = np.array_split(df, df.shape[0] / 10 ** 2)

        for chunk in chunks:
            chunk.to_sql(**kwargs)

        return True

    #engine = create_engine('postgresql://captain:Captain$0@pacedb.cfq1ibhygxfn.us-east-2.rds.amazonaws.com:5432/pacedb')
    write_df_to_sql(df,
            name="pace_table_1",
            con=engine,
            schema='dbo',
            if_exists="append",
            index=False,
    )
def run():
    df = pd.read_csv("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv", sep=',')
    print(df.head())
    MY_TABLE = 'dbo.pace_table_1'
    server = 'wkdummydb.database.windows.net'
    database = 'dummydb'
    username = 'myname'
    password = 'Ingrity@123'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    insert_to_tmp_tbl_stmt = f"INSERT INTO {MY_TABLE} values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor.fast_executemany = True
    cursor.executemany(insert_to_tmp_tbl_stmt, df.values.tolist())
    # for index, row in df.iterrows():
    #     print(row)
    #     cursor.execute("INSERT INTO dbo.pace_table (BusinessEntityID, TotalPurchaseYTD, DateFirstPurchase, BirthDate, MaritalStatus, YearlyIncome, Gender, TotalChildren, NumberChildrenAtHome, Education, Occupation, HomeOwnerFlag, NumberCarsOwned) values(?,?,?,?,?,?,?,?,?,?,?,?,?)", row.BusinessEntityID, row.TotalPurchaseYTD, row.DateFirstPurchase, row.BirthDate, row.MaritalStatus, row.YearlyIncome, row.Gender, row.TotalChildren, row.NumberChildrenAtHome, row.Education, row.Occupation, row.HomeOwnerFlag, row.NumberCarsOwned)
    print(f'{len(df)} rows inserted to the {MY_TABLE} table')
    cnxn.commit()
    cursor.close()


def run2():
    df = pd.read_csv("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv", sep=',')
    from bcpandas import SqlCreds, to_sql
    creds = SqlCreds('wkdummydb.database.windows.net', 'dummydb', 'myname', 'Ingrity@123')
    to_sql(df, 'pace_table', creds, index=False, if_exists='replace')

run2()