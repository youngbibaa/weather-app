stmt_create = """
    CREATE TABLE base (
        id TEXT,
        password TEXT
    )
"""
stmt_add = """
INSERT INTO base (id, password) VALUES (?, ?)
"""
stmt_select = """
SELECT id, password FROM base WHERE id = ?
"""
