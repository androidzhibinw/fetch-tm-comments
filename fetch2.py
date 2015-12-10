import requests as rq
import re
import pandas as pd
import json
import sys
import datetime

url='http://world.tmall.com/item/44320847678.htm?spm=a220m.1000858.0.0.K7jhC4&id=44320847678&is_b=1&cat_id=2&q=%BC%D7%C8%A9'
URL_BASE= 'https://rate.tmall.com/list_detail_rate.htm?'

SPU_PREFIX='spuId='
SELLER_PREFIX='sellerId='
ITEM_PREFIX='itemId='
AND='&'

def getSpuId(data):
    sup_m= re.search(SPU_PREFIX+'\d*',data)
    if sup_m:
        return str(sup_m.group(0))
    else:
        return None

def getSellerId(data):
    seller_m = re.search(SELLER_PREFIX+'\d*',data)
    if seller_m:
        return str(seller_m.group(0))
    else:
        return None

def getItemId(data):
    item_m = re.search(ITEM_PREFIX+'\d*',data)
    if item_m:
        return str(item_m.group(0))
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'fetch2.py url'
        sys.exit()
    myweb = rq.get(sys.argv[1])
    raw = myweb.text.encode('utf-8')
    spuId = getSpuId(raw)
    sellerId = getSellerId(raw)
    itemId = getItemId(raw)
    url_c = URL_BASE+spuId+AND+sellerId+AND+itemId
    print url_c
    comm = rq.get(url_c)
    print comm.text


