import sqlite3

CONN = sqlite3.connect('C:/Users/andrt/PycharmProjects/ConTia/dp/contia_dp.db')
cur = CONN.cursor()


def get_cursor():
    return cur


def timer_create_dp(user_id, time):
    cur.execute(f"""INSERT INTO Time (user_id, time)
VALUES ({user_id}, '{time}');""")
    cur.connection.commit()
    return


def timer_del_dp(user_id, time):
    cur.execute(f"""DELETE FROM Time
where user_id = '{user_id}' and time = '{time}';""")
    cur.connection.commit()
    return


def timer_info_dp(user_id):
    cur.execute(f"""SELECT time FROM Time
where user_id == '{user_id}';""")
    c = cur.fetchall()
    all_timers = list(map(lambda x: x[0], c))
    return all_timers
