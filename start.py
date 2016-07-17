import time
import schedule
import kandelcaffe.digits
import mailchimp.sendmail
import common.utils
import datetime

next_hour = 8

def calculate_probability(url):
    return kandelcaffe.digits.classify('kandelcaffe/model/kandel.caffemodel', 'kandelcaffe/model/deploy.prototxt', [url], 'kandelcaffe/model/mean.binaryproto', None, False)

def job():
    global next_hour
    hour = datetime.datetime.now().hour
    if hour > 7 and hour >= next_hour and hour < 22:
        url = common.utils.current_image_url(0)
        prob = calculate_probability(url)
        if prob > 0.6:
            campaign_id = mailchimp.sendmail.create_campaign(url)
            mailchimp.sendmail.send_mail(campaign_id)
            print 'mail!'
            next_hour = hour + 4

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
