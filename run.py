import os
import datetime

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

def run():
    client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

    url = "http://www.elztalflieger1.de/webcamsp/images/current.jpg"
    try:
        client.upload_from_url(url, config={'album': '1EN5T'}, anon=False)
        print("Uploaded " + url)
    except ImgurClientError as e:
        print(e.error_message)

    time = datetime.datetime.now()
    hour = str(time.hour).zfill(2)
    minute = str(time.minute / 15 * 15).zfill(2)
    url = "http://www.dgfc-suedschwarzwald.de/webcam2/image-{0}-{1}.jpg".format(hour, minute)
    try:
        client.upload_from_url(url, config={'album': 'BN5AE'}, anon=False)
        print("Uploaded " + url)
    except ImgurClientError as e:
        print(url + ' ' + e.error_message)
