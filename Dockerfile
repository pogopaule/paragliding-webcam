FROM kaixhin/caffe:latest

ADD caffe/kandel.caffemodel caffe/deploy.prototxt caffe/positive-probability.py common/utils.py paragliding-webcam/

# https://stackoverflow.com/questions/37379611/how-do-i-interpret-pycaffe-classify-py-output
ADD caffe-fixes/classifier.py python/caffe/

# https://stackoverflow.com/questions/28692209/using-gpu-despite-setting-cpu-only-yielding-unexpected-keyword-argument/28979649#28979649
ADD caffe-fixes/io.py python/caffe/

ENV CAFFE_DIR /root/caffe
