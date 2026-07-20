import pandas as pd


def load_sentences(file_path):
    df = pd.read_excel(file_path)

    return df