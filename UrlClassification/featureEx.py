import scrapy
import mimetypes
from deep_translator import GoogleTranslator
import pickle


class FeatureexSpider(scrapy.Spider):
    name = 'featureEx'
    start_urls = ['http://haberler.com/','https://www.sondakika.com/','https://www.theworldnews.net/','https://www.headtopics.com/','https://www.borsagundem.com/','https://www.qoshe.com/','https://www.tr.sputniknews.com/','https://www.turkish.shafaqna.com/','https://www.haberturk.com/','https://www.gazetevatan.com/','https://www.posta.com.tr/','https://www.f5haber.com/',]

    def parse(self, response):
        baseUrl=response.url
        NoFollowKeyword=['contact','contact us','login','log in','about us','about us','terms of use','privacy policy','cookie policy','terms and conditions','sign in','sign up','signin','signup','authors','membership','info']
        Links= response.xpath('/html//a')
        
        for a in Links:
            
            href=a.xpath('.//@href').get()
            rel=a.xpath('.//@rel').get()
            title=a.xpath('.//@title').get()
            
            self.log('///////////////////////////////////////////////////')
            self.log(baseUrl)
            self.log(len(Links))
            self.log(href)
            self.log('///////////////////////////////////////////////////')
            
            if "www" not in href :
                href=response.urljoin(href)
            urlLength=len(href)
            titleLength=0
            if title is not None:
                titleLength=len(title)
                
            nOfForwardSlash = href.count('/')
            nOfDot = href.count('.')
            nOfAnd = href.count('&')
            nOfEqual = href.count('=')
            nOfSemicolon = href.count(';')
            nOfPercent= href.count('%')
            nOfAt  = href.count('@')
            nOfHyphen = href.count('–')
            nOfUnderscore = href.count('_')
            nOfComma= href.count(',')
            nOfHash= href.count('#')
            
            # count numbers in title 
            nOfDdigits=0
            try:
                for i in title:
                    if(i.isdigit()):
                        nOfDdigits=nOfDdigits+1
            except:
                nOfDdigits=0
            
            #is the link is going to change our website
            baseUrlNoHttp = baseUrl.split("www.", 1)
            otherWebsiteLink=False
            
            try:
                
                if baseUrlNoHttp[1] not in href:
                    otherWebsiteLink=True
            except:
                otherWebsiteLink=True
                
            #can i follow 
            follow_allowed=False
            rel=''
            if len(rel)==0:
                follow_allowed=True
            
            print(follow_allowed,len(rel))
            
            #is it a file link lik jpg or zip 
            fileLink, _ = mimetypes.guess_type(href)
            isFileLink=False
            if fileLink is not None:
                isFileLink=True
            
            
            #is it  only base url 
            isBaseOnly=False
            if  baseUrl==href or href=='/' :
                isBaseOnly=True
                
            #is the link contains any non important pages    
            containsNOfollowKeyword=False
            categorybysplit=''
            translatedCategoy=''
            try:
                if (otherWebsiteLink==False and isBaseOnly==False ):
                        categorybysplit=href.split(baseUrl)[1:]
                        toBeTranslate=categorybysplit[0]+title
                        translatedCategoy= GoogleTranslator(source='auto', target='en').translate(toBeTranslate)
                        if any(word in translatedCategoy.lower() for word in NoFollowKeyword):
                            containsNOfollowKeyword=True
            except:
                translatedCategoy='no words'
                
            isNews=False
            if(isBaseOnly==False and isFileLink==False and  follow_allowed==True  and otherWebsiteLink==False and containsNOfollowKeyword==False):
                isNews=True
                 
                
            linkFeatures={
                'isNews':isNews,
                'otherWebsiteLink':otherWebsiteLink,
                'href':href,
                'follow_allowed':follow_allowed,
                'isFileLink':isFileLink,
                'isBaseOnly':isBaseOnly,
                'containsNOfollowKeyword':containsNOfollowKeyword,
                'rel':rel,
                'title':title,
                'urlLength':urlLength,
                'titleLength':titleLength,
                'nOfDdigits':nOfDdigits,
                'nOfForwardSlash':nOfForwardSlash,
                'nOfDot':nOfDot,
                'nOfAnd':nOfAnd,
                'nOfEqual':nOfEqual,
                'nOfSemicolon':nOfSemicolon,
                'nOfPercent':nOfPercent,
                'nOfAt':nOfAt,
                'nOfHyphen':nOfHyphen,
                'nOfUnderscore':nOfUnderscore,
                'nOfComma':nOfComma,
                'nOfHash':nOfHash,
                }
            yield linkFeatures
         
            

            