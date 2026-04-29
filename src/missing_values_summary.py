from pathlib import Path
import pandas as pd


def load_report(path: str) -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


def filter_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    summary_df = df[df["missing_values"] > 0].copy()
    summary_df = summary_df.sort_values(by="missing_values", ascending=False)
    return summary_df


def save_summary(df: pd.DataFrame, output_path: str) -> None:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    report_df = load_report("reports/missing_values_report.csv")
    summary_df = filter_missing_values(report_df)

    print(summary_df)
    save_summary(summary_df, "reports/missing_values_summary.csv")

    print()
    print("Missing values summary saved to reports/missing_values_summary.csv")