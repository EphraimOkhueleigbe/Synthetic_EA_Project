from database.db import get_connection


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # =====================================================
    # Projects
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        description TEXT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        updated_at TEXT DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # =====================================================
    # Strategies
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategies(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        project_id INTEGER NOT NULL,

        name TEXT NOT NULL,

        d1_fast_ema INTEGER DEFAULT 9,

        d1_slow_ema INTEGER DEFAULT 18,

        m30_fast_ema INTEGER DEFAULT 9,

        m30_slow_ema INTEGER DEFAULT 18,

        risk_formula TEXT,

        stop_loss_type TEXT,

        stop_loss_value REAL,

        take_profit_type TEXT,

        take_profit_value REAL,

        trade_direction TEXT DEFAULT 'Trend',

        active INTEGER DEFAULT 1,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(project_id)
            REFERENCES projects(id)
            ON DELETE CASCADE

    )
    """)

    # =====================================================
    # Backtests
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS backtests(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        strategy_id INTEGER NOT NULL,

        start_date TEXT,

        end_date TEXT,

        initial_balance REAL,

        final_balance REAL,

        total_trades INTEGER,

        win_rate REAL,

        drawdown REAL,

        profit_factor REAL,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(strategy_id)
            REFERENCES strategies(id)
            ON DELETE CASCADE

    )
    """)

    # =====================================================
    # Optimizations
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS optimizations(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        strategy_id INTEGER NOT NULL,

        score REAL,

        parameter_set TEXT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(strategy_id)
            REFERENCES strategies(id)
            ON DELETE CASCADE

    )
    """)

    # =====================================================
    # Trades
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        backtest_id INTEGER NOT NULL,

        direction TEXT,

        entry_price REAL,

        exit_price REAL,

        stop_loss REAL,

        take_profit REAL,

        profit REAL,

        open_time TEXT,

        close_time TEXT,

        FOREIGN KEY(backtest_id)
            REFERENCES backtests(id)
            ON DELETE CASCADE

    )
    """)

    conn.commit()

    conn.close()