# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DongguanPipeline(object):
   
   
    def __init__(self):
    #  self.filename = open("dongguan.json", "w")
      self.nun= 0  
    def process_item(self, item, spider):
     # print(self.nun)
      filename = open(str(self.nun)+'.text','w')
      content = item['content'].encode('utf-8')
      filename.write(content)
      self.nun=self.nun+1
     #print(item['content'].encode('utf-8'))
     # print(item['content'])
     # text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
     # self.filename.write(text.encode("utf-8"))
      return item
#    def close_spider(self, spider):
#      self.filename.close()

