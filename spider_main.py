#!/usr/bin/python
#coding:utf8
import url_manager,html_downloader,html_outputer,html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls=  url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser=  html_parser.HtmlParser()
        self.outputer=  html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                url=self.urls.get_new_url()
                #parse
                print 'craw %d : %s' % (count,url)
                html_str=self.downloader.download(url)
                new_urls,new_data=self.parser.parse(url,html_str)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except:
                print 'craw failed'
            if count==5:
                break;
            count=count+1

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

