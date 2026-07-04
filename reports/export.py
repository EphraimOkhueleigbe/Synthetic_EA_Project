import pandas as pd
from typing import List
from backtester.models import Trade

def export_trades(history: List[Trade], filename: str = "trade_history.csv"):
    rows = []
    for trade in history:
        rows.append({
            "Direction": trade.direction,
            "EntryTime": trade.entry_time,
            "EntryPrice": trade.entry_price,
            "StopLoss": trade.stop_loss,
            "TakeProfit": trade.take_profit,
            "LotSize": trade.lot_size,
            "ExitTime": trade.exit_time,
            "ExitPrice": trade.exit_price,
            "Result": trade.result,
            "PnL": trade.pnl
        })
        
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"\nTrade history saved to {filename}")
