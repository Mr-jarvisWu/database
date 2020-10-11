import pymysql


def main():
    # 默认创建一个事务,不会自动提交
    conn = pymysql.connect(host='47.98.168.117', port=3306,
                           user='root', password='Wu126084!',
                           db='jarvis', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute('insert into 成绩表 values(6,"jarivs","数学","99")')
            if result == 1:
                print('添加成功')
            conn.commit()  # 提交事务

    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()  # 回滚事务

    finally:  # 总是执行的代码，一定要关闭连接
        conn.close()
        # print(conn)   # 判断是否连接到数据库


if __name__ == '__main__':
    main()
