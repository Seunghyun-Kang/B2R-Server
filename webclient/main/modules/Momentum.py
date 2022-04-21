import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta

class DualMomentum:
    def __init__(self, symbol):
        self.conn = pymysql.connect(host='localhost', user='root', password='apple10g', db='INVESTAR', charset='utf8')
        with self.conn.cursor() as curs :
            if symbol == "KRX":
                self.codeTable = "company_info"
                self.priceTable = "daily_price"
            elif symbol == "NASDAQ":
                self.codeTable = "company_info_usa"
                self.priceTable = "daily_price_usa"
            elif symbol == "CODE":
                self.codeTable = "ticker_info"
                self.priceTable = "daily_price_coin"
            
            sql = f"select code from {self.codeTable}"
            curs.execute(sql)
            result = curs.fetchall()
            self.codes = []
            for code in result:
                self.codes.append(code[0])
            print(self.codes)
            if self.codes[0] is None:
                print(f"codes are none")
                return

    def __del__(self):
        self.conn.close()

    def get_rltv_momentum(self, start_date, end_date, stockCount):
         with self.conn.cursor() as curs:
            sql = f"select max(date) from {self.priceTable} where date <= '{start_date}'"
            curs.execute(sql)
            result = curs.fetchone()

            if result[0] is None:
                print(f"startdate is none")
                return
            start_date = result[0].strftime('%Y-%m-%d')
            
            sql = f"select max(date) from {self.priceTable} where date <= '{end_date}'"
            curs.execute(sql)
            result = curs.fetchone()

            if result[0] is None:
                print(f"enddate is none")
                return
            end_date = result[0].strftime('%Y-%m-%d')

            rows = []
            columns = ['code', 'old_price', 'new_price', 'returns']
            
            for code in self.codes:
                sql = f"select close from {self.priceTable} where code='{code}' and date='{start_date}' and volume != 0"
                curs.execute(sql)
                result = curs.fetchone()
                if result is None:
                    continue
                old_price = float(result[0])

                sql = f"select close from {self.priceTable} where code='{code}' and date='{end_date}' and volume != 0"
                curs.execute(sql)
                result = curs.fetchone()
                if result is None:
                    continue
                new_price = float(result[0])

                returns = (new_price / old_price -1) * 100
                rows.append([code, old_price, new_price, returns])

            df = pd.DataFrame(rows, columns=columns)
            df = df[['code', 'old_price', 'new_price', 'returns']]
            df = df.sort_values(by='returns', ascending=False)
            df = df.head(stockCount)
            df.index = pd.Index(range(stockCount))

            print(df)
            print(f"\n Relative momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}% \n")
            return df

# a=DualMomentum('KRX')
# print(a.get_rltv_momentum('2021-04-20', '2022-04-19'))
