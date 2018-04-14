# coding:utf8

# 解析json 节点不存在返回None  strDic=['','']  jsonObj= Json对象
import re


def dict_json(strDic, jsonObj, is_toStr=True):
    try:
        for nextDic in strDic:
            jsonObj = jsonObj[nextDic]
    except Exception as e:
        return None

    if is_toStr:
        return str(jsonObj)
    return jsonObj


'''
        保存response 的上下文到mysql 里面去
        该方法会解析html ，或者json 然后调用，save方法保存到mysql里面去
    '''


def re_replace_title(data):
    try:
        message = str(data)
        ret1 = re.sub(r'<span class=H>', ' ', message)
        ret2 = re.sub(r'</span>', ' ', ret1)
        return ret2
    except:
        return ''
        pass
