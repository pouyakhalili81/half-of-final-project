import mysql.connector
from CONFIG import *

def create_table_User(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS User (
        ID BIGINT PRIMARY KEY,
        USERNAME VARCHAR(50) NOT NULL,
        FULLNAME VARCHAR(50) NOT NULL,
        SCORE INT DEFAULT 0,
        JOIN_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
        LAST_ACTIVE DATETIME,
        LAST_UPDATE DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table User has been created!')

def create_table_Goal(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Goal (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        USER_ID BIGINT NOT NULL,
        GOAL_TEXT VARCHAR(500) NOT NULL,	
        STATUS ENUM('ACTIVE', 'DONE', 'ARCHIVED') NOT NULL DEFAULT 'ACTIVE',
        AIM_DATE DATE,
        CREATED_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,
        LAST_UPDATE DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES User(ID)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Goal has been created!')

def create_table_Reminder(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Reminder (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        USER_ID BIGINT NOT NULL,
        REMI_TEXT VARCHAR(500) NOT NULL,
        GOAL_ID INT NOT NULL,
        REMI_TIME DATETIME NOT NULL,
        ORDER_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,
        LAST_UPDATE DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES User(ID),
        FOREIGN KEY (GOAL_ID) REFERENCES Goal(ID)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Reminder has been created!')

def create_table_Goal_report(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Goal_report (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        GOAL_ID INT NOT NULL,
        USER_ID BIGINT NOT NULL,
        GOAL_REPORT VARCHAR(500) NOT NULL,
        REPORT_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,
        LAST_UPDATE DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES User(ID),
        FOREIGN KEY (GOAL_ID) REFERENCES Goal(ID)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Goal_report has been created!')

def create_table_Score_log(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Score_log (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        USER_ID BIGINT NOT NULL,
        GOAL_ID INT DEFAULT NULL,
        REMINDER_ID INT DEFAULT NULL,
        CHANGE_SCORE INT NOT NULL,
        SCORE_REASON VARCHAR(100) NOT NULL,
        SCORE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,
        SOURCE_TYPE ENUM('GOAL', 'REMINDER', 'SYSTEM') NOT NULL,
        LAST_UPDATE DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES User(ID),
        FOREIGN KEY (GOAL_ID) REFERENCES Goal(ID),
        FOREIGN KEY (REMINDER_ID) REFERENCES Reminder(ID)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Score_log has been created!')

def create_table_Motive(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Motive (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        MOTIVE_TEXT VARCHAR(500) NOT NULL,
        SEND_TIME TIME DEFAULT '07:00:00'
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Motive has been created!')

def create_table_Daily_plan(): 
    conn = mysql.connector.MySQLConnection(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Daily_plan (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        USER_ID BIGINT NOT NULL,
        TASK_TEXT VARCHAR(300) NOT NULL,
        PLAN_DATE DATE NOT NULL,
        IS_DONE BOOLEAN DEFAULT FALSE,
        CREATED_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES User(ID)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table Daily_plan has been created!')

def create_all_tables():
    create_table_User()
    create_table_Goal()
    create_table_Reminder()
    create_table_Goal_report()
    create_table_Score_log()
    create_table_Motive()
    create_table_Daily_plan()

if __name__ == "__main__":
    create_all_tables()
