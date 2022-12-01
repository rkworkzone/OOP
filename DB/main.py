# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import datetime as dt
from tabulate import tabulate
from sqlalchemy import create_engine
import csv
from io import StringIO
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    df = pd.read_csv("D:\Support\Anil\pace-data.txt", sep=',')
    df['MovementDateTime'] = df['MovementDateTime'].astype('datetime64[ns]').apply(dt.datetime.isoformat)
    df['BeamRatio'] = df['Beam'] / df['Length']
    df['avg_speed'] = df.groupby(['CallSign', 'ShipName'])['Speed'].transform('mean')
    df['Speed_new'] = np.where((df['MoveStatus'] == 'Under way using engine') & (df['Speed'] == 0.0), df['avg_speed'],
                           df['Speed'])

    clms = ['MovementDateTime', 'Destination', 'DestinationTidied', 'Speed',
     'AdditionalInfo', 'CallSign', 'Heading', 'MMSI', 'MovementID',
     'ShipName', 'ShipType', 'Beam', 'Draught', 'Length', 'ETA',
     'MoveStatus', 'ladenStatus', 'LRIMOShipNo', 'Latitude', 'Longitude',
     'BeamRatio']

    df.drop('Speed', 1)
    df.drop('avg_speed', 1)

    df_final = df[['MovementDateTime', 'Destination', 'DestinationTidied', 'Speed_new',
     'AdditionalInfo', 'CallSign', 'Heading', 'MMSI', 'MovementID',
     'ShipName', 'ShipType', 'Beam', 'Draught', 'Length', 'ETA',
     'MoveStatus', 'ladenStatus', 'LRIMOShipNo', 'Latitude', 'Longitude',
     'BeamRatio']]

    df_final.columns = clms
    #print(tabulate(df.head(100), headers='keys', tablefmt='psql'))

    def psql_insert_copy(table, conn, keys, data_iter):

        dbapi_conn = conn.connection
        with dbapi_conn.cursor() as cur:
            s_buf = StringIO()
            writer = csv.writer(s_buf)
            writer.writerows(data_iter)
            s_buf.seek(0)

            columns = ', '.join('"{}"'.format(k) for k in keys)
            if table.schema:
                table_name = '{}.{}'.format(table.schema, table.name)
            else:
                table_name = table.name

            sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
                table_name, columns)
            cur.copy_expert(sql=sql, file=s_buf)





    engine = create_engine('postgresql://captain:Captain$0@pacedb.cfq1ibhygxfn.us-east-2.rds.amazonaws.com:5432/pacedb')
    df_final.to_sql(
        name="pace_table",
        con=engine,
        if_exists="append",
        index=False,
        method=psql_insert_copy
    )

    #df_final.to_sql('table_name', engine)

    # k = df1.loc[(df1['Speed'] == 0.0) & (df1['MoveStatus'] == 'Under way using engine') & (df1['avg_speed'] > 0 )].head(100)
    # print(tabulate(k, headers='keys', tablefmt='psql'))

    # s = df[['Speed','Speed_new', 'avg_speed', 'MoveStatus']]
    # k = s.loc[(s['Speed'] == 0.0) & (s['MoveStatus'] =='Under way using engine')].head(100)
    # print(tabulate(k, headers = 'keys', tablefmt = 'psql'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
