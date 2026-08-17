from __future__ import annotations

from pathlib import Path

import pandas as pd


def save(df: pd.DataFrame, path: str | Path, fmt: str = "parquet") -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "parquet":
        if not path.suffix:
            path = path.with_suffix(".parquet")
        df.to_parquet(path)
    elif fmt == "csv":
        if not path.suffix:
            path = path.with_suffix(".csv")
        df.to_csv(path)
    else:
        raise ValueError(f"unsupported format: {fmt}")
    return path


def load(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    if path.suffix == ".csv":
        df = pd.read_csv(path, index_col=0, parse_dates=True)
        df.index.name = "date"
        return df
    raise ValueError(f"unsupported extension: {path.suffix}")
