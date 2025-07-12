import numpy as np
from scipy.stats import linregress
import pandas as pd


def pivot_id(df, current_candle_index, neigh_1, neigh_2):
    if current_candle_index - neigh_1 < 0 or current_candle_index + neigh_2 >= len(df):
        return 0

    pivot_low = 1
    pivot_high = 1
    for i in range(current_candle_index - neigh_1, current_candle_index + neigh_2 + 1):
        pivot_low = 0 if df['low'][current_candle_index] > df['low'][i] else 1
        pivot_high = 0 if df['high'][current_candle_index] < df['high'][i] else 1

    if pivot_low and pivot_high:
        return 3
    elif pivot_low:
        return 1
    elif pivot_high:
        return 2
    else:
        return 0


def point_pos(df_row):
    if df_row['pivots'] == 1:
        return df_row['low'] - 1e-3
    elif df_row['pivots'] == 2:
        return df_row['high'] + 1e-3
    else:
        return np.nan


def detect_flag(df, candle, back_candles, window):
    local_df = df[(candle - back_candles - window):(candle - window)]
    highs = local_df[local_df['pivots'] == 2]['high'].tail(3).values
    idx_highs = local_df[local_df['pivots'] == 2]['high'].tail(3).index
    lows = local_df[local_df['pivots'] == 1]['low'].tail(3).values
    idx_lows = local_df[local_df['pivots'] == 1]['low'].tail(3).index

    if len(highs) == 3 and len(lows) == 3:
        order_condition = (
                (idx_lows[0] < idx_highs[0] < idx_lows[1] < idx_highs[1] < idx_lows[2] < idx_highs[2])
                or
                (idx_highs[0] < idx_lows[0] < idx_highs[1] < idx_lows[1] < idx_highs[2] < idx_lows[2])
        )

        sl_min, inter_c_min, r_min, _, _ = linregress(idx_lows, lows)
        sl_max, inter_c_max, r_max, _, _ = linregress(idx_highs, highs)

        if (order_condition and (r_max * r_max) >= 0.9 and (
                r_min * r_min) >= 0.9 and sl_min >= 0.0001 and sl_max <= -0.0001):
            return 1
        else:
            return 0
