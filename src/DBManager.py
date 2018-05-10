# -*- coding: utf-8 -*-
import MySQLdb


class DBManager:
    """
    数据库管理类
    """

    def __init__(self, host, port, user, password, db_name):
        self.create_db(host, port, user, password, db_name)
        self.conn = MySQLdb.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    db=db_name,
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        self.create_table('her')

    def create_db(self, host, port, user, pwd, db_name):
        conn = MySQLdb.connect(host=host,
                               port=port,
                               user=user,
                               password=pwd,
                               db='sys',
                               charset='utf8')
        if conn.cursor().execute('SHOW DATABASES LIKE \'%s\';' % db_name) == 0:
            conn.cursor().execute('CREATE DATABASE %s CHARACTER SET utf8;' % db_name)

    def create_table(self, table_name):
        tb_exist = self.cursor.execute('show tables like \'%s\'' % table_name)
        if tb_exist == 0:
            table_sql = 'CREATE TABLE %s (\
                        id           INT AUTO_INCREMENT PRIMARY KEY,\
                        wei_id       VARCHAR(50)  NOT NULL, \
                        name         VARCHAR(50)  NOT NULL,\
                        url          VARCHAR(200) NOT NULL,\
                        match_school BOOL         NOT NULL,\
                        assay_count  INT          NOT NULL\
                        );' % table_name
            self.cursor.execute(table_sql)
            self.conn.commit()

    def add_a_fan(self, fan, match_school, assay_count):
        user_str = 'SELECT id FROM her WHERE id = \'%s\';' % fan.id
        print(user_str)
        user_exist = self.cursor.execute(user_str)
        print(user_exist)
        if user_exist == 0:
            add_str = 'INSERT INTO her(wei_id,name,url,match_school,assay_count) \
                               VALUES (\'%s\',\'%s\',\'%s\',%s,%d)' % \
                      (fan.id, fan.name, fan.url, match_school, assay_count)
            self.cursor.execute(add_str)
            self.conn.commit()

    def close(self):
        self.cursor.close()
