import pandas as pd
import datetime


class DataImport:

    def __init__(self, yesterday):
        self.yesterday = yesterday

    def insert_to_game(self):
        df = pd.read_csv(f"../../../csv/{self.yesterday}.csv")
        print(df)


def main():
    current_date = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = current_date.strftime('%Y-%m-%d')
    di = DataImport(yesterday)
    di.insert_to_game()


if __name__ == "__main__":
    main()
