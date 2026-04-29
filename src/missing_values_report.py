from pathlib import Path
import pandas as pd


def load_cleaned_data(path: str) -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


def create_missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    report = df.isnull().sum().reset_index()
    report.columns = ["column", "missing_values"]
    report = report.sort_values(by="missing_values", ascending=False)
    return report


def save_report(df: pd.DataFrame, output_path: str) -> None:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    cleaned_df = load_cleaned_data("data/processed/adult_cleaned.csv")
    report_df = create_missing_values_report(cleaned_df)

    print(report_df)
    save_report(report_df, "reports/missing_values_report.csv")

    print()
    print("Missing values report saved to reports/missing_values_report.csv")