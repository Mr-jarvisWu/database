import pymysql


def conn_sql():
    conn = pymysql.connect(host='47.98.168.117',port=3306,
                       user='root',db='jarvis',
                       password='Wu126084!',charset='utf8')
    print(conn)
    dlt = int(input('请输入需要删除的id:'))
    try:
        with conn.cursor() as cursor:
            result = cursor.execute('delete from 成绩表 where id=%s'%dlt)
            if result == 1:
                print('删除成功')
                conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
        conn_sql()