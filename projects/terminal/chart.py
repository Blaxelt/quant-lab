from __future__ import annotations

import argparse
from pathlib import Path

from data import plot


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Visualize saved data files")
    parser.add_argument("files", nargs="+", help="parquet/csv files to chart")
    parser.add_argument("--out", default="data/output/charts/", help="output directory for PNG files")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for f in args.files:
        path = Path(f)
        save = out / f"{path.stem}.png"
        plot.candlestick(path, savefig=save)
        print(f"{path} -> {save}")


if __name__ == "__main__":
    main()
