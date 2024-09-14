from instabot import Bot  

bot = Bot()

# log into instagram
bot.login(username='*****', password = '*****')

# Upload the image
bot.upload_photo("image.png",caption='Say hi to my new frnd')

