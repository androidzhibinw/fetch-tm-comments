import requests as rq
import re
import pandas as pd
import json

#url='http://world.tmall.com/item/44320847678.htm?'
base_url='https://rate.tmall.com/list_detail_rate.html?'
itemId='itemId=44320847678&spuId=327809007&sellerId=1732577545'
# 1 is time ,3 is default
orderByTime='&order=1'
orderByDefault='&order=3'
apend='&append=0'
page='&currentPage='
#tag not good
tagId='&tagId=620'
url='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=1&append=0&content=1&posi=-1&picture=0'
urlD='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=3&append=0&content=1&posi=-1&picture=0'
urlbad='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=1&append=0&content=0&tagId=620'
urlbad2='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=1&append=0&content=1&tagId=620&posi=-1&picture=0'


def getPage(page_id):
    myweb = rq.get(urlD+page+str(page_id))

    #print myweb.text.encode('utf-8')
    content = re.findall('\"rateList\":(\[.*?\])\,\"tags\"',myweb.text.encode('utf-8'))[0]
    myjson = json.loads(content)
    for item in myjson:
        print item['rateDate'].encode('utf-8'),item['rateContent'].encode('utf-8')
    #print json.dumps(myjson,indent=4, separators=(',', ': '),ensure_ascii=False).encode('utf-8')
    #mytable = pd.read_json(content)
    #a=mytable['rateDate']
    #b=mytable['rateContent']
    #print b
    #mytable.to_csv('mytable.txt')


for i in range(1,50):
    getPage(i)
