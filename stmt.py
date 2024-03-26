stmt_main = {
    "create": """
        CREATE TABLE base (
            id TEXT,
            password TEXT
        )
    """,
    "add": """
        INSERT INTO base (id, password) VALUES (?, ?)
    """,
    "select": """
        SELECT id, password FROM base WHERE id = ?
    """,
}
stmt_coordinates = {
    "create": """
        CREATE TABLE coordinates (
            nickname varchar(15),
            lon FLOAT(2),
            lat FLOAT(2)
        )
    """,
    "add": """
        INSERT INTO coordinates (nickname, lon, lat) VALUES (?, ?, ?)
    """,
    "select": """
        SELECT * FROM coordinates WHERE nickname = ?
    """,
}
stmt_cities = {
    "create": """
        CREATE TABLE cities (
            nickname varchar(15),
            city varchar(15)
        )
    """,
    "add": """
        INSERT INTO cities (nickname, city) VALUES (?, ?)
    """,
    "select": """
        SELECT * FROM cities WHERE nickname = ?
    """,
}
