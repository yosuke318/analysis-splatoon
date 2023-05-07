import pandas as pd
import datetime
from psycopg2.extras import execute_values


class DataImport:

    def __init__(self, yesterday):
        self.yesterday = yesterday

    def insert_to_game(self):
        df = pd.read_csv(f"../../../csv/{self.yesterday}.csv")
        # todo エリアのみに絞る
        df_area = df.query("mode == 'area'")
        # todo データインサート
        print('あいうえお')




def main():
    current_date = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = current_date.strftime('%Y-%m-%d')
    di = DataImport(yesterday)
    di.insert_to_game()


if __name__ == "__main__":
    main()
