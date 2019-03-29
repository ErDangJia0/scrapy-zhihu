import scrapy
import json
from Zhihu.items import ZhihuItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    offset = 0
    baseurl = 'https://www.zhihu.com/api/v4/members/xue-xi-pythonde-zheng-que-zi-shi-92/followers?limit=20&offset='
    start_urls = [baseurl + str(offset)]
    quesUrl = 'https://www.zhihu.com/people/'
    topicsUrl = 'https://www.zhihu.com/people/'

    def parse(self, response):
        print(response.url)
        # 将json格式转换为python格式
        data = json.loads(response.text)['data']
        is_end = json.loads(response.text)['paging']['is_end']
        for each in data:
            item = ZhihuItem()
            item['id'] = each['id']
            item['name'] = each['name']
            item['headline'] = each['headline']
            item['gender'] = each['gender']
            item['url_token'] = each['url_token']
            yield scrapy.Request(url=self.quesUrl + item['url_token'] + '/following/questions',
                                 meta={'item': item, 'download_timeout': 10},
                                 callback=self.getQuesHtml)
        # if is_end == False:
        #     self.offset += 20
        #     yield scrapy.Request(self.baseurl + str(self.offset), callback=self.parse)

    def getQuesHtml(self, response):
        item = response.meta['item']
        ques = response.xpath('//div[@class="List-item"]//a/text()').extract()
        qStr = ''
        for q in ques:
            qStr = qStr + ',' + q
        item['question'] = qStr
        yield scrapy.Request(url=self.topicsUrl + item['url_token'] + '/following/topics',
                             meta={'item': item, 'download_timeout': 10},
                             callback=self.getTopicsHtml)

    def getTopicsHtml(self, response):
        item = response.meta['item']
        topics = response.xpath('//div[@class="List-item"]//div[@class="Popover"]/div/text()').extract()
        tStr = ''
        for t in topics:
            tStr = tStr + ',' + t
        item['topics'] = tStr
        yield item
