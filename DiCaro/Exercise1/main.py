import os
import pandas as pd


file_path = os.path.abspath('../DiCaro/Exercise1/definizioni.xlsx')


def main():
    df = pd.read_excel(file_path)
    print(df)