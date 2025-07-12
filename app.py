# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import talib
from luno_python.client import Client

from flag_recog import pivot_id, point_pos, detect_flag
from pattern_recog import three_inside, three_outside, dark_cloud_cover, doji, doji_star, dragonfly_doji, \
    engulfing, evening_doji_star, evening_star, gravestone_doji, hammer, inverted_hammer, morning_doji_star, \
    morning_star, piercing, shooting_star

c = Client(api_key_id='dv7y5qkfp7jhj', api_key_secret='FaM3xxURGgt5zv_Z8iKV6tAE2iP0RYxr-cLbhVFRlDY')

xbt_balance = 0
eth_balance = 0
zar_balance = 0
usdc_balance = 0
try:
    res = c.get_balances()
    xbt_balance = res["balance"][1]["balance"]
    eth_balance = res["balance"][3]["balance"]
    usdc_balance = res["balance"][5]["balance"]
    zar_balance = res["balance"][7]["balance"]
except Exception as e:
    print(e)

since = int(time.time() * 1000) - 365 * 24 * 60 * 59 * 1000
candles = []
showing_candles = []
try:
    res = c.get_candles(duration=86400, pair='ETHZAR', since=since)
    candles = pd.DataFrame(res['candles'])
    candles = candles.astype({'open': 'float'})
    candles = candles.astype({'close': 'float'})
    candles = candles.astype({'high': 'float'})
    candles = candles.astype({'low': 'float'})
    candles = candles.astype({'volume': 'float'})

    candles['28_Day_SMA'] = talib.SMA(candles['close'], timeperiod=28)

    candles['pivots'] = candles.apply(
        lambda row: pivot_id(df=candles, current_candle_index=row.name, neigh_1=3, neigh_2=3),
        axis=1)
    candles['point_pos'] = candles.apply(lambda point_row: point_pos(point_row), axis=1)
    candles['flag'] = candles.index.map(
        lambda flag_x: detect_flag(df=candles, candle=flag_x, back_candles=35, window=3))
    print(candles[candles['flag']==1])

    ti = three_inside(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    to = three_outside(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    dcc = dark_cloud_cover(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    do = doji(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    ds = doji_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    dfd = dragonfly_doji(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    eng = engulfing(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    eds = evening_doji_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    es = evening_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    gsd = gravestone_doji(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    ham = hammer(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    ih = inverted_hammer(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    mds = morning_doji_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    ms = morning_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    pc = piercing(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])
    ss = shooting_star(open_=candles['open'], high=candles['high'], low=candles['low'], close=candles['close'])

    candles['Three Inside'] = ti[ti != 0]
    candles['Three Outside'] = to[to != 0]
    candles['Dark Cloud Cover'] = dcc[dcc != 0]
    candles['Doji'] = do[do != 0]
    candles['Doji Star'] = ds[ds != 0]
    candles['Dragonfly Doji'] = dfd[dfd != 0]
    candles['Engulfing'] = eng[eng != 0]
    candles['Evening Doji Star'] = eds[eds != 0]
    candles['Evening Star'] = es[es != 0]
    candles['Gravestone Doji'] = gsd[gsd != 0]
    candles['Hammer'] = ham[ham != 0]
    candles['Inverted Hammer'] = ih[ih != 0]
    candles['Morning Doji Star'] = mds[mds != 0]
    candles['Morning Star'] = ms[ms != 0]
    candles['Piercing'] = pc[pc != 0]
    candles['Shooting Star'] = ss[ss != 0]

    showing_candles = candles.tail(30)
except Exception as e:
    print(e)

fig_primary = go.Figure(data=[
    go.Candlestick(
        x=[time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp / 1000)) for timestamp in
           showing_candles['timestamp']],
        open=showing_candles['open'],
        high=showing_candles['high'],
        low=showing_candles['low'],
        close=showing_candles['close'],
        increasing=dict(fillcolor='#2FC622', line=dict(color='#2FC622')),
        decreasing=dict(fillcolor='#FF5E5E', line=dict(color='#FF5E5E')),
        name='ETHZAR'
    ),
    go.Scatter(x=showing_candles['timestamp'], y=showing_candles['28_Day_SMA'], mode='lines', name='28 Day SMA'),
    go.Scatter(x=showing_candles['timestamp'], y=showing_candles['point_pos'], mode='markers',
               marker=dict(size=5, color='MediumPurple'), name='Pivot')
])

for x in showing_candles['Three Outside'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Doji'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Doji Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Dragonfly Doji'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Engulfing'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Evening Doji Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Evening Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Gravestone Doji'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Hammer'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Inverted Hammer'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Morning Doji Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Morning Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Piercing'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)
for x in showing_candles['Shooting Star'].dropna().index:
    fig_primary.add_vrect(x0=showing_candles['timestamp'][x], x1=showing_candles['timestamp'][x], line_width=20,
                          opacity=0.2)

fig_primary.update_layout(
    xaxis=dict(rangeslider=dict(visible=False)),
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0)
)
fig_primary.update_xaxes(fixedrange=True, showticklabels=False)
fig_primary.update_yaxes(fixedrange=True)


def run_sidebar():
    with st.sidebar:
        title_cols = st.columns([1, 12])
        with title_cols[0]:
            st.markdown(':elephant:')
        with title_cols[1]:
            st.markdown('<p style="font-weight:bold;letter-spacing:2px;">EUGE.INVESTMENTS</p>', unsafe_allow_html=True)

        st.markdown('#')
        crypt_cols = st.columns(4)
        with crypt_cols[0]: st.button('BTC', use_container_width=True)
        with crypt_cols[1]: st.button('ETH', use_container_width=True)
        with crypt_cols[2]: st.button('XRP', use_container_width=True)
        with crypt_cols[3]: st.button('LTC', use_container_width=True)

        coin_cols = st.columns([1.3, 2, 3])
        with coin_cols[0]:
            st.markdown(
                '''<p style="margin-bottom:22px;">
                <span style="border-radius:32px;background:#FF5E5E;font-size:32px;font-weight:bold;padding:2px 12px;">฿</span>
                </p>''',
                unsafe_allow_html=True
            )
        with coin_cols[1]:
            st.markdown('<p style="font-weight:bold;font-size:20px;">BTC</p>', unsafe_allow_html=True)
            st.markdown('<p style="margin-top:-20px;">USD</p>', unsafe_allow_html=True)
        with coin_cols[2]:
            st.markdown('<p style="font-weight:bold;font-size:20px;text-align:right;">1.00 BTC</p>',
                        unsafe_allow_html=True)
            st.markdown('<p style="text-align:right;margin-top:-20px;">38245.23 USD</p>', unsafe_allow_html=True)
        st.markdown('<hr style="margin-top:8px">', unsafe_allow_html=True)

        st.markdown('''<div style="font-size:11px;display:flex;justify-content:space-between;">
        <p style="font-size:11px;">JAN</p>
        <p style="font-size:11px;">FEB</p>
        <p style="font-size:11px;">MAR</p>
        <p style="font-size:11px;">APR</p>
        <p style="font-size:11px;">MAY</p>
        </div>''', unsafe_allow_html=True)

        fig_second = go.Figure(data=[go.Candlestick(
            x=[time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp / 1000)) for timestamp in
               candles['timestamp']],
            open=candles['open'],
            high=candles['high'],
            low=candles['low'],
            close=candles['close'],
            increasing=dict(fillcolor='#2FC622', line=dict(color='#2FC622')),
            decreasing=dict(fillcolor='#FF5E5E', line=dict(color='#FF5E5E'))
        )])
        fig_second.update_layout(
            showlegend=False,
            yaxis_showgrid=False,
            yaxis_showticklabels=False,
            xaxis_showticklabels=False,
            margin=dict(t=0, b=0, l=0, r=0),
            xaxis=dict(rangeslider=dict(visible=False)),
            height=212
        )

        st.plotly_chart(fig_second, theme='streamlit', use_container_width=True, config={'displayModeBar': False})

        minmax_cols = st.columns(2)
        with minmax_cols[0]:
            st.markdown('$ 14,3K')
        with minmax_cols[1]:
            st.markdown('<p style="text-align:right;">$ 38,5K</p>', unsafe_allow_html=True)

        st.markdown('#')
        st.markdown('<p style="text-align:center;">Find out more about the settings going on in the background.</p>',
                    unsafe_allow_html=True)
        st.button("Settings", type="secondary", use_container_width=True)
        st.markdown('<p style="text-align:center;font-size:12px;">Investment tools are currently active.</p>',
                    unsafe_allow_html=True)


def under_chart():
    balance_cols = st.columns([2, 2, 1])

    with balance_cols[0]:
        st.metric(label='BTC BALANCE', value=f'฿ {xbt_balance}')
        st.metric(label='ETH BALANCE', value=f'Ξ {eth_balance}')

    with balance_cols[1]:
        st.metric(label='ZAR BALANCE', value=f'R {zar_balance}')
        st.metric(label='USDC BALANCE', value=f'$ {usdc_balance}')

    with balance_cols[2]:
        st.metric(label=':green[PROFIT]', value='64%')
        st.metric(label=':red[LOSS]', value='36%')


def run():
    run_sidebar()

    st.markdown('<p style="margin-bottom:-32px">ΞTH/ZAR</p>', unsafe_allow_html=True)

    try:
        st.title(f'R {c.get_ticker(pair="ETHZAR")["last_trade"][:-6]}')
    except Exception as ticker_e:
        print(ticker_e)

    st.divider()
    timeframe_cols = st.columns([1, 1, 5.5])
    with timeframe_cols[0]:
        if st.button('HOURLY', use_container_width=True):
            fig_primary.data[0].update(
                dict(open=candles['open'], high=candles['high'], low=candles['low'], close=candles['close']))
    with timeframe_cols[1]:
        if st.button('DAILY', use_container_width=True):
            fig_primary.data[0].update(dict(low=candles['close']))
    with timeframe_cols[2]:
        st.empty()

    st.plotly_chart(fig_primary, theme='streamlit', use_container_width=True, config={'displayModeBar': False})
    st.divider()

    under_chart()


if __name__ == "__main__":
    run()
