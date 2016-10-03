import kandelcaffe.digits
import sys

def calculate_probability(url):
    return kandelcaffe.digits.classify('kandelcaffe/model/kandel.caffemodel', 'kandelcaffe/model/deploy.prototxt', [url], 'kandelcaffe/model/mean.binaryproto', None, False)

def build_url(time):
    return 'http://www.dgfc-suedschwarzwald.de/webcam2/image-{}-{}.jpg'.format(time[0:2], time[2:4])


print calculate_probability(build_url(sys.argv[1]))
