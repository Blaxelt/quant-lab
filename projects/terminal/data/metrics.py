from __future__ import annotations

import pandas as pd

def daily_returns(df: pd.DataFrame) -> pd.Series:
    return df["Close"].pct_change()


def cumulative_return(df: pd.DataFrame) -> pd.Series:
    return (1 + daily_returns(df)).cumprod() - 1
