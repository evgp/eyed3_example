# -*- coding: utf-8 -*-

from pprint import pprint
import re, eyed3, os, io

lectures = {} # num: file
podcasts = {} # num: file

file_path = '/mnt/c/dev/scrapy_eslpod/scrapy_selenium_test/Cultural English 1 - 100/'
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
    try:
        pprint("Processing file " + podcasts[pod_key].decode('utf-8'))
        pod = eyed3.load(file_path + podcasts[pod_key])
        with io.open(file_path+lectures[pod_key], mode='r', encoding='utf-8') as f:
            lyric = f.read()
        lyric = re.sub(u"(\u201c|\u201d)", '\"', lyric)
        lyric = re.sub(u"(\u2018|\u2019)", "'", lyric)
        lyric = re.sub(u"(\u2013|\u2014)", "-", lyric)        
        lyric = re.sub(u"(\u2026)", "...", lyric)        
        new_name = unicode(lectures[pod_key])
        pod.tag.title = new_name[:-4]
        pod.tag.lyrics[0].text = unicode(lyric)
        pod.tag.save()
        pod.rename(new_name[:-4])
    except:
        pprint("!!! Errors with file: " + lectures[pod_key].decode('utf-8'))