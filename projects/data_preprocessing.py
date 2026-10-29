import pandas as pd
def preprocess_data(df):
    # Remove any duplicate rows
    df = df.drop_duplicates()
    # Convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    return df
if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    df = preprocess_data(df)
    df.to_csv('preprocessed_data.csv')