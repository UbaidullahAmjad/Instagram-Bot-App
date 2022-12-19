# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:51:14 2020

@author: Ali
"""

from instabot import Bot 
import json
import requests
import time
bot = Bot() 

s=requests.get("http://localhost/chat_bot/Table/time.php")

post=s.json()


for row in post:
    idd=row['id']
    passw=row['password']
    image=row['pic']
    desc=row['desc']
    tag=row['tag']
    ss=image[3:]
    
    
#c="C://xamp//htdocs//chat_bot//Table//"+ss
#print(c)    
 
    
caption=desc+" #"+tag
print(caption)



bot.login(username = idd,password = passw) 


#c="C:\\xamp\\htdocs\\chat_bot\\Table\\images\\postsimages\\LoginBG.png"
#c="C:\\xamp\\htdocs\\chat_bot\\Table\\"+ss
c="img-01.png"    
bot.upload_photo(c, caption=desc + "#"+tag ) 
