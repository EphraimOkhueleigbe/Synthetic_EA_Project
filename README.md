# Synthetic Index Expert Advisor

An automated trading system for Deriv Synthetic Indices built with Python and MetaTrader 5.

## Features

- MT5 integration
- EMA indicator engine
- D1 trend detection
- Retracement detection
- M30 confirmation engine
- Dynamic lot sizing
- Trade simulation

## Strategy

1. Detect D1 trend using EMA(9) and EMA(18).
2. Wait for price to retrace to the D1 EMA 9.
3. Monitor M30 after retracement.
4. Enter after an M30 EMA confirmation crossover.
5. Exit at Take Profit or when an opposite D1 trend begins.

## Tech Stack

- PySide6
- MetaTrader5
- pandas
- numpy
- pyqtgraph