import mysql.connector
from CONFIG import *

# ---------- INSERT FUNCTIONS ----------

def insert_data_User(ID, username, fullname, age):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO User (ID, USERNAME, FULLNAME, AGE)
            VALUES (%s, %s, %s, %s);
        """, (ID, username, fullname, age))
        conn.commit()
        print(f'User added: {(ID, username, fullname, age)}')
    except Exception as f:
        print(f"Error in insert_data_User: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Goal(user_id, goal_title, goal_text,aim_date):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO goal (USER_ID, GOAL_TITLE, GOAL_TEXT,AIM_DATE)
            VALUES (%s, %s, %s,%s);
        """, (user_id, goal_title, goal_text,aim_date))
        conn.commit()
        last_id = cur.lastrowid
        print(f"Goal inserted with ID: {last_id}")
        return last_id
    except Exception as e:
        print(f"Error in insert_data_Goal: {e}")
    finally:
        cur.close()
        conn.close()



def insert_data_Reminder(user_id, remi_text, goal_id, remi_time):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Reminder (USER_ID, REMI_TEXT, GOAL_ID, REMI_TIME)
            VALUES (%s, %s, %s, %s);
        """, (user_id, remi_text, goal_id, remi_time))
        conn.commit()
        last_id = cur.lastrowid
        print(f"Reminder inserted with ID: {last_id}")
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Reminder: {f}")
    finally:
        cur.close()
        conn.close()

# ---------- UPDATE FUNCTIONS ----------

def update_data_Goal(goal_id, goal_title=None, goal_text=None, status=None, aim_date=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        update_fields = []
        values = []
        if goal_title is not None:
            update_fields.append("GOAL_TITLE = %s")
            values.append(goal_title)
        if goal_text is not None:
            update_fields.append("GOAL_TEXT = %s")
            values.append(goal_text)
        if status is not None:
            update_fields.append("STATUS = %s")
            values.append(status)
        if aim_date is not None:
            update_fields.append("AIM_DATE = %s")
            values.append(aim_date)
        if last_update is not None:
            update_fields.append("LAST_UPDATE = %s")
            values.append(last_update)

        values.append(goal_id)

        sql = f"UPDATE Goal SET {', '.join(update_fields)} WHERE ID = %s"
        cur.execute(sql, tuple(values))
        conn.commit()
        print(f"Goal {goal_id} updated.")
    except Exception as f:
        print(f"Error in update_data_Goal: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Reminder(reminder_id, remi_text=None, remi_time=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        update_fields = []
        values = []
        if remi_text is not None:
            update_fields.append("REMI_TEXT = %s")
            values.append(remi_text)
        if remi_time is not None:
            update_fields.append("REMI_TIME = %s")
            values.append(remi_time)
        if last_update is not None:
            update_fields.append("LAST_UPDATE = %s")
            values.append(last_update)

        values.append(reminder_id)
        sql = f"UPDATE Reminder SET {', '.join(update_fields)} WHERE ID = %s"
        cur.execute(sql, tuple(values))
        conn.commit()
        print(f"Reminder {reminder_id} updated.")
    except Exception as f:
        print(f"Error in update_data_Reminder: {f}")
    finally:
        cur.close()
        conn.close()

# ---------- DELETE FUNCTIONS ----------

def delete_from_Goal(goal_id):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("DELETE FROM Goal WHERE ID = %s", (goal_id,))
        conn.commit()
        print(f"Goal {goal_id} deleted.")
    except Exception as f:
        print(f"Error in delete_from_Goal: {f}")
    finally:
        cur.close()
        conn.close()

def delete_from_Reminder(reminder_id):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("DELETE FROM Reminder WHERE ID = %s", (reminder_id,))
        conn.commit()
        print(f"Reminder {reminder_id} deleted.")
    except Exception as f:
        print(f"Error in delete_from_Reminder: {f}")
    finally:
        cur.close()
        conn.close()

# ---------- SELECT (SHOW) FUNCTIONS ----------

def show_all_Goal(user_id):
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("SELECT ID, GOAL_TITLE, GOAL_TEXT, aim_date FROM Goal WHERE USER_ID = %s", (user_id,))
        show = cur.fetchall()
        cur.close()
        conn.close()
        return show
    

def show_all_Reminder(user_id):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("SELECT ID, REMI_TEXT, REMI_TIME FROM Reminder WHERE USER_ID = %s", (user_id,))
        return cur.fetchall()
    except Exception as f:
        print(f"Error in show_all_Reminder: {f}")
        return []
    finally:
        cur.close()
        conn.close()

def is_user_exists(cid):
    conn = mysql.connector.connect(**config)
    cur = conn.cursor()
    
    query = "SELECT 1 FROM user WHERE ID = %s"
    cur.execute(query, (cid,))
    exists = cur.fetchone() is not None

    cur.close()
    conn.close()
    return exists

