#-*-coding:utf8-*-
from bs4 import BeautifulSoup
import urllib.request as urlrequest
import re #用于正则处理的包
exit_flag=False
citys_dict={
    'beijing':'北京',
    'shanghai':'上海',
    'guangzhou':'广州',
    'wuhan':'武汉',
    'chengdu':'成都',
    'shenzhen':'深圳',
    'hangzhou':'杭州',
    'xian':'西安',
    'nanjing':'南京',
    'zhengzhou':'郑州',
    'changsha':'长沙',
    'wenzhou':'温州',
    'fuzhou':'福州',
    'shenyang':'沈阳'
}
#城市列表，用于循环控制城市取数
citys=['beijing',
'shanghai',
'guangzhou',
'wuhan',
'chengdu',
'shenzhen',
'hangzhou',
'xian',
'nanjing',
'zhengzhou',
'changsha',
'wenzhou',
'fuzhou',
'shenyang'
]

for city in citys_dict.keys():
    #douban_url='https://{}.douban.com/events/future-all?start={}'
    douban_url='https://www.douban.com/location/{}/events/future-all?start={}'
    for i in range(2000):
        start=10*i
        #传入参数
        url_visit=douban_url.format(city,start)
        web_page=urlrequest.urlopen(url_visit).read()
        soup=BeautifulSoup(web_page,'lxml')
        #print(soup.prettify())
        all_event_list=soup.find(class_='events-list events-list-pic100 events-list-psmall')
        #元素为空跳出内循环
        if all_event_list == None:
            exit_flag==True
            break
            #continue
            
        all_list_entry=all_event_list.find_all(class_='list-entry')
        #写文件会出现gbk' codec can't encode character错误，加上encoding="utf-8"解决问题
        #写文件w为覆盖写入，a为追加写入
        with open('doubantongcheng.csv','a',encoding="utf-8") as outputfile:
            #循环取出元素
            for each_item_div in all_list_entry:
                title_div=each_item_div.find(class_='title')
                fee_div=each_item_div.find(class_='fee')
                time_div=each_item_div.find(class_='event-time')
                count_div=each_item_div.find(class_='counts')
            #    print(pic_div)
                each_item_div.find(class_='title')
                item_href=title_div.find('a')['href']
                item_name=re.sub(r'\"','',title_div.find('a')['title']) #活动名称中可能含有双引号，csv打开可能错位，把双引号替换

                each_item_div.find(class_='fee')
                item_fee=fee_div.find('strong').get_text()
                item_time=time_div.find('time')['datetime']
                item_count=re.sub(r'人参加','',count_div.find('span').get_text())
            #    item_time2=time_div.find_all(time='datetime')
                outputfile.write('{},{},{},{},{},{}\n'.format(city,"\""+item_name+"\"",item_href,item_fee,item_time,item_count))
                print('{},{},{},{},{},{}'.format(city,"\""+item_name+"\"",item_href,item_fee,item_time,item_count))
                #print('{}'.format(item_href))
