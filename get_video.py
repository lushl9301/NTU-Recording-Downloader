#!/usr/bin/python

import sys
import subprocess
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def USAGE():
	print("ERROR!\nUSAGE: python3 get_video.py http://presentur.ntu.edu.sg/podcast/rss/rss****_2.xml")
	return

def GET_metafile(url):
	page_source = urlopen(url).read()
	soup = BeautifulSoup(page_source)
	meta_url_list = []
	for link in soup.find_all('item'):
		title = link.find('title').contents[0]
		meta_url = link.find('enclosure').get('url').replace("?", "/?")
		meta_url_list.append((title, meta_url))
	# sort by date
	meta_url_list.sort(key=lambda tup: tup[0])
	video_index = 0
	for (title, meta_url) in meta_url_list:
		print("===========")
		video_index += 1
		print("video :", video_index)
		command = "curl -X GET '" + meta_url + "'"
		# use curl to GET media link via metafile
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		process.wait()
		stdout, stderr = process.communicate()
		media_url = BeautifulSoup(stdout.decode('ascii')).find_all('a', href=True)[0]['href']
		
		video_name = str(video_index) + " " + title + ".mp4"
		command = "curl -X GET '" + media_url + "' > " + video_name
		# print(command)
		process = subprocess.Popen(['curl', '-X', 'GET', media_url, '-o', video_name], shell=False)
		process.wait()
		print(process.returncode)
		print("\n---------\n\n")
		print(len(meta_url_list) - video_index, "video(s) to be downloaded")



if len(sys.argv) != 2:
	USAGE()
	exit(0)
regex = re.compile(
	r'^(?:http|ftp)s?://' # http:// or https://
	r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	r'localhost|' #localhost...
	r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	r'(?::\d+)?' # optional port
	r'(?:/?|[/?]\S+)$', re.IGNORECASE)
if regex.match(sys.argv[1]):
	GET_metafile(sys.argv[1])
else:
	USAGE()
