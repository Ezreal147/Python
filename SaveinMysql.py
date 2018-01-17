import pymysql.cursors
import random
from base64 import b64encode
def getActivationCode():
    numlist = range(10000000, 99999999)
    num_dic = random.sample(numlist, 200)
    code_dic = []
    for num in num_dic:
        code_dic.append(b64encode(bytes(str(num), 'utf-8'))[:-1])
    return code_dic

if __name__ == '__main__':
    connection=pymysql.Connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='12345yy')
    cursors=connection.cursor()
    cursors.execute('create database if not exists python')
    cursors.execute('use Python;')
    cursors.execute('CREATE TABLE IF NOT EXISTS `activation_code`(`id` INT UNSIGNED AUTO_INCREMENT,`code` VARCHAR(100) NOT NULL,PRIMARY KEY ( `id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    insert='insert into activation_code(code)values'
    code_dic=getActivationCode()
    i=0
    for code in code_dic:
        if i==0:
            i+=1
        else:
            insert+=','
        insert+='("'
        insert+=str(code,'utf-8')
        insert+='")'
    insert+=';'
    cursors.execute(insert)
    cursors.execute('select * from activation_code;')
    print(cursors.fetchall())