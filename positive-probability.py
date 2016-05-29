import caffe
import utils
import urllib
from PIL import Image

caffe.set_mode_cpu()

classifier = caffe.Classifier('deploy.prototxt', 'webcam.caffemodel')
Image.open(urllib.urlopen('http://i.imgur.com/3pptFmk.jpg')).crop((0, 500, 1500, 1100)).save('temp.jpg')

predictions = classifier.predict([caffe.io.load_image('temp.jpg')])

positive_propability = predictions

print positive_propability
