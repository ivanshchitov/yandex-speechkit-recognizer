__author__ = 'Ivan Shchitov <ivan.shchitov@jabber.ru>'

import argparse
import requests
import sys
import xml.etree.ElementTree

api_key = '936e9bf4-b019-494d-9cfc-931a62bc0886'
uuid = '01ae13cb744628b58fb536d496daa1e6'
headers = {'Content-Type': 'audio/x-pcm;bit=16;rate=16000'}


def wav_type(path):
    if not path.endswith('.wav'):
        raise argparse.ArgumentTypeError('Файл %s имеет неверный формат. Используйте только wav-файлы.' % path)
    return path

parser = argparse.ArgumentParser()
for i in sys.argv[1:]:
    parser.add_argument('filename', help='wav file', type=wav_type)
args = parser.parse_args()

for arg in sys.argv[1:]:
    data = open(arg, 'rb').read()
    r = requests.post(url='http://asr.yandex.net/asr_xml?key=%s&uuid=%s&topic=notes' % (api_key, uuid),
                      data=data, headers=headers)
    recognized_strings = map(lambda item: item.text, xml.etree.ElementTree.fromstring(r.text))
    for string in recognized_strings:
        print(string)
