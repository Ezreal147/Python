import redis
import random
from base64 import b64encode
import time
def getActivationCode():
    numlist = range(10000000, 99999999)
    num_dic = random.sample(numlist, 200)
    code_dic = []
    for num in num_dic:
        code_dic.append(b64encode(bytes(str(num), 'utf-8'))[:-1])
    return code_dic
if __name__ == '__main__':
    connection=redis.Redis(host='localhost',port=6379,db=0)
    code_dic=getActivationCode()
    key='activation_code'
    if connection.exists(key):
        connection.delete(key)
    for code in code_dic:
        connection.sadd(key, code)
    print(connection.smembers(key))
