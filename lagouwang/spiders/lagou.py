# coding: utf-8
import scrapy
from lagouwang.items import LagouwangItem

class LagouwangScripy(scrapy.Spider):
    name='lagouwang'
    allowed_domains=['lagou.com']
    start_urls=(
        'https://www.lagou.com/zhaopin/'
    )
    def start_requests(self):
        reqs=[]
        for i in range(1,30):
            url="https://www.lagou.com/zhaopin/Python/{}/?filterOption={}".format(i,i)#处理分页数据确保所有数据都能抓取到
            req=scrapy.Request(url)
            reqs.append(req)
        return reqs

    def parse(self, response):
        job_lists=response.xpath('//*[@id="s_position_list"]/ul/li')
        page_lists=response.xpath('//*[@id="s_position_list"]/div[2]/div/a[@class="page_no pager_is_current"]')#抓取当前页数
        items=[]
        f=0
        for pg in page_lists:
            page=pg.xpath('./@data-index').extract()
            print page,">>>>>>>>>>>"
            for i in job_lists:
                job = LagouwangItem()
                f+=1
                job['pk']=f+(int(page[0])-1)*15
                job['positionname']=i.xpath('./div[1]/div[1]/div[1]/a/h2/text()').extract()
                job['city']=i.xpath('./div[1]/div[1]/div[1]/a/span/em/text()').extract()
                job['positionname']=i.xpath('./div[1]/div[1]/div[1]/a/h2/text()').extract()
                job['company']=i.xpath('./div[1]/div[2]/div[1]/a/text()').extract()
                job['salary']=i.xpath('./div[1]/div[1]/div[2]/span/text()').extract()
                a=i.xpath('./div[1]/div[1]/div[2]/div/text()').extract()
                job['request']=a[1].strip()
                l=i.xpath('./div[1]/div[2]/div[2]/text()').extract()
                job['companykinds']=l[0].strip()
                job['provide']=i.xpath('./div[2]/div[1]/text()').extract()
                welfare=i.xpath('./div[2]/div[2]/span')
                s=[]
                for k in welfare:
                    p=k.xpath('text()').extract()
                    s.append(p)
                job['welfare']=s
                items.append(job)
        return items
