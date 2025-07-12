import csv
import os
from typing import List


def read_from_csv(file_path: str) -> List[List[str]]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Skip header, assume always "Title", "Description"
    return rows[1:]  # return only data rows


def write_to_csv(file_path: str, data: List[List[str]]):
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Description"])  # fixed headers
        writer.writerows(data)
