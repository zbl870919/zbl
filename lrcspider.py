# -*- coding: utf-8 -*-
#Filename:lrcspider.py
import urllib
from HTMLParser import HTMLParser
import sys
import traceback


success = 0
def changecode():
    try:
        new = 'utf-8'
        default = sys.getdefaultencoding()
        print default,new
        if new != default:
            reload(sys)
            print(default,new)
            sys.setdefaultencoding(new)
    except Exception,e:
        print 'changecode except'
        print Exception,":",e
        #traceback.print_exc()
    else:
        print sys.getdefaultencoding()
    finally:
        print sys.getdefaultencoding()
        
def spider(url):
    content = ''
    try:
        f = urllib.urlopen(url)
        #print f
        content = f.read()
        #print content
    except:
        print 'spider exception:' + url, 
    return content
 

class myHtmlParser(HTMLParser):  
    #处理<!开头的内容  
    #def handle_decl(self,decl):  
        #print 'Encounter some declaration:'+ decl  
    def handle_starttag(self,tag,attrs):  
        if tag == 'a':    
            for attr in attrs:
                if len(attr) == 2 and attr[0] == 'class' and attr[1].startswith('down-lrc-btn'):
                    #print "attr [%d]:%s" % (len(attr), attr)
                    url = '''http://music.baidu.com''' + attr[1][23:-3]
                    #print url
                    idx = url.rfind('/')
                    if idx != -1:
                        path = 'F:\\Python\\lrc\\' + url[idx+1:]
                        print path
                        lrc = spider(url)
                        if len(lrc) > 0:
                            f = file(path, 'w')   # open for 'w'riting
                            f.write(lrc)               # write text to file
                            f.close()                   # close the file

    #def handle_endtag(self,tag):  
        #print 'Encounter the end of a %s tag' % tag  
    #处理注释  
    #def handle_comment(self,comment):   
        #print 'Encounter some comments:' + comment

if __name__ == '__main__':
    idx = 0
    while True:
        url = '''http://music.baidu.com/search/lrc?key=%s&start=%d&size=20&third_type=0''' % ('%E6%AD%8C%E8%AF%8D', idx)
        print url 
        content = spider(url)
        if len(content) > 0:
            try:
                htmlparser = myHtmlParser()
                htmlparser.feed(content)
            except Exception,e:
                print Exception,":",e
                #traceback.print_exc()
        idx += 20
        if idx > 10000:
            break
    
    
