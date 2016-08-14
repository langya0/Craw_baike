#!/usr/bin/python
#coding:utf8

import urllib2

class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""

	def download(self,url):
		if url is None:
			return None

		response = urllib2.urlopen(url)
		# print ("in down",response.read())
		if response.getcode()!=200:
			return None

		# print (response.read())
		return response.read()

