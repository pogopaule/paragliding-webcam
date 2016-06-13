import os
import webbrowser

from imgurpython import ImgurClient

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'], os.environ['IMGUR_ACCESS_TOKEN'], os.environ['IMGUR_REFRESH_TOKEN'])

albums = [{
    'album_id': 'BN5AE',
    'positive_album_id': '0XfM8',
    'negative_album_id': 'NX3p8'
}, {
    'album_id': '1EN5T',
    'positive_album_id': 'OthOo',
    'negative_album_id': 'jQIwZ'
}]


for album in albums:
    positive_images = []
    negative_images = []
    album_id = album['album_id']
    positive_album_id = album['positive_album_id']
    negative_album_id = album['negative_album_id']

    for image in client.get_album_images(album_id):
        webbrowser.open(image.link)
        answer = raw_input('Activity on picture? (y/n/s): ')
        if answer == 's':
            break
        elif answer == 'y':
            positive_images.append(image.id)
        else:
            negative_images.append(image.id)

    client.album_add_images(positive_album_id, positive_images)
    client.album_add_images(negative_album_id, negative_images)
    client.album_remove_images(album_id, positive_images)
    client.album_remove_images(album_id, negative_images)
