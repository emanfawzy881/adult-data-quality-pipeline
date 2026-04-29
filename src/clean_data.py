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


def clean_adult_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    # remove duplicate rows
    cleaned_df = cleaned_df.drop_duplicates()

    # strip spaces from text columns
    text_columns = cleaned_df.select_dtypes(include="object").columns
    for col in text_columns:
        cleaned_df[col] = cleaned_df[col].str.strip()

    return cleaned_df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    df = load_adult_data("data/raw/adult.csv")
    cleaned_df = clean_adult_data(df)

    print("Original shape:", df.shape)
    print("Cleaned shape:", cleaned_df.shape)
    print()
    print("Missing values:")
    print(cleaned_df.isnull().sum())

    save_cleaned_data(cleaned_df, "data/processed/adult_cleaned.csv")
    print()
    print("Cleaned file saved to data/processed/adult_cleaned.csv")