# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#把爬取的数据存放到数据库
import MySQLdb
class LagouwangPipeline(object):
    def process_item(self, item, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()
        sql = ("insert into lagou(idlagou,positionname,city,salary,company,request,provide,welfare_1,welfare_2,welfare_3,welfare_4,companykinds) "
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        lis = (item['pk'],item['positionname'][0],item['city'][0],item['salary'][0],item['company'][0],item['request'],item['provide'][0],item['welfare'][0],
               item['welfare'][1],item['welfare'][2],item['welfare'][3],item['companykinds'])
        try:
            cur.execute(sql,lis)
        except Exception,e:
            print "Insert error:",e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item
