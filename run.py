import os
from imgurpython import ImgurClient

client = ImgurClient(os.environ['IMGUR_CLIENT_ID'], os.environ['IMGUR_CLIENT_SECRET'])

authorization_url = client.get_auth_url('pin')
print("Go to the following URL: {0}".format(authorization_url))
pin = raw_input("Enter pin code: ")
credentials = client.authorize(pin, 'pin')
client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

print("Authentication successful! Here are the details:")
print("   Access token:  {0}".format(credentials['access_token']))
print("   Refresh token: {0}".format(credentials['refresh_token']))

config = {
            'album': '1EN5T'
        }
client.upload_from_url("http://www.elztalflieger1.de/webcamsp/images/current.jpg", config=config, anon=False)
