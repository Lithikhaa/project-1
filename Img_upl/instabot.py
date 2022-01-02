
import os
import glob
from instabot import Bot
bot = Bot()
# cookie_del = glob.glob("config/*cookie.json")
# if cookie_del : os.remove(cookie_del[0])

bot.login(username = "kavikathir76", password= "Lithi2426" )
image ="bright.jpg"
bot.upload_photo(image,caption="Post uploaded")