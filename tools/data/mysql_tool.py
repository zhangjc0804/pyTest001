# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/10 6:26

import pymysql

def connect(**db):
    conn = pymysql.connect(**db)
    return conn


def query_one(sql,conn):
    # print(type(db))
    # conn = connect(**db)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        # 执行sql语句
        cursor.execute(sql)
        row = cursor.fetchone()
        return row
    except Exception as  e:
        # 如果执行sql语句出现问题，则执行回滚操作
        print(e)
    finally:
        # 不论try中的代码是否抛出异常，这里都会执行
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()



class DataBaseHandle(object):
    ''' 定义一个 MySQL 操作类'''


    # def __init__(self,host,username,password,database,port):
    #     '''初始化数据库信息并创建数据库连接'''
    #     # 下面的赋值其实可以省略，connect 时 直接使用形参即可
    #     self.host = host
    #     self.username = username
    #     self.password = password
    #     self.database = database
    #     self.port = port
    #     self.db = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset='utf8')

    def __init__(self,**db):
        conn = pymysql.connect(**db)
        self.db=conn


    #  这里 注释连接的方法，是为了 实例化对象时，就创建连接。不许要单独处理连接了。
    #
    # def connDataBase(self):
    #     ''' 数据库连接 '''
    #
    #     self.db = pymysql.connect(self.host,self.username,self.password,self.port,self.database)
    #
    #     # self.cursor = self.db.cursor()
    #
    #     return self.db

    def insertDB(self,sql):
        ''' 插入数据库操作 '''

        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # print(tt)
            self.db.commit()
            resp['result'] = self.cursor.rowcount
            return resp
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            print(e)
            resp['status'] = '0001'
            resp['error'] = e
            return resp
        finally:
            self.cursor.close()



    def deleteDB(self,sql):
        ''' 操作数据库数据删除 '''

        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # print(tt)
            self.db.commit()
            resp['result'] = self.cursor.rowcount
            return resp
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            print(e)
            resp['status'] = '0001'
            resp['error'] = e
            return resp
        finally:
            self.cursor.close()





    def updateDb(self,sql):
        ''' 更新数据库操作 '''
        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # print(tt)
            self.db.commit()
            resp['result'] = self.cursor.rowcount
            return resp
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            print(e)
            resp['status']='0001'
            resp['error']=e
            return resp
        finally:
            self.cursor.close()




    def selectDb(self,sql):
        ''' 数据库查询 '''
        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            content = self.cursor.fetchall() # 返回所有记录列表

            # 获取表头
            labels = self.cursor.description
            labels = [l[0] for l in labels]

            table_data={}
            table_data['content']=content
            table_data['labels']=labels
            resp['result']=table_data
            return resp
        except Exception as e:
            print(e)
            resp['status']='0001'
            resp['error']=e
            return resp
        finally:
            self.cursor.close()

    def showDb(self,sql):

        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            content = self.cursor.fetchall()  # 返回所有记录列表

            # 获取表头
            labels = self.cursor.description
            labels = ['name']

            table_data = {}
            table_data['content'] = content
            table_data['labels'] = labels
            resp['result']=table_data
            return resp
        except Exception as e:
            print(e)
            resp['status'] = '0001'
            resp['error'] = e
            return resp
        finally:
            self.cursor.close()

    def useDb(self,sql):

        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            return resp
        except Exception as e:
            print(e)
            resp['status'] = '0001'
            resp['error'] = e
            return resp
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()



if __name__ == '__main__':

    DbHandle = DataBaseHandle('127.0.0.1','adil','helloyyj','AdilTest',3306)

    DbHandle.insertDB('insert into test(name) values ("%s")'%('FuHongXue'))
    DbHandle.insertDB('insert into test(name) values ("%s")'%('FuHongXue'))
    DbHandle.selectDb('select * from test')
    DbHandle.updateDb('update test set name = "%s" where sid = "%d"' %('YeKai',22))
    DbHandle.selectDb('select * from test')
    DbHandle.insertDB('insert into test(name) values ("%s")'%('LiXunHuan'))
    DbHandle.deleteDB('delete from test where sid > "%d"' %(25))
    DbHandle.selectDb('select * from test')
    DbHandle.closeDb()