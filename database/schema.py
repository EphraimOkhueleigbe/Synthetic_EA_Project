cursor.execute("""
CREATE TABLE IF NOT EXISTS strategies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    project_id INTEGER NOT NULL,

    name TEXT NOT NULL,

    d1_fast_ema INTEGER NOT NULL DEFAULT 9,
    d1_slow_ema INTEGER NOT NULL DEFAULT 18,

    m30_fast_ema INTEGER NOT NULL DEFAULT 9,
    m30_slow_ema INTEGER NOT NULL DEFAULT 18,

    risk_formula TEXT,

    stop_loss_type TEXT,
    stop_loss_value REAL,

    take_profit_type TEXT,
    take_profit_value REAL,

    trade_direction TEXT DEFAULT 'Trend',

    active INTEGER DEFAULT 1,

    created_at TEXT,
    updated_at TEXT,

    FOREIGN KEY(project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE

);
""")