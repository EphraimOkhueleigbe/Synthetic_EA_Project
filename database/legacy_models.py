from dataclasses import dataclass
from datetime import datetime


# ==========================================
# Project
# ==========================================

@dataclass
class Project:

    id: int

    name: str

    created_at: datetime


# ==========================================
# Backtest
# ==========================================

@dataclass
class Backtest:

    id: int

    project_id: int

    starting_balance: float

    ending_balance: float

    net_profit: float

    win_rate: float

    profit_factor: float

    max_drawdown: float

    total_trades: int

    created_at: datetime


# ==========================================
# Trade
# ==========================================

@dataclass
class Trade:

    id: int

    backtest_id: int

    direction: str

    entry_price: float

    exit_price: float

    stop_loss: float

    take_profit: float

    result: str

    profit: float

    open_time: datetime

    close_time: datetime