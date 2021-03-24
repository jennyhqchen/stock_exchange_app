import baostock as bs
import pandas as pd
import pymysql
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()
DB_STRING = 'mysql+mysqldb://root:qwer1234@127.0.0.1/stockexchange?charset=utf8'
engine = create_engine(DB_STRING)

lg = bs.login()
print('login respond error_code:' + lg.error_code)
print('login respond  error_msg:' + lg.error_msg)

rs = bs.query_stock_basic()

data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
bs.logout()
result = pd.DataFrame(data_list[300:350], columns=rs.fields)
filter_result = result.filter(["code", "code_name"])
filter_result.to_sql('stock_exchange_stock', con=engine, chunksize=10000, if_exists='append')
