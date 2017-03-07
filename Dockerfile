FROM kaixhin/caffe:latest

ADD start.py requirements.txt paragliding-webcam/
ADD mailchimp/__init__.py mailchimp/email-template.html mailchimp/sendmail.py paragliding-webcam/mailchimp/
ADD common/__init__.py common/utils.py paragliding-webcam/common/
ADD kandelcaffe/__init__.py kandelcaffe/digits.py paragliding-webcam/kandelcaffe/
ADD kandelcaffe/model/deploy.prototxt kandelcaffe/model/kandel.caffemodel kandelcaffe/model/mean.binaryproto paragliding-webcam/kandelcaffe/model/

ENV CAFFE_DIR /root/caffe

RUN pip install -r paragliding-webcam/requirements.txt
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN sudo ln /dev/null /dev/raw1394

CMD cd paragliding-webcam && python start.py
