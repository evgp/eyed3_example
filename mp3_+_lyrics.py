# -*- coding: utf-8 -*-

from pprint import pprint
import re, eyed3, os, io

lectures = {} # num: file
podcasts = {} # num: file

file_path = '/mnt/c/dev/scrapy_eslpod/scrapy_selenium_test/Daily English 301 - 400/'
file_list = os.listdir(file_path)

for file_name in file_list:
    if ".txt" in file_name:
        m = re.search('\d+', file_name)
        lectures.update({
            int(m.group(0)):file_name
        })
    elif ".mp3" in file_name:
        m = re.search('\d+', file_name)
        podcasts.update({
            int(m.group(0)):file_name
        })

for pod_key in podcasts:
        pprint("Processing file " + podcasts[pod_key].decode('utf-8'))
        pod = eyed3.load(file_path + podcasts[pod_key])
        with io.open(file_path+lectures[pod_key], mode='r', encoding='utf-8') as f:
            lyric = f.read()
        new_name = unicode(lectures[pod_key])
        pod.rename(new_name[:-4])
        pod.tag.title = new_name[:-4]
        pod.tag.lyrics[0].text = unicode(lyric)
        pod.tag.save()
