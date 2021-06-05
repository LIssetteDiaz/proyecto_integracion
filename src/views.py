from django.shortcuts import render

# Create your views here.


import requests
 
url_stream = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
my_stream_file = requests.get(url_stream, stream=True)
path = 'data/python_guide_stream.pdf'
 
with open(path, 'wb') as f:
    for ch in my_stream_file:
        f.write(ch)