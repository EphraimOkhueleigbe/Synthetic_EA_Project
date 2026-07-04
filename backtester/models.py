from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Trade:
    direction: str           # "BUY" or "SELL"
    entry_time: datetime.datetime
    entry_price: float
    stop_loss: float
    take_profit: float
    lot_size: float
    exit_time: Optional[datetime.datetime] = None
    exit_price: Optional[float] = None
    result: str = "OPEN"      # "WIN", "LOSS", "CLOSED_BY_TREND", "OPEN"
    pnl: float = 0.0

    def close(self, exit_time: datetime.datetime, exit_price: float, result: str):
        self.exit_time = exit_time
        self.exit_price = exit_price
        self.result = result
        
        # Calculate PnL (1 Lot = 1 Volume unit. Profit/Loss = (Exit - Entry) * LotSize for BUY)
        if self.direction == "BUY":
            self.pnl = (self.exit_price - self.entry_price) * self.lot_size
        else: # SELL
            self.pnl = (self.entry_price - self.exit_price) * self.lot_size
