import os
import urllib
import time

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

places = [{
    'name': 'Kandel',
    'albums': [
        {
            'name': 'positive',
            'id': '0XfM8',
        }, {
            'name': 'negative',
            'id': 'NX3p8'
        }
    ]
}, {
    'name': 'Gschasi',
    'albums': [
        {
            'name': 'positive',
            'id': 'OthOo',
        }, {
            'name': 'negative',
            'id': 'jQIwZ'
        }
    ]
}]

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

for place in places:
    for album in place['albums']:

        path = 'images/' + place['name'] + '/' + album['name']
        if not os.path.exists(path):
            os.makedirs(path)

        for image in client.get_album_images(album['id']):
            filename = time.strftime('%Y-%m-%d_%H-%M.jpg', time.localtime(image.datetime))
            fullfilename = os.path.join( path, filename)
            urllib.urlretrieve(image.link, fullfilename)
