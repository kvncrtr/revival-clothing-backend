from pathlib import Path
import csv


INPUT_FILE = "/Users/repayjesus/Dev/personal/study/revival-clothing-backend/users_export.csv"
OUTPUT_FILE = "/Users/repayjesus/Dev/personal/study/revival-clothing-backend/users_export.md"


def escape_markdown_cell(value: str) -> str:
    """
    Cleans values so they do not break the Markdown table.
    """
    return (
        value
        .replace("|", "\\|")
        .replace("\n", " ")
        .replace("\r", " ")
        .strip()
    )


def csv_to_markdown_table(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    with input_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="|")
        rows = list(reader)

    if not rows:
        raise ValueError("The input file is empty.")

    headers = rows[0]
    data_rows = rows[1:]
    column_count = len(headers)

    markdown_lines = []

    # Header row
    markdown_lines.append(
        "| " + " | ".join(escape_markdown_cell(cell) for cell in headers) + " |"
    )

    # Separator row
    markdown_lines.append(
        "| " + " | ".join(["---"] * column_count) + " |"
    )

    # Data rows
    for row_number, row in enumerate(data_rows, start=2):
        if len(row) != column_count:
            raise ValueError(
                f"Row {row_number} has {len(row)} columns, "
                f"but expected {column_count}: {row}"
            )

        markdown_lines.append(
            "| " + " | ".join(escape_markdown_cell(cell) for cell in row) + " |"
        )

    output_path.write_text("\n".join(markdown_lines), encoding="utf-8")

    print(f"Created Markdown file: {output_path}")


if __name__ == "__main__":
    csv_to_markdown_table(INPUT_FILE, OUTPUT_FILE)