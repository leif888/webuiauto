import pymysql

from util_tools.handle_data.configParse import ConfigParse
from util_tools.logs_util.recordlog import logs

conf = ConfigParse()


class ConnectMysql:

    def __init__(self):
        self.conf = {
            'host': conf.get_section_mysql('host'),
            'port': int(conf.get_section_mysql('port')),
            'user': conf.get_section_mysql('username'),
            'password': conf.get_section_mysql('password'),
            'database': conf.get_section_mysql('database')
        }
        try:
            self.conn = pymysql.connect(**self.conf)
            # 获取操作游标
            # cursor=pymysql.cursors.DictCursor：将数据表表字段显示，以key-value形式展示
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            logs.info(f'成功连接到数据库，数据ip：{self.conf.get("host")}')
        except Exception as e:
            logs.error(f'连接数据库失败，{e}')

    def close(self):
        if self.conn and self.cursor:
            self.conn.close()
            self.cursor.close()
        return True

    def query(self, sql, fetchall=False):
        """
        查询数据库数据
        :param sql: 查询的SQL语句
        :param fetchall: 查询全部数据，默认为False则查询单条数据
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            if fetchall:
                res = self.cursor.fetchall()
            else:
                res = self.cursor.fetchone()
            return res
        except Exception as e:
            logs.error(f'查询数据库内容出现异常，{e}')
        finally:
            self.close()

    def delete(self, sql):
        """
        删除数据库内容
        :param sql: 删除的SQL语句
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logs.info('数据库数据删除成功')
        except Exception as e:
            logs.error(f'删除数据库数据出现异常，{e}')
        finally:
            self.close()
