# coding=UTF-8

from __future__ import print_function
import re
import feedparser

urls = ['http://www.cwb.gov.tw/rss/forecast/36_03.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_01.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_04.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_08.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_13.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_02.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_05.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_06.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_14.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_07.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_09.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_10.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_11.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_12.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_16.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_15.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_19.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_18.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_17.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_20.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_21.xml',
        'http://www.cwb.gov.tw/rss/forecast/36_22.xml']

print("CWB RSS Realtime Temperature:")
print("====================================")
for i in range(len(urls)):
    d = feedparser.parse(urls[i])
    data = d.entries[0].title
    print(data[0:3], end=' ')
    print(re.search(r'\d+ ~ \d+', data).group(0))
print("\nCWB RSS Realtime Typhoon Warning:")
print("====================================")
d = feedparser.parse('http://www.cwb.gov.tw/rss/Data/cwb_warning.xml')
if d.entries != None:
    print(d.entries[0].description)
else:
    print("Nothing happend. The world is peace :)")
