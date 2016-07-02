import os
import requests

from common.utils import current_image_url

api_url = "https://us12.api.mailchimp.com/3.0/"
api_key = os.environ['MAILCHIMP_APIKEY']

def create_content():
    f = open('mailchimp/email-template.html', 'r')
    html = f.read()
    return html.replace('*|WEBCAM_URL|*', current_image_url())

def create_campaign():
    campaign_data = {
            'type': 'regular',
            'recipients': {
                'list_id': 'd6d1d87606'
                },
            'settings': {
                'subject_line': 'Es scheint jemand fliegen zu gehen!',
                'from_name': 'Kandel Webcam',
                'reply_to': 'kandel-webcam@posteo.de'
                }
            }
    endpoint = api_url + 'campaigns'
    response = requests.post(endpoint, auth=('apikey', api_key), json=campaign_data)
    campaign_id = response.json()['id']


    campaign_data = {
            'html': create_content()
            }
    endpoint = api_url + 'campaigns/' + campaign_id + '/content'
    response = requests.put(endpoint, auth=('apikey', api_key), json=campaign_data)
    return campaign_id

def send_mail(campaign_id):
    endpoint = api_url + 'campaigns/' + campaign_id + '/actions/send'
    response = requests.post(endpoint, auth=('apikey', api_key))


campaign_id = create_campaign()
send_mail(campaign_id)
