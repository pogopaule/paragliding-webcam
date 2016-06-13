import os
import urllib
import time
import random

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from subprocess import call
from PIL import Image

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
}
# , {
    # 'name': 'Gschasi',
    # 'albums': [
        # {
            # 'name': 'positive',
            # 'id': 'OthOo',
        # }, {
            # 'name': 'negative',
            # 'id': 'jQIwZ'
        # }
    # ]
# }
]


def album_size(album):
    return len(client.get_album_images(album['id']))

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

for place in places:

    min_image_number = min(map(album_size, place['albums']))

    for album in place['albums']:

        path = 'images/' + place['name'] + '/' + album['name']
        if not os.path.exists(path):
            os.makedirs(path)

        for image in random.sample(client.get_album_images(album['id']), min_image_number):
            filename = time.strftime('%Y-%m-%d_%H-%M.jpg', time.localtime(image.datetime))
            fullfilename = os.path.join( path, filename)
            Image.open(urllib.urlopen(image.link)).crop((0, 500, 1500, 1100)).save(fullfilename)
