from __future__ import annotations

import argparse
from pathlib import Path

from data import metrics, storage

METRICS = {
    "daily_returns": metrics.daily_returns,
    "cumulative_return": metrics.cumulative_return,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate metrics from saved data files")
    parser.add_argument("files", nargs="+", help="parquet/csv files to analyze")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for f in args.files:
        df = storage.load(f)
        for name, fn in METRICS.items():
            print(f"{f} -> {name}:")
            print(fn(df))
            print()


if __name__ == "__main__":
    main()
