import mysql.connector
from CONFIG import *

def insert_data_User(ID, username, fullname,age, score=None, join_date=None, last_active=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO User (ID, USERNAME, FULLNAME, SCORE, JOIN_DATE, LAST_ACTIVE, LAST_UPDATE)
            VALUES (%s, %s, %s, %s, %s, %s, %s,%s);
        """, (ID, username, fullname,age, score, join_date, last_active, last_update))
        conn.commit()
        print(f'this data\n{ID, username, fullname,age, score, join_date, last_active, last_update}\nhas added to table User!!')
    except Exception as f:
        print(f"Error in insert_data_User: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Goal(user_id, goal_text, status=None, aim_date=None, created_time=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Goal (USER_ID, GOAL_TEXT, STATUS, AIM_DATE, CREATED_TIME, LAST_UPDATE)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (user_id, goal_text, status, aim_date, created_time, last_update))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, user_id, goal_text, status, aim_date, created_time, last_update}\nhas added to table Goal!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Goal: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Reminder(user_id, remi_text, goal_id, remi_time, order_time=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Reminder (USER_ID, REMI_TEXT, GOAL_ID, REMI_TIME, ORDER_TIME, LAST_UPDATE)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (user_id, remi_text, goal_id, remi_time, order_time, last_update))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, user_id, remi_text, goal_id, remi_time, order_time, last_update}\nhas added to table Reminder!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Reminder: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Goal_report(goal_id, user_id, goal_report, report_time=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Goal_report (GOAL_ID, USER_ID, GOAL_REPORT, REPORT_TIME, LAST_UPDATE)
            VALUES (%s, %s, %s, %s, %s);
        """, (goal_id, user_id, goal_report, report_time, last_update))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, goal_id, user_id, goal_report, report_time, last_update}\nhas added to table Goal_report!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Goal_report: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Score_log(user_id, goal_id=None, reminder_id=None, change_score=0, score_reason=None, score_time=None, source_type=None, last_update=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Score_log (USER_ID, GOAL_ID, REMINDER_ID, CHANGE_SCORE, SCORE_REASON, SCORE_TIME, SOURCE_TYPE, LAST_UPDATE)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (user_id, goal_id, reminder_id, change_score, score_reason, score_time, source_type, last_update))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, user_id, goal_id, reminder_id, change_score, score_reason, score_time, source_type, last_update}\nhas added to table Score_log!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Score_log: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Motive(motive_text, send_time=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Motive (MOTIVE_TEXT, SEND_TIME)
            VALUES (%s, %s);
        """, (motive_text, send_time))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, motive_text, send_time}\nhas added to table Motive!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Motive: {f}")
    finally:
        cur.close()
        conn.close()

def insert_data_Daily_plan(user_id, task_text, plan_date, is_done=None, created_time=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Daily_plan (USER_ID, TASK_TEXT, PLAN_DATE, IS_DONE, CREATED_TIME)
            VALUES (%s, %s, %s, %s, %s);
        """, (user_id, task_text, plan_date, is_done, created_time))
        conn.commit()
        last_id = cur.lastrowid
        print(f'this data\n{last_id, user_id, task_text, plan_date, is_done, created_time}\nhas added to table Daily_plan!!')
        return last_id
    except Exception as f:
        print(f"Error in insert_data_Daily_plan: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_User(ID, username1, fullname1):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE User SET USERNAME = %s, FULLNAME = %s WHERE ID = %s
        """, (username1, fullname1, ID))
        conn.commit()
        print(f'this data\n{ID, username1, fullname1}\nhas changed!!')
    except Exception as f:
        print(f"Error in update_data_User: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Goal(user_id, goal_text1, status1, aim_date1):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE Goal SET GOAL_TEXT = %s, STATUS = %s, AIM_DATE = %s WHERE USER_ID = %s;
        """, (goal_text1, status1, aim_date1, user_id))
        conn.commit()
        print(f'This goal for user {user_id} has been updated:\nText: {goal_text1}, Status: {status1}, Aim Date: {aim_date1}')
    except Exception as f:
        print(f"Error in update_data_Goal: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Reminder(reminder_id, remi_text1, remi_time1):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE Reminder SET REMI_TEXT = %s, REMI_TIME = %s WHERE ID = %s
        """, (remi_text1, remi_time1, reminder_id))
        conn.commit()
        print(f'your reminder text has updated to {remi_text1}!!\nyour reminder time has updated to {remi_time1}!!')
    except Exception as f:
        print(f"Error in update_data_Reminder: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Goal_report(goal_report1, goal_id, user_id):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE Goal_report SET GOAL_REPORT = %s WHERE GOAL_ID = %s AND USER_ID = %s
        """, (goal_report1, goal_id, user_id))
        conn.commit()
        print(f'your goal report has updated to {goal_report1}!!')
    except Exception as f:
        print(f"Error in update_data_Goal_report: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Score_log(log_id, change_score=0, score_reason=None, score_time=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE Score_log SET CHANGE_SCORE = %s, SCORE_REASON = %s , SCORE_TIME = %s WHERE ID = %s
        """, (change_score, score_reason, score_time, log_id))
        conn.commit()
        affected_rows = cur.rowcount
        print(f'as your new command:\nchange_score = {change_score}\nscore_reason = {score_reason}\nscore_time = {score_time}\nedit has successfully done for log {log_id}')
        return affected_rows
    except Exception as f:
        print(f"Error in update_data_Score_log: {f}")
    finally:
        cur.close()
        conn.close()

def update_data_Daily_plan(plan_id, task_text1, plan_date1, is_done1=None):
    try:
        conn = mysql.connector.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute("""
            UPDATE Daily_plan SET TASK_TEXT = %s, PLAN_DATE = %s , IS_DONE = %s WHERE ID = %s
        """, (task_text1, plan_date1, is_done1, plan_id))
        conn.commit()
        affected_rows = cur.rowcount
        print(f'as your new command:\ntask_text = {task_text1}\nplan_date = {plan_date1}\nis_done = {is_done1}\nedit has successfully done for plan {plan_id}')
        return affected_rows
    except Exception as f:
        print(f"Error in update_data_Daily_plan: {f}")
    finally:
        cur.close()
        conn.close()
