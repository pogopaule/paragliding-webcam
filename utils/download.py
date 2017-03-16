import os
import urllib
import random
import io
import sys
import hashlib

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
            try:
                fd = urllib.urlopen(image.link)
                image_file = io.BytesIO(fd.read())
                image = Image.open(image_file)
                md5 = hashlib.md5()
                md5.update(image.tobytes().decode('base64'))
                filename = md5.hexdigest() + '.jpg'
                fullfilename = os.path.join(path, filename)
                left = 200
                top = 750
                width = 1200
                height = 350
                image.crop((left, top, left+width, top+height)).save(fullfilename)
                sys.stdout.write('.')
                sys.stdout.flush()
            except IOError:
                if hasattr(image, 'link'):
                    print('Could not download: ' + image.link)
                else:
                    print('Could not download: ' + str(image))
