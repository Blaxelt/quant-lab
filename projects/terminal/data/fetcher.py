from __future__ import annotations

from typing import Iterable

import pandas as pd
import yfinance as yf


def download(
    tickers: str | Iterable[str],
    start: str,
    end: str,
    interval: str = "1d",
    auto_adjust: bool = True,
    group_by: str = "ticker",
) -> pd.DataFrame:
    if isinstance(tickers, str):
        tickers = [tickers]

    data = yf.download(
        tickers=list(tickers),
        start=start,
        end=end,
        interval=interval,
        auto_adjust=auto_adjust,
        group_by=group_by,
        progress=False,
        threads=True,
    )

    data.index.name = "date"
    return data
