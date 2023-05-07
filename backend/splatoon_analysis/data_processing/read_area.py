import pandas as pd
import datetime
import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv




class DataImport:

    def __init__(self, day, host, port, database, user, password):
        self.yesterday = day
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect_postgres(self):
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def insert_to_game(self):
        df = pd.read_csv(f"../../../csv/{self.yesterday}.csv")
        # エリアのみに絞る
        df_area = df.query("mode == 'area'")
        df_area['bravo-count'] = df_area['bravo-count'].astype(int)
        df_area['alpha-count'] = df_area['alpha-count'].astype(int)

        print('あいうえお')

        table_name = "game"

        query = f"""INSERT INTO {table_name} VALUES %s"""

        # todo 以下を参考
        # データフレームの値をタプルのリストに変換
        # values = []
        # for row in df[['Name', 'Age', 'City']].values:
        #     # 欠損値をNoneに変換してタプルに追加
        #     row = [None if pd.isnull(value) else value for value in row]
        #     values.append(tuple(row))
        # values = [tuple(x) for x in df_area.to_numpy()]
        values = [tuple(x) for x in df_area.values]

        cur = self.conn.cursor()

        cur.executemany(query, values)
        # execute_values(cur, query, values)
        self.conn.commit()
        cur.close()

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None




def main():
    load_dotenv('../../../.env')
    current_date = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = current_date.strftime('%Y-%m-%d')
    env_host = os.getenv('host')
    di = DataImport(day=yesterday,
                    host='192.168.11.15',
                    port='5432',
                    database='postgres',
                    user='postgres',
                    password='postgres')
    di.connect_postgres()
    di.insert_to_game()


if __name__ == "__main__":
    main()
