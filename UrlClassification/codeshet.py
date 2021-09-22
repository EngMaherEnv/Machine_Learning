# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:14:50 2021

@author: STC

#create  a scrapy
scrapy genspider newsScraper https://www.haberler.com/kim-jong-un-aldigi-kararlara-uymayan-kisiyi-14161887-haberi/
 
# start the scrpy with jeson out put
scrapy runspider featureEx.py -o allLinks.json
"""


# define string
string = "Python is awesome,1 /Python.nofollow is awesome Python is awesome Python/ is awesome 34.Python is awesome/ Python is awesome Python is 5awesome Python is awesome Pyt/hon/ is awesome Python is "




#can i follow 
follow_allowed=True
if 'nofollow' in  string:
    follow_allowed=False




if 'login' in "https://qoshe.com/login":
    print('yes')