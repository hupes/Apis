# conding:utf8
from django.db import connection, transaction

'''
直接执行原生的sql 查询
sql = sql 语句
params = 查询参数
'''


def my_custom_sql(sql, params):
    cursor = connection.cursor()

    # 数据修改操作——提交要求
    # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", 11)
    # transaction.commit_unless_managed()

    # 数据检索操作,不需要提交
    cursor.execute(sql, params)

    # 返回一行
    # data = cursor.fetchone()

    # 返所有
    data = dictfetchall(cursor)
    return data


# 将返回结果转换成字典
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


'''
执行sql语句查询
sql = sql语句
obj_model = models 对象
'''


def my_person_sql(raw_sql, obj_model):
    raw_querySet = None

    if raw_sql or obj_model:
        raw_querySet = obj_model.objects.raw(raw_sql)

    return raw_querySet
