import os
import urllib
import time

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

for image in client.get_album_images('1EN5T'):
    filename = time.strftime('%Y-%m-%d_%H-%M.jpg', time.localtime(image.datetime))
    fullfilename = os.path.join( '/Users/fabian/Downloads/paragliding-webcam/gschasi/', filename)
    urllib.urlretrieve(image.link, fullfilename)

for image in client.get_album_images('BN5AE'):
    filename = time.strftime('%Y-%m-%d_%H-%M.jpg', time.localtime(image.datetime))
    fullfilename = os.path.join( '/Users/fabian/Downloads/paragliding-webcam/kandel/', filename)
    urllib.urlretrieve(image.link, fullfilename)
