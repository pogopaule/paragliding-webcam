import os
from imgurpython import ImgurClient

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

config = {
            'album': '1EN5T'
        }
client.upload_from_url("http://www.elztalflieger1.de/webcamsp/images/current.jpg", config=config, anon=False)
