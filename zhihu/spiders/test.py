# encoding=utf-8
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	zh_session = requests.session()
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	           'Accept-Encoding': 'gzip, deflate, sdch, br',
	           'Accept-Language': 'zh-CN,zh;q=0.8',
	           'Cache-Control': 'max-age=0',
	           'Connection': 'keep-alive',
	           # 'Cookie':'_zap=c50f1ce1-c039-4878-b673-e76982dab3d1; q_c1=6a7d72f3062043abbabd77ff3edc5e76|1507269943000|1498383708000; __guid=74140564.3330934609671899600.1512185487945.4722; q_c1=6a7d72f3062043abbabd77ff3edc5e76|1514351088000|1498383708000; l_cap_id="MGMzMGI4OWNkNjMwNGM2M2FmOTRiNDlhZjEyMTZkNDc=|1516868430|b0764c668f61a3d1929dafe72fbd7ede9e8bd499"; r_cap_id="MzRiYTQ3MmZlZWVmNDdhMGI0YTk2OGIzNTRhODBlYzk=|1516868430|e19f2f42efbff9f2685cbdf70b045e31ccc8827c"; cap_id="MDgxM2Y0ODA3MzZmNDAzYzg2ZjkyYjlmMzQwMmU4YmM=|1516868430|642196eb34149739c24a17f00a6e970cedcc3cfe"; aliyungf_tc=AQAAAPYyW3zyxQoAk6i1J2cqid4Izger; d_c0="AEBrdMFhDA2PTjhtOXBSBxchNts96dl7gwk=|1516949231"; __utma=51854390.2068399816.1516949324.1516949324.1516949324.1; __utmb=51854390.0.10.1516949324; __utmc=51854390; __utmz=51854390.1516949324.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20170308=1^3=entry_date=20170308=1; _xsrf=aa5d755c-22f5-4d6f-af84-d41ed4ac9808; capsion_ticket="2|1:0|10:1516950735|14:capsion_ticket|44:YWI1NDJiODI1YzllNDY1Mzg2NDE1MWNkOWNkYzkwYTk=|0d76740455433f3ea364809a4a7bcd74c5ca6bcba3bc0ddd7414d6cabbaa83cf"',
	           'Host': 'www.zhihu.com',
	           'Upgrade-Insecure-Requests': '1',
	           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	response = zh_session.get(url='https://www.zhihu.com/signup?next=%2F', headers=headers)
	print(BeautifulSoup(response.text, 'lxml'))
	print(response.cookies)
