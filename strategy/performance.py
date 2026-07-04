def performance_report(history, starting_balance=1000):

    total_trades = len(history)

    wins = 0
    losses = 0

    gross_profit = 0
    gross_loss = 0

    balance = starting_balance

    max_balance = balance
    max_drawdown = 0

    for trade in history:

        outcome = trade["result"]["result"]

        # Skip trades still open
        if outcome == "OPEN":
            continue

        # Risk per trade (1% of current balance)
        risk = balance * 0.01

        if outcome == "WIN":

            wins += 1

            profit = risk

            gross_profit += profit

            balance += profit

        elif outcome == "LOSS":

            losses += 1

            loss = risk

            gross_loss += loss

            balance -= loss

        if balance > max_balance:
            max_balance = balance

        drawdown = max_balance - balance

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    closed_trades = wins + losses

    if closed_trades > 0:
        win_rate = wins / closed_trades * 100
    else:
        win_rate = 0

    net_profit = balance - starting_balance

    if gross_loss == 0:
        profit_factor = float("inf")
    else:
        profit_factor = gross_profit / gross_loss

    print("\n" + "=" * 50)
    print("BACKTEST PERFORMANCE REPORT")
    print("=" * 50)

    print(f"Starting Balance : ${starting_balance:.2f}")
    print(f"Ending Balance   : ${balance:.2f}")
    print(f"Net Profit       : ${net_profit:.2f}")

    print()

    print(f"Total Trades     : {closed_trades}")
    print(f"Wins             : {wins}")
    print(f"Losses           : {losses}")
    print(f"Win Rate         : {win_rate:.2f}%")

    print()

    print(f"Gross Profit     : ${gross_profit:.2f}")
    print(f"Gross Loss       : ${gross_loss:.2f}")
    print(f"Profit Factor    : {profit_factor:.2f}")
    print(f"Max Drawdown     : ${max_drawdown:.2f}")

    print("=" * 50)