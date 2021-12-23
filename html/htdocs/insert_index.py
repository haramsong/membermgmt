import pymysql

# connection 정보
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='hrsong502',
    db='club_member_mgmt',
    charset='utf8'
)
try:
    curs = conn.cursor()
    sql = "SELECT a.member_id, a.name, a.phone_number, b.start_date, b.due_date FROM member as a left outer join " \
          "time_manage as b on a.member_id = b.member_id order by a.member_id, b.start_date desc"
    curs.execute(sql)
    conn.commit()
    data = curs.fetchall()
    for i in data:
        print(i[3])
    # type : datetime.date, 출력 2020-08-05

#     insert와 delete 동시에 사용 가능

finally:
    conn.close()
