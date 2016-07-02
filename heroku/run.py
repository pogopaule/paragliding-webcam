import os
import datetime

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from common.utils import current_image_url

def run():
    client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

    url = "http://www.elztalflieger1.de/webcamsp/images/current.jpg"
    try:
        client.upload_from_url(url, config={'album': '1EN5T'}, anon=False)
        print("Uploaded " + url)
    except ImgurClientError as e:
        print(e.error_message)

    url = current_image_url()
    try:
        client.upload_from_url(url, config={'album': 'BN5AE'}, anon=False)
        print("Uploaded " + url)
    except ImgurClientError as e:
        print(url + ' ' + e.error_message)
