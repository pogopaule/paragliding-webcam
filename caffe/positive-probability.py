import caffe
import urllib
import numpy
from PIL import Image
import os

caffe.set_mode_cpu()

caffe_dir = os.environ['CAFFE_DIR']
mean = numpy.load(caffe_dir + '/python/caffe/imagenet/ilsvrc_2012_mean.npy')
image_dims = [256, 256]
channel_swap=[2,1,0]
input_scale=None
raw_scale=255.0

url = 'https://i.imgur.com/VAJfCk8.jpg'

classifier = caffe.Classifier('caffe/deploy.prototxt', 'caffe/kandel.caffemodel', image_dims=image_dims, mean=mean, channel_swap=channel_swap, input_scale=input_scale, raw_scale=raw_scale)
Image.open(urllib.urlopen(url)).crop((0, 500, 1500, 1100)).save('temp.jpg')

predictions = classifier.predict([caffe.io.load_image('temp.jpg')], True)

positive_propability = predictions[0][1]

print positive_propability
