from database.db import get_connection


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    # =====================================
    # PROJECTS
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        description TEXT,

        created_at TEXT,

        last_modified TEXT

    );
    """)

    # =====================================
    # STRATEGIES
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategies (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        project_id INTEGER,

        name TEXT,

        ema_fast INTEGER,

        ema_slow INTEGER,

        risk_formula TEXT,

        take_profit REAL,

        created_at TEXT

    );
    """)

    # =====================================
    # BACKTESTS
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS backtests (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        strategy_id INTEGER,

        test_date TEXT,

        symbol TEXT,

        timeframe TEXT,

        starting_balance REAL,

        ending_balance REAL,

        net_profit REAL,

        win_rate REAL,

        profit_factor REAL,

        max_drawdown REAL

    );
    """)

    # =====================================
    # TRADES
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        backtest_id INTEGER,

        direction TEXT,

        entry_price REAL,

        exit_price REAL,

        stop_loss REAL,

        take_profit REAL,

        profit REAL,

        result TEXT,

        entry_time TEXT,

        exit_time TEXT

    );
    """)

    # =====================================
    # OPTIMIZATIONS
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS optimizations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        strategy_id INTEGER,

        optimization_date TEXT,

        best_parameters TEXT,

        score REAL,

        profit REAL,

        drawdown REAL

    );
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()