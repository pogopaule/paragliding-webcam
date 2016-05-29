import datetime
import urllib

def current_image_url():
    time = datetime.datetime.now()
    hour = str(time.hour + 2).zfill(2)
    minute = str(time.minute / 15 * 15).zfill(2)
    return "http://www.dgfc-suedschwarzwald.de/webcam2/image-{0}-{1}.jpg".format(hour, minute)
