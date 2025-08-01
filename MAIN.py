import mysql.connector

def create_n_drop_database(db_name):
    conn = mysql.connector.MySQLConnection(user = 'root' , password = '123456', host = 'localhost')
    cur = conn.cursor()
    cur.execute(f"""
                CREATE DATABASE IF NOT EXISTS {db_name}
                """)
    conn.commit()
    cur.close()
    conn.close()
    print(f'database in name {db_name} has created!!')

create_n_drop_database('lifemate_db')