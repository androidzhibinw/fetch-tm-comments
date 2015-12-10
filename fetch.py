import requests as rq
import re
import pandas as pd
import json
import sys
import datetime

#url='http://world.tmall.com/item/44320847678.htm?'
base_url='https://rate.tmall.com/list_detail_rate.html?'
itemId='itemId=44320847678&spuId=327809007&sellerId=1732577545'
# 1 is time ,3 is default
help_msg='''
Usage: fetch.py a/b d/t 
fetch all order by default : fetch.py a d  
fetch all order by time    : fetch.py a t  
fetch bad order by default : fetch.py b d  
fetch bad order by time    : fetch.py b t  
'''
orderByTime='&order=1'
orderByDefault='&order=3'
apend='&append=0'
page='&currentPage='
#tag not good
tagId='&tagId=620'
urlT='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=1&append=0&content=1&posi=-1&picture=0'
urlD='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=3&append=0&content=1&posi=-1&picture=0'
urlbadT='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=1&append=0&content=1&tagId=620&posi=-1&picture=0'
urlbadD='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=3&append=0&content=1&tagId=620&posi=-1&picture=0'
index=0
#0=all, 1=bad
TYPE_ALL = 0
TYPE_BAD = 1
fetch_type = TYPE_ALL

ORDER_DEFAULT = 0
ORDER_TIME = 1
order_type= ORDER_DEFAULT

DEFAULT_PAGES = 50
url = urlD
file_name_prefix=''
sufix='.html'

def getPage(page_id):
    myweb = rq.get(url+page+str(page_id))
    content = re.findall('\"rateList\":(\[.*?\])\,\"tags\"',myweb.text.encode('utf-8'))[0]
    myjson = json.loads(content)
    for item in myjson:
        #if len(item['rateContent'].encode('utf-8')) <400:
        #    continue
        global index
        index += 1
        #print index,' :'
        #print item['rateDate'].encode('utf-8'),item['rateContent'].encode('utf-8')
        #print "</br>"
        out_file.write(str(index)+' :')
        out_file.write(item['rateDate'].encode('utf-8'))
        out_file.write(item['rateContent'].encode('utf-8'))
        out_file.write('</br>')
    #print json.dumps(myjson,indent=4, separators=(',', ': '),ensure_ascii=False).encode('utf-8')
    #mytable = pd.read_json(content)
    #a=mytable['rateDate']
    #b=mytable['rateContent']
    #print b
def printPages(page):
    for i in range(1,page+1):
        getPage(i)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print help_msg
        sys.exit()
    if sys.argv[1] =='a' and  sys.argv[2] == 'd':
        url=urlD
        file_name_prefix='all_by_default'
    elif sys.argv[1] == 'a' and sys.argv[2] == 't':
        url=urlT
        file_name_prefix='all_by_time'
    elif sys.argv[1] == 'b' and sys.argv[2] == 'd':
        url=urlbadD
        file_name_prefix='bad_by_default'
    elif sys.argv[1] == 'b' and sys.argv[2] == 't':
        url=urlbadT
        file_name_prefix='bad_by_time'
    else:
        print help_msg
        sys.exit()
    str_dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    global out_file
    out_file = open(file_name_prefix + str_dt + sufix,'w')
    printPages(DEFAULT_PAGES)
    out_file.close()
