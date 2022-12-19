from instabot import Bot 
from time import sleep
import sys
bot = Bot()

#bot.login(username = "usmanaslam406",password = "usman11?") 


x=["abdul_jabbar_a_j","arsalan.ak47","muhammad.ali797"]


for row in x:
    #print(row)
    bot.login(username = "usmanaslam406",password = "usman11?") 
    bot.follow(row)
    print(row)
    #sys.exit()
    #bot.logout()
    
    sleep(10)