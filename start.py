import time
import schedule
import kandelcaffe.digits
import mailchimp.sendmail
import common.utils
import datetime


def calculate_probability(url):
    return kandelcaffe.digits.classify('kandelcaffe/model/kandel.caffemodel', 'kandelcaffe/model/deploy.prototxt', [url], 'kandelcaffe/model/mean.binaryproto', None, False)

def job():
    global delay_countdown
    print '------------------'
    print datetime.datetime.now()

    hour = datetime.datetime.now().hour
    if hour > 8 and hour < 22 and delay_countdown <= 0:
        url = common.utils.current_image_url(0)
        print url
        try:
            prob = calculate_probability(url)
            print prob
            if prob > 0.6:
                campaign_id = mailchimp.sendmail.create_campaign(url)
                mailchimp.sendmail.send_mail(campaign_id)
                delay_countdown = 12
                print 'mail!'
        except IOError:
            print 'Could not load image'
    else:
        print 'sleeping'

    delay_countdown = delay_countdown - 1


delay_countdown = 0
schedule.every(15).minutes.do(job)

job()

while True:
    schedule.run_pending()
    time.sleep(1)
