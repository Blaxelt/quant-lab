from __future__ import annotations

from pathlib import Path

import mplfinance as mpf

from data import storage


def candlestick(path: str | Path, savefig: str | Path, title: str | None = None) -> None:
    df = storage.load(path)
    df.columns.name = None
    title = title or Path(path).stem
    mpf.plot(
        df,
        type="candle",
        volume=True,
        style="yahoo",
        title=title,
        savefig=str(savefig),
    )
