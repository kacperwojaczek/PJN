#!/usr/bin/python

import re
import requests
import json
from BeautifulSoup import BeautifulSoup

apiKey = 'cb8c1c86239a4fdcbacf4244f17084a8'
apiUrl = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?query='
imdbApiUrl = 'http://www.omdbapi.com/?r=json&t='

def cleanhtml(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

class Review:

	movieTitle = ''
	reviewContent = ''
	movieRating = ''

	def __init__(self, title):
		self.movieTitle = title
		try:
			self.fetchReview()
			self.fetchRating()
		except:
			print 'Film not found'
			self.movieTitle = ''
			self.reviewContent = ''
			self.movieRating = ''

	def fetchReview(self):
		response = requests.get(apiUrl + self.movieTitle + '&api-key=' + apiKey)
		if response.status_code == 200:
			response = response.json()
			self.movieTitle = response['results'][0]['display_title']
			self.parseReview(response['results'][0]['link']['url'])

	def parseReview(self, reviewLink):
		page = requests.get(reviewLink)
		html = page.content
		soup = BeautifulSoup(html)
		paragraphs = soup.findAll("p")
		for paragraph in paragraphs:
			self.reviewContent += cleanhtml(unicode(paragraph.contents[0]))

	def fetchRating(self):
		response = requests.get(imdbApiUrl + self.movieTitle)
		if response.status_code == 200:
			response = response.json()
			self.movieRating = response['imdbRating']	

