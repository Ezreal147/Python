import random
from base64 import b64encode
if __name__ == '__main__':
    numlist=range(10000000,99999999)
    num_dic=random.sample(numlist,200)
    code_dic=[]
    for num in num_dic:
        code_dic.append(b64encode(bytes(str(num),'utf-8'))[:-1])
    print(code_dic)
