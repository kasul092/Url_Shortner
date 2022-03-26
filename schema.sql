DROP TABLE IF EXISTS urls;

CREATE TABLE urls("""
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original url TEXT NOT NULL,
                  clicks INTEGER NOT NULL DEFAULT 0""");