from aip import AipOcr
import time
import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
APP_ID='******'#百度云api的账号，需要自己去注册
API_KEY='********'#同上，需填写
SECRET_KEY='********'#同上
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
if __name__ == '__main__':
    baidu = webdriver.Edge()#需要下载edge浏览器驱动并且添加目录到path
    baidu.get('http://www.baidu.com')
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    flag = 0
    while True:
        shipin = input('西瓜视频请输入1，非西瓜2')
        if shipin == '1':
            flag = 1
            break
        elif shipin == '2':
            flag = 0
            break
        else:
            print("输入错误")    
    while True:
        input('按回车获取题目：')
        start=time.time()
        os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png D:\PythonProject\RsaTest\\screenshot.png')
        txt=client.general(get_file_content('screenshot.png'))
        s=''
        choose1=''
        choose2=''
        choose3=''
        for i in txt.get('words_result'):
            if (i.get('location').get('top')>350)&(i.get('location').get('top')<500):
                s+=i.get('words')
            elif (i.get('location').get('top')>650)&(i.get('location').get('top')<830):
                choose1+=i.get('words')
            elif (i.get('location').get('top')>835)&(i.get('location').get('top')<1025):
                choose2+=i.get('words')
            elif (i.get('location').get('top') > 1030) & (i.get('location').get('top') < 1050):
                choose3 += i.get('words')
                break
        search = baidu.find_element_by_id('kw')
        search.click()
        search.clear()
        if flag==1:
            search.send_keys(s[2:])
        else:
            search.send_keys(s)
        searchbutton = baidu.find_element_by_id('su')
        searchbutton.click()
        page=baidu.page_source
        t1=re.findall(choose1,page).__len__()
        t2=re.findall(choose2,page).__len__()
        t3=re.findall(choose3,page).__len__()
        if flag==1:
            print(s[2:])
        else:
            print(s)
        print('choose1:%d'%t1)
        print('choose2:%d'%t2)
        print('choose3:%d'%t3)
        end = time.time()
        print('runtime: ' + str(end - start))
