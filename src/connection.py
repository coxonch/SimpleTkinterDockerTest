import sqlite3
 
def Database(database):
    global conn, cursor
    # database = "./sqlite.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS `windchill_vault_20220224` (	Column1 TEXT, Column2 TEXT,	Column3 TEXT, Column4 TEXT,	Column5 TEXT, Column6 INTEGER, Column7 INTEGER, Column8 TEXT, Column9 TIMESTAMP, Column10 TIMESTAMP, Column11 TEXT, Column12 TEXT, Column13 TEXT, Column14 TEXT)")
    except Exception as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn