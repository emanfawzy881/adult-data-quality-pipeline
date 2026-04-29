from pathlib import Path
import pandas as pd


def load_adult_data(path: str) -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    column_names = [
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education_num",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital_gain",
        "capital_loss",
        "hours_per_week",
        "native_country",
        "income",
    ]

    df = pd.read_csv(
        file_path,
        header=None,
        names=column_names,
        na_values="?",
        skipinitialspace=True,
    )

    return df


if __name__ == "__main__":
    df = load_adult_data("data/raw/adult.csv")
    print(df.head())
    print()
    print(df.info())