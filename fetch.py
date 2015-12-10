import requests as rq
import re
import pandas as pd
import json

#url='http://world.tmall.com/item/44320847678.htm?'
base_url='https://rate.tmall.com/list_detail_rate.html?'
itemId='itemId=44320847678&spuId=327809007&sellerId=1732577545'
orderByTime='&order=1'
url='https://rate.tmall.com/list_detail_rate.htm?itemId=44320847678&spuId=327809007&sellerId=1732577545&order=3&currentPage=0&append=0&content=1'

myweb = rq.get(url)

#print myweb.text.encode('utf-8')
content = re.findall('\"rateList\":(\[.*?\])\,\"tags\"',myweb.text.encode('utf-8'))[0]
myjson = json.loads(content)
#print json.dumps(myjson,indent=4, separators=(',', ': '),ensure_ascii=False).encode('utf-8')

mytable = pd.read_json(content)
a=mytable['rateDate']
b=mytable['rateContent']
print b
#mytable.to_csv('mytable.txt')

