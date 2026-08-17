from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data import fetcher, storage


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch historical data for stocks and ETFs")
    parser.add_argument("tickers", nargs="+", help="ticker symbols, e.g. SPY AAPL")
    parser.add_argument("--start", required=True, help="start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="end date (YYYY-MM-DD)")
    parser.add_argument("--interval", default="1d", help="interval: 1d, 1wk, 1mo, 1h, ...")
    parser.add_argument("--out", default="data/output/", help="output directory")
    parser.add_argument("--format", default="parquet", choices=["parquet", "csv"])
    parser.add_argument("--raw", action="store_true", help="disable auto-adjust for splits/dividends")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = fetcher.download(  
        args.tickers,
        start=args.start,
        end=args.end,
        interval=args.interval,
        auto_adjust=not args.raw,
    )
    out = Path(args.out)
    for t in args.tickers:
        series = df[t] if isinstance(df.columns, pd.MultiIndex) else df
        print(series.head())
        path = storage.save(series, out / f"{t}.{args.format}", fmt=args.format)
        print(f"{t}: {len(series)} rows -> {path}")


if __name__ == "__main__":
    main()
