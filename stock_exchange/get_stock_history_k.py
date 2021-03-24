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
stock_basic_info = pd.DataFrame(data_list[300:350], columns=rs.fields)

data_list = []
for index, row in stock_basic_info.iterrows():
    print(row.get("code"))
    rs = bs.query_history_k_data_plus(row.get("code"),
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,"
                                      "pctChg,isST",
                                      start_date='2021-03-15', end_date='2021-03-15',
                                      frequency="d", adjustflag="3")
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())

print('query_history_k_data_plus respond error_code:' + rs.error_code)
print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)



result = pd.DataFrame(data_list, columns=rs.fields)
print(result)
join_result = result.join(stock_basic_info.set_index('code'), on='code').filter(["date","code", "code_name","open","high","low","close","preclose","volume","amount","adjustflag","turn","tradestatus","pctChg","isST"])
join_result.to_sql('stock_exchange_k_day', con=engine, chunksize=10000, if_exists='append',index= False)
print(join_result)

bs.logout()
