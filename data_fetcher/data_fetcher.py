import pandas as pd
import yfinance as yf


class DataFetcher:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self) -> pd.DataFrame:
        """
        Return dataframe of Price, Close, High, Low, Open and Volume for given
        Ticker and date range.
        """
        return pd.DataFrame(
            yf.download(self.ticker, start=self.start_date, end=self.end_date)
        )

    def save_to_csv(self):
        # TODO - Use config to define default data path
        data = self.get_data()
        csv_path = f"data/raw/{self.ticker}_{self.start_date}_{self.end_date}.csv"
        data.to_csv(csv_path)


tsla = DataFetcher("TSLA", "2025-01-01", "2025-03-18")
tsla_data = tsla.get_data()

print(tsla_data.info())
