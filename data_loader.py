import pandas as pd


def load_excel(file_path):
    df = pd.read_excel(file_path)
    df = df.dropna(how="all")
    df.columns = df.columns.str.strip()
    return df